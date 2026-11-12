import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_upload_invalid_file_fail_case():
    """
    Test case (Fail): Kiểm thử tính năng Upload file trên trang The Internet.
    Sử dụng Explicit Wait, không dùng time.sleep().
    Kết quả: Bắt buộc FAILED do cố tình assert kỳ vọng sai kết quả trả về.
    """
    # Bước 1: Tạo một file .txt giả ở local để upload
    test_file_path = os.path.abspath("unsupported_format.txt")
    with open(test_file_path, "w") as f:
        f.write("Day la file text de test chuc nang upload.")

    # Bước 2: Khởi tạo trình duyệt
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)

    try:
        # Bước 3: Điều hướng đến trang Upload của The Internet
        driver.get("https://the-internet.herokuapp.com/upload")

        # Bước 4: Tìm thẻ input file và nút submit dựa theo ID của trang The Internet
        file_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
        upload_button = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))

        # Bước 5: Truyền đường dẫn file tuyệt đối vào thẻ input
        file_input.send_keys(test_file_path)

        # Bước 6: Bấm nút upload
        upload_button.click()

        # Bước 7: Chờ thẻ h3 chứa kết quả xuất hiện
        # Trang này khi upload xong sẽ hiện một thẻ h3 có chữ "File Uploaded!"
        result_message = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))

        # Bước 8: Cố tình Assert sai để test case FAILED
        # Sự thật là file up thành công, nhưng ta kỳ vọng nó phải quăng ra lỗi từ chối
        assert result_message.text == "Lỗi định dạng file!", \
            f"LỖI CỐ TÌNH: Web trả về '{result_message.text}' nhưng test lại kỳ vọng báo lỗi!"

    finally:
        # Bước 9: Dọn dẹp - Đóng trình duyệt và xóa file giả
        driver.quit()
        if os.path.exists(test_file_path):
            os.remove(test_file_path)