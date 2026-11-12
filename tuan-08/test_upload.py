import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_upload_invalid_file_fail_case():
    """
    Test case (Fail): Cố tình upload file sai định dạng (.exe).
    Sử dụng Explicit Wait, không dùng time.sleep().
    Kết quả: FAILED do hệ thống không chặn file lỗi (trang The Internet nhận mọi file).
    """
    # Bước 1: Tạo một file không hợp lệ (.exe) để test "invalid input" theo đúng đề bài
    test_file_path = os.path.abspath("virus_gia.exe")
    with open(test_file_path, "w") as f:
        f.write("Day la file exe dung de test invalid input.")

    # Bước 2: Khởi tạo trình duyệt
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)

    try:
        # Bước 3: Điều hướng đến trang Upload 
        driver.get("https://the-internet.herokuapp.com/upload")

        # Bước 4: Tìm thẻ input file và nút submit 
        file_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
        upload_button = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))

        # Bước 5: Truyền đường dẫn file .exe (invalid input) vào
        file_input.send_keys(test_file_path)

        # Bước 6: Bấm nút upload
        upload_button.click()

        # Bước 7: Chờ phần tử chứa kết quả hiển thị
        result_message = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))

        # Bước 8: Kiểm tra thông báo lỗi (Assert the error message)
        # Đưa vào file .exe, ta KỲ VỌNG web phải chặn và báo lỗi "Unsupported file format"
        # NHƯNG thực tế web lại hiện "File Uploaded!" -> Lệnh assert này sẽ gây ra lỗi FAILED
        assert result_message.text == "Unsupported file format", \
            f"LỖI: Đưa vào file .exe nhưng web không chặn, lại báo '{result_message.text}'"

    finally:
        # Bước 9: Dọn dẹp
        driver.quit()
        if os.path.exists(test_file_path):
            os.remove(test_file_path)