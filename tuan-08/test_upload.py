import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_upload_file_invalid(driver):
    # Bước 1: Mở trang web upload
    driver.get("https://the-internet.herokuapp.com/upload")
    
    # Bước 2: Chờ nút Upload (ID: file-submit) xuất hiện và bấm vào mà không chọn file
    wait = WebDriverWait(driver, 15)
    upload_button = wait.until(
        EC.element_to_be_clickable((By.ID, "file-submit"))
    )
    upload_button.click()
    
    # Bước 3: Chờ cho đến khi URL thay đổi hoặc nội dung trang báo lỗi xuất hiện
    wait.until(lambda d: "Internal Server Error" in d.page_source or "No file was chosen" in d.page_source)
    
    # Bước 4: Xác nhận thông báo lỗi xuất hiện đúng như dự kiến (Negative Test)
    assert "Internal Server Error" in driver.page_source or "No file was chosen" in driver.page_source, \
        "Không tìm thấy thông báo lỗi khi upload file rỗng!"