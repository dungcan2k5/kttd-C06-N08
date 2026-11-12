import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) # Thiết lập Implicit Wait 10 giây
    yield driver
    # Đóng trình duyệt sau khi kiểm thử đã hoàn tất
    driver.quit()

def test_upload_file_invalid(driver):
    # Bước 1: Mở trang web upload
    driver.get("https://the-internet.herokuapp.com/upload")
    
    # Bước 2: Sử dụng Explicit Wait để chờ nút Upload hiển thị và có thể tương tác
    wait = WebDriverWait(driver, 10)
    upload_button = wait.until(
        EC.element_to_be_clickable((By.ID, "file-submit"))
    )
    
    # Bước 3: Cố tình nhấn nút Upload mà KHÔNG chọn file trước (Negative Test)
    upload_button.click()
    
    # Bước 4: Chờ thông báo lỗi hoặc trang kết quả tải xong
    error_header = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )
    
    # Bước 5: Kiểm tra nội dung báo lỗi (Assert) để xác nhận kịch bản thất bại đúng dự kiến
    assert "Internal Server Error" in error_header.text or "Error" in error_header.text, \
        "Kịch bản không hiển thị thông báo lỗi như mong đợi!"