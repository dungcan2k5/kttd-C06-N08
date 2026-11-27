
import pytest
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://the-internet.herokuapp.com"


@pytest.fixture
def driver():
    # Khởi tạo Chrome và bật Performance Log để theo dõi HTTP response.
    options = webdriver.ChromeOptions()
    options.set_capability(
        "goog:loggingPrefs",
        {"performance": "ALL"}
    )

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    yield browser

    # Đóng trình duyệt sau khi mỗi test kết thúc.
    browser.quit()


def get_http_status(driver, endpoint):
    """
    Lấy mã HTTP status từ Chrome Performance Log.
    Chỉ lấy response thuộc endpoint đang kiểm thử.
    """
    logs = driver.get_log("performance")
    statuses = []

    for entry in logs:
        message = json.loads(entry["message"])["message"]

        if message["method"] == "Network.responseReceived":
            response = message["params"]["response"]

            if endpoint in response["url"]:
                statuses.append(response["status"])

    return statuses


@pytest.mark.parametrize(
    "endpoint",
    ["basic_auth", "digest_auth"]
)
def test_auth_valid(driver, endpoint):
    # Chèn username và password trực tiếp vào URL.
    # Cấu trúc: https://username:password@domain/path
    # Trình duyệt sẽ sử dụng thông tin này khi thực hiện xác thực HTTP.
    url = f"{BASE_URL.replace('https://', 'https://admin:admin@')}/{endpoint}"

    # Xóa log cũ trước khi thực hiện request.
    driver.get_log("performance")

    driver.get(url)

    # Chờ nội dung xác nhận đăng nhập thành công xuất hiện.
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h3"))
    )

    # Assertion 1: Nội dung xác nhận phải đúng.
    assert "Congratulations" in success_message.text, \
        f"{endpoint}: Đăng nhập hợp lệ nhưng không thành công"

    # Assertion 2: HTTP response phải trả về 200.
    statuses = get_http_status(driver, f"/{endpoint}")

    assert 200 in statuses, \
        f"{endpoint}: Không nhận được HTTP 200"


@pytest.mark.parametrize(
    "endpoint",
    ["basic_auth", "digest_auth"]
)
def test_auth_invalid(driver, endpoint):
    # Chèn username và password không hợp lệ vào URL.
    # Trình duyệt gửi thông tin xác thực sai đến máy chủ.
    # Máy chủ phải từ chối và trả về HTTP 401 Unauthorized.
    url = f"{BASE_URL.replace('https://', 'https://wrong:wrong@')}/{endpoint}"

    # Xóa log cũ trước khi thực hiện request.
    driver.get_log("performance")

    driver.get(url)

    # Lấy mã HTTP response của endpoint.
    statuses = get_http_status(driver, f"/{endpoint}")

    # Assertion 1: Máy chủ phải trả về HTTP 401.
    assert 401 in statuses, \
        f"{endpoint}: Mong đợi HTTP 401 khi thông tin đăng nhập không hợp lệ"

    # Assertion 2: Không được xuất hiện nội dung xác thực thành công.
    assert "Congratulations" not in driver.page_source, \
        f"{endpoint}: Thông tin đăng nhập sai nhưng vẫn xác thực thành công"

if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_auth.py"])