import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

UPLOAD_URL = "https://the-internet.herokuapp.com/upload"

@pytest.fixture
def driver():
    """Fixture dùng chung cho tất cả các test case"""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

# --- Bài 1: Cố tình upload file sai định dạng (Fail case) ---
def test_upload_invalid_file_fail_case(driver):
    test_file_path = os.path.abspath("virus_gia.exe")
    with open(test_file_path, "w") as f:
        f.write("Day la file exe dung de test invalid input.")

    wait = WebDriverWait(driver, 5)
    
    try:
        driver.get(UPLOAD_URL)
        file_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
        upload_button = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))

        file_input.send_keys(test_file_path)
        upload_button.click()

        result_message = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))

        # Lệnh assert này SẼ GÂY LỖI (FAILED) vì web không chặn file .exe
        assert result_message.text == "Unsupported file format", \
            f"LỖI: Đưa vào file .exe nhưng web không chặn, lại báo '{result_message.text}'"
    finally:
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

# --- Bài 2: Upload không chọn file (Negative Test) ---
def test_upload_file_invalid(driver):
    driver.get(UPLOAD_URL)
    wait = WebDriverWait(driver, 15)
    
    upload_button = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))
    upload_button.click()
    
    wait.until(lambda d: "Internal Server Error" in d.page_source or "No file was chosen" in d.page_source)
    
    assert "Internal Server Error" in driver.page_source or "No file was chosen" in driver.page_source, \
        "Không tìm thấy thông báo lỗi khi upload file rỗng!"

# --- Bài 3: Upload tệp hợp lệ thành công (Pass case) ---
def test_upload_valid_file(driver, tmp_path):
    test_file = tmp_path / "kiem_thu_nhom08.txt"
    test_file.write_text("Noi dung kiem thu tu dong - Nhom C06-N08", encoding="utf-8")
    file_path = str(test_file)

    wait = WebDriverWait(driver, 10)
    driver.get(UPLOAD_URL)

    file_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
    file_input.send_keys(file_path)

    upload_button = driver.find_element(By.ID, "file-submit")
    upload_button.click()

    success_heading = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3")))
    assert "File Uploaded!" in success_heading.text, "Tiêu đề trang không đúng"

    uploaded_filename_el = wait.until(EC.visibility_of_element_located((By.ID, "uploaded-files")))
    actual_filename = uploaded_filename_el.text.strip()
    
    assert actual_filename == test_file.name, "Tên tệp không khớp"