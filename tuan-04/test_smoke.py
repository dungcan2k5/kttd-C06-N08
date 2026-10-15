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
        
        # Maximize cửa sổ để load đầy đủ giao diện
        driver.maximize_window()
        
        # 3. Lấy title của trang hiện tại
        actual_title = driver.title
        expected_title = "The Internet"
        
        # 4. Kiểm tra tiêu đề trang có khớp với mong đợi không
        assert actual_title == expected_title, f"Title mismatch: got '{actual_title}' but expected '{expected_title}'"
        print("\nSmoke test PASSED: Title matched.")
        
    finally:
        # 5. Đóng trình duyệt sau khi test xong để giải phóng tài nguyên
        driver.quit()

if __name__ == "__main__":
    test_the_internet_title()