import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

UPLOAD_URL = "https://the-internet.herokuapp.com/upload"


@pytest.fixture
def driver():
    """Fixture dùng chung: Khởi tạo Chrome và tự động đóng sau khi test xong."""
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_upload_file_invalid(driver):
    """Negative test: Bấm Upload khi không chọn file."""
    wait = WebDriverWait(driver, 15)
    driver.get(UPLOAD_URL)

    upload_button = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))
    upload_button.click()

    # Chờ nội dung hiển thị trên thẻ body xuất hiện thông báo lỗi
    wait.until(
        lambda d: "Internal Server Error" in d.find_element(By.TAG_NAME, "body").text
        or "No file was chosen" in d.find_element(By.TAG_NAME, "body").text
    )

    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Internal Server Error" in body_text or "No file was chosen" in body_text, \
        f"Không tìm thấy thông báo lỗi khi upload file rỗng! Nội dung thực tế: '{body_text}'"


def test_upload_invalid_file_fail_case(driver, tmp_path):
    """Negative test: Upload file sai định dạng (.exe) dùng fixture driver và tmp_path."""
    test_file = tmp_path / "virus_gia.exe"
    test_file.write_text("Day la file exe dung de test invalid input.", encoding="utf-8")

    wait = WebDriverWait(driver, 10)
    driver.get(UPLOAD_URL)

    file_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
    upload_button = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))

    file_input.send_keys(str(test_file))
    upload_button.click()

    result_message = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
    assert result_message.text == "File type not allowed", \
        f"Kỳ vọng web báo 'File type not allowed', nhưng thực tế trả về '{result_message.text}'"


def test_upload_valid_file(driver, tmp_path):
    """TC01 (Pass case): Kiểm thử tải lên tệp hợp lệ thành công."""
    test_file = tmp_path / "kiem_thu_nhom08.txt"
    test_file.write_text("Noi dung kiem thu tu dong - Nhom C06-N08", encoding="utf-8")

    wait = WebDriverWait(driver, 10)
    driver.get(UPLOAD_URL)

    file_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
    file_input.send_keys(str(test_file))

    upload_button = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))
    upload_button.click()

    success_heading = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3")))
    assert "File Uploaded!" in success_heading.text, (
        f"Tiêu đề trang không đúng: '{success_heading.text}', kỳ vọng chứa 'File Uploaded!'"
    )

    uploaded_filename_el = wait.until(EC.visibility_of_element_located((By.ID, "uploaded-files")))
    actual_filename = uploaded_filename_el.text.strip()
    assert actual_filename == test_file.name, (
        f"Tên tệp không khớp: nhận được '{actual_filename}', kỳ vọng '{test_file.name}'"
    )