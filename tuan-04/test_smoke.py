from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def test_the_internet_title():
    # 1. Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()
    
    try:
        # 2. Điều hướng tới trang web thực hành
        driver.get("https://the-internet.herokuapp.com/")
        
        # Maximize (phóng to) cửa sổ để load đầy đủ giao diện
        driver.maximize_window()
        
        # 3. Lấy title của trang hiện tại (Đọc tiêu đề trang web)
        actual_title = driver.title
        # Đây là tiêu đề mình kỳ vọng (đã sửa lại thành đúng để test pass)
        expected_title = "The Internet"
        
        # 4. Kiểm tra tiêu đề trang có khớp với mong đợi không
        # Nếu không bằng thì quăng lỗi ra màn hình
        assert actual_title == expected_title, f"Sai title rồi: nhận '{actual_title}' nhưng mong đợi '{expected_title}'"
        print("\nSmoke test PASSED: Tiêu đề trang khớp hoàn toàn.")
        
    finally:
        # 5. Đóng trình duyệt sau khi test xong để giải phóng tài nguyên
        driver.quit()

if __name__ == "__main__":
    test_the_internet_title()