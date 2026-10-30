import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Đóng trình duyệt sau khi test xong
    driver.quit()

def test_checkboxes_fail_case_invalid_action(driver):
    """
    Test case (Fail): Kiểm tra tính năng Checkboxes.
    Sử dụng Explicit Wait để chờ phần tử, tuyệt đối không dùng time.sleep().
    Kết quả: FAILED do thao tác sai (người dùng click đúp) làm sai lệch trạng thái.
    """
    # Khởi tạo Explicit Wait (đợi tối đa 5 giây)
    wait = WebDriverWait(driver, 5)

    # Bước 1: Điều hướng đến trang test Checkboxes
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # Bước 2: Đợi Checkbox 1 tải lên và có thể tương tác bằng Explicit Wait
    checkbox_1 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//form[@id='checkboxes']/input[1]"))
    )

    # Bước 3: THAO TÁC SAI (Invalid input/action)
    # Cố tình click 2 lần (double-click) khiến checkbox được chọn rồi lại bị bỏ chọn
    checkbox_1.click()
    checkbox_1.click()

    # Bước 4: Kiểm tra trạng thái
    # Test sẽ FAILED ngay tại đây vì kỳ vọng là True nhưng thực tế là False
    assert checkbox_1.is_selected(), "LỖI CỐ TÌNH: Thao tác sai (click 2 lần) khiến Checkbox 1 không giữ được trạng thái chọn!"