import pytest
import os
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
# URL trang tải tệp lên cần kiểm thử
UPLOAD_URL = "https://the-internet.herokuapp.com/upload"


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


def test_upload_valid_file(driver, tmp_path):
    """
    TC01 (Pass case): Kiểm thử tải lên tệp hợp lệ thành công.
    Mục tiêu: Xác nhận trang /upload chấp nhận tệp được chọn,
    hiển thị tên tệp và thông báo tải lên thành công.
    Thành viên phụ trách: Nguyễn Tiến Dũng
    """
    # --- Chuẩn bị dữ liệu: Tạo tệp văn bản tạm thời để tải lên ---
    # Dùng tmp_path (fixture của pytest) để tạo tệp trong thư mục tạm thời,
    # đảm bảo tệp sạch sẽ và không để lại rác sau khi test kết thúc.
    test_file = tmp_path / "kiem_thu_nhom08.txt"
    test_file.write_text("Noi dung kiem thu tu dong - Nhom C06-N08", encoding="utf-8")
    file_path = str(test_file)

    # Khởi tạo Explicit Wait - chờ tối đa 10 giây cho mỗi thao tác
    wait = WebDriverWait(driver, 10)

    # Bước 1: Điều hướng trình duyệt đến trang tải tệp lên
    driver.get(UPLOAD_URL)

    # Bước 2: Chờ ô nhập liệu chọn tệp (input type="file") xuất hiện và sẵn sàng
    # Dùng Explicit Wait thay hoàn toàn cho time.sleep()
    file_input = wait.until(
        EC.presence_of_element_located((By.ID, "file-upload"))
    )

    # Bước 3: Truyền đường dẫn tệp vào ô input thông qua send_keys
    # Selenium tự động xử lý hộp thoại chọn tệp bằng cách gửi đường dẫn trực tiếp
    file_input.send_keys(file_path)

    # Bước 4: Định vị và nhấn nút "Upload" để gửi tệp lên máy chủ
    upload_button = driver.find_element(By.ID, "file-submit")
    upload_button.click()

    # Bước 5: Chờ trang kết quả xuất hiện - đợi tiêu đề thành công hiển thị
    # Explicit Wait đảm bảo script không tiến hành kiểm tra trước khi trang tải xong
    success_heading = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3"))
    )

    # Bước 6: Kiểm tra tiêu đề trang kết quả có chứa thông báo thành công
    assert "File Uploaded!" in success_heading.text, (
        f"Tiêu đề trang không đúng: '{success_heading.text}', "
        f"kỳ vọng chứa 'File Uploaded!'"
    )

    # Bước 7: Định vị phần tử hiển thị tên tệp đã được tải lên
    uploaded_filename_el = wait.until(
        EC.visibility_of_element_located((By.ID, "uploaded-files"))
    )

    # Bước 8: Lấy tên tệp thực tế được hiển thị trên trang kết quả
    actual_filename = uploaded_filename_el.text.strip()

    # Bước 9: Xác nhận tên tệp hiển thị khớp với tên tệp đã tải lên
    expected_filename = test_file.name
    assert actual_filename == expected_filename, (
        f"Tên tệp không khớp: nhận được '{actual_filename}', "
        f"kỳ vọng '{expected_filename}'"
    )

    print("\nTest PASSED: Tai tep len thanh cong!")
    print(f"   Tep da tai len     : {actual_filename}")
    print(f"   Thong bao ket qua  : {success_heading.text}")
