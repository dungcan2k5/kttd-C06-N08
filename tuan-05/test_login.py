import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL trang đăng nhập cần kiểm thử
LOGIN_URL = "https://the-internet.herokuapp.com/login"

# Thông tin đăng nhập hợp lệ (valid credentials)
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


@pytest.fixture
def driver():
    """
    Test harness fixture: Khởi tạo và giải phóng WebDriver (Setup & Teardown).
    - Setup: Khởi tạo Chrome WebDriver và phóng to cửa sổ trình duyệt.
    - Teardown: Đảm bảo driver.quit() luôn được gọi sau khi hoàn thành test case
      (kể cả khi test pass hoặc fail) để tránh rò rỉ tiến trình browser.
    """
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_valid_credentials(driver):
    """
`    TC01: Kiểm thử đăng nhập thành công với thông tin hợp lệ.
    Mục tiêu: Xác nhận trang /login chấp nhận đúng tài khoản,
    chuyển hướng sang trang bảo mật và hiển thị thông báo thành công.
    Thành viên phụ trách: Nguyễn Tiến Dũng
    """
    screenshot_path = os.path.join(os.path.dirname(__file__), "anh", "tdung.png")
    wait = WebDriverWait(driver, 10)

    # 1. Điều hướng trình duyệt đến trang đăng nhập
    driver.get(LOGIN_URL)

    # 2. Định vị trường nhập tên đăng nhập bằng thuộc tính ID
    username_field = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )

    # 3. Định vị trường nhập mật khẩu bằng thuộc tính ID
    password_field = driver.find_element(By.ID, "password")

    # 4. Định vị nút "Login" bằng CSS Selector (button kiểu submit)
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # 5. Nhập tên đăng nhập hợp lệ vào trường username
    username_field.send_keys(USERNAME)

    # 6. Nhập mật khẩu hợp lệ vào trường password
    password_field.send_keys(PASSWORD)

    # 7. Nhấn nút đăng nhập để gửi form
    login_button.click()

    # 8. Chờ cho đến khi URL thay đổi sang trang bảo mật sau đăng nhập
    wait.until(EC.url_contains("/secure"))

    # 9. Kiểm tra chuyển hướng: URL hiện tại phải chứa "/secure"
    actual_url = driver.current_url
    assert "/secure" in actual_url, (
        f"Chuyển hướng thất bại: URL hiện tại là '{actual_url}', "
        f"kỳ vọng chứa '/secure'"
    )

    # 10. Định vị thông báo flash message thành công
    flash_message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    # 11. Lấy nội dung văn bản của thông báo flash
    flash_text = flash_message.text

    # 12. Kiểm tra thông báo hiển thị đúng nội dung đăng nhập thành công
    assert "You logged into a secure area!" in flash_text, (
        f"Flash message không đúng: '{flash_text}'"
    )

    print("\n✅ Test PASSED: Đăng nhập thành công!")
    print(f"   URL sau đăng nhập : {actual_url}")
    print(f"   Flash message      : {flash_text.strip()}")

    # 13. Chụp ảnh màn hình làm bằng chứng thực thi và lưu vào tuan-05/anh/
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)
    print(f"   Screenshot đã lưu  : {screenshot_path}")


def test_login_invalid_password(driver):
    """
    TC02: Kiểm thử đăng nhập thất bại với mật khẩu sai.
    Mục tiêu: Đảm bảo hệ thống từ chối mật khẩu không đúng và hiển thị
    thông báo lỗi "Your password is invalid!".
    Thành viên phụ trách: Lê Thị Nga
    """
    screenshot_path = os.path.join(os.path.dirname(__file__), "anh", "nga.png")
    wait = WebDriverWait(driver, 10)

    # 1. Điều hướng trình duyệt đến trang đăng nhập
    driver.get(LOGIN_URL)

    # 2. Định vị các phần tử bằng chiến lược Locator
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # 3. Nhập dữ liệu (Username đúng, Password sai)
    username_field.send_keys(USERNAME)
    password_field.send_keys("WrongPassword123!")

    # 4. Kích hoạt hành động đăng nhập
    login_button.click()

    # 5. Chờ và định vị thông báo lỗi flash hiển thị (chứng tỏ đăng nhập bị từ chối)
    error_message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    error_text = error_message.text

    # 6. Assertion: Kiểm tra thông báo lỗi có chứa đoạn text mong đợi hay không
    assert "Your password is invalid!" in error_text, (
        f"Kỳ vọng thấy lỗi 'Your password is invalid!' nhưng nhận được: '{error_text}'"
    )

    print("\n✅ Test PASSED: Đăng nhập thất bại hợp lệ (Bắt đúng thông báo lỗi mật khẩu)!")
    print(f"   Error message hiện ra: {error_text.strip()}")

    # 7. Lưu bằng chứng thực thi
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)
    print(f"   Screenshot đã lưu    : {screenshot_path}")


def test_login_invalid_username(driver):
    """
    TC03: Kiểm thử đăng nhập thất bại với username không tồn tại.
    Mục tiêu: Xác nhận hệ thống hiển thị thông báo lỗi "Your username is invalid!".
    Thành viên phụ trách: Nguyễn Phúc Hưng
    """
    screenshot_path = os.path.join(os.path.dirname(__file__), "anh", "hwng.png")
    wait = WebDriverWait(driver, 10)

    # Dùng username không tồn tại và mật khẩu bất kỳ
    invalid_username = "this_user_does_not_exist_123"
    arbitrary_password = "AnyRandomPassword123!"

    # 1. Mở trang đăng nhập
    driver.get(LOGIN_URL)

    # 2. Dùng ID để định vị ô nhập username
    username_field = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )

    # 3. Dùng ID để định vị ô nhập password
    password_field = driver.find_element(By.ID, "password")

    # 4. Dùng CSS Selector để định vị nút Login
    login_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )

    # 5. Nhập username không tồn tại
    username_field.send_keys(invalid_username)

    # 6. Nhập mật khẩu bất kỳ
    password_field.send_keys(arbitrary_password)

    # 7. Nhấn Login để gửi thông tin đăng nhập
    login_button.click()

    # 8. Chờ thông báo lỗi xuất hiện
    flash_message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    # 9. Lấy nội dung thông báo để kiểm tra
    actual_message = flash_message.text

    # 10. Xác nhận thông báo chứa đúng nội dung theo yêu cầu
    assert "Your username is invalid!" in actual_message, (
        f"Thông báo lỗi không đúng: '{actual_message}'"
    )

    print("\n✅ Test PASSED: Đăng nhập thất bại hợp lệ (Bắt đúng thông báo lỗi username)!")
    print(f"   Error message hiện ra: {actual_message.strip()}")

    # 11. Chụp màn hình thông báo lỗi làm bằng chứng thực thi
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)
    print(f"   Screenshot đã lưu    : {screenshot_path}")


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
