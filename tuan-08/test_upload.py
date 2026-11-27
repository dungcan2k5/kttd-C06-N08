import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # Tự bật headless trên Linux/Codespaces/CI khi không có màn hình GUI
    if os.name != "nt" and not os.getenv("DISPLAY"):
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
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
    
    # Bước 3: Chờ thông báo lỗi đặc trưng của trang sau submit hiển thị
    error_detail = wait.until(
        EC.visibility_of_element_located((By.ID, "upload-error"))
    )
    error_heading = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h3"))
    )

    # Bước 4: Xác nhận tiêu đề và chi tiết lỗi (Negative Test)
    assert "Internal Server Error" in error_heading.text, (
        f"Tiêu đề lỗi không đúng: '{error_heading.text}'"
    )
    assert "No file was chosen" in error_detail.text, (
        f"Nội dung lỗi không đúng: '{error_detail.text}'"
    )

@pytest.mark.xfail(
    reason="App bug: trang /upload khong kiem tra va chan dinh dang file .exe",
    strict=True,
)
def test_upload_invalid_file_fail_case(driver, tmp_path):
    """
    Test case (XFail): Kiểm thử upload file sai định dạng (.exe).
    - Dùng fixture `driver` (đã có teardown driver.quit()) và `tmp_path` để tránh rác ở thư mục gốc.
    - Sử dụng Explicit Wait (WebDriverWait + expected_conditions), không dùng time.sleep().
    - Kỳ vọng hệ thống chặn file .exe, nhưng thực tế web vẫn báo "File Uploaded!" (App Bug),
      nên gắn @pytest.mark.xfail(strict=True) để bộ test 3x chạy sạch mà vẫn ghi nhận lỗi.
    """
    # Bước 1: Tạo file giả lập định dạng .exe trong thư mục tạm tmp_path của pytest
    invalid_file = tmp_path / "virus_gia.exe"
    invalid_file.write_text("Day la file exe dung de test invalid input.", encoding="utf-8")

    # Bước 2: Khởi tạo Explicit Wait (chờ tối đa 10 giây, đồng bộ toàn bộ suite)
    wait = WebDriverWait(driver, 10)

    # Bước 3: Điều hướng đến trang Upload
    driver.get(UPLOAD_URL)

    # Bước 4: Chờ thẻ input file xuất hiện và nút submit sẵn sàng để click
    file_input = wait.until(
        EC.presence_of_element_located((By.ID, "file-upload"))
    )
    upload_button = wait.until(
        EC.element_to_be_clickable((By.ID, "file-submit"))
    )

    # Bước 5: Truyền đường dẫn file .exe vào input rồi bấm Upload
    file_input.send_keys(str(invalid_file))
    upload_button.click()

    # Bước 6: Chờ tiêu đề kết quả hiển thị trên giao diện
    result_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3"))
    )

    # Bước 7: Kiểm tra kỳ vọng (web phải chặn và báo lỗi thay vì cho upload thành công)
    assert result_message.text.strip() == "Unsupported file format", (
        f"LỖI ỨNG DỤNG: Đưa vào file .exe nhưng web không chặn, "
        f"lại báo '{result_message.text.strip()}'"
    )
    

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
    upload_button = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))
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

@pytest.mark.xfail(reason="App bug: /upload khong chan tep rong 0 byte", strict=True) 
def test_upload_empty_file(driver, tmp_path):
    """
    Negative/Edge case: Kiểm thử tải lên tệp rỗng (0 byte).
    Mục tiêu: Xác nhận hệ thống xử lý và không chấp nhận tệp không có nội dung.
    """
    # Bước 1: Tạo tệp rỗng 0 byte trong thư mục tạm tmp_path
    empty_file = tmp_path / "empty_file.txt"
    empty_file.write_bytes(b"")
    assert empty_file.stat().st_size == 0

    wait = WebDriverWait(driver, 10)

    # Bước 2: Mở trang upload
    driver.get(UPLOAD_URL)

    # Bước 3: Chờ ô chọn tệp xuất hiện và truyền đường dẫn tệp rỗng
    file_input = wait.until(
        EC.presence_of_element_located((By.ID, "file-upload"))
    )
    file_input.send_keys(str(empty_file))

    # Bước 4: Chờ nút Upload sẵn sàng để click và gửi form
    upload_button = wait.until(
        EC.element_to_be_clickable((By.ID, "file-submit"))
    )
    upload_button.click()

    # Bước 5: Chờ tiêu đề kết quả hiển thị trên giao diện (h3 hoặc h1 nếu lỗi server)
    result_heading = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3, h1"))
    )
    heading_text = result_heading.text.strip()

    # Bước 6: Kiểm tra hệ thống từ chối tệp rỗng (không báo thành công)
    assert "File Uploaded!" not in heading_text, (
        f"LỖI: Hệ thống vẫn cho phép tải lên tệp rỗng 0 byte ('{heading_text}')"
    )