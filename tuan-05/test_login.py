from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Đường dẫn lưu ảnh chụp màn hình bằng chứng thực thi
SCREENSHOT_PATH = os.path.join(os.path.dirname(__file__), "anh", "tdung.png")

# URL trang đăng nhập cần kiểm thử
LOGIN_URL = "https://the-internet.herokuapp.com/login"

# Thông tin đăng nhập hợp lệ (valid credentials)
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


def test_login_valid_credentials():
    """
    Kiểm thử đăng nhập thành công với thông tin hợp lệ.
    Mục tiêu: Xác nhận trang /login chấp nhận đúng tài khoản,
    chuyển hướng sang trang bảo mật và hiển thị thông báo thành công.
    """

    # 1. Khởi tạo trình duyệt Chrome và mở tối đa cửa sổ
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Đối tượng chờ tường minh: tối đa 10 giây cho mỗi điều kiện
    wait = WebDriverWait(driver, 10)

    try:
        # 2. Điều hướng trình duyệt đến trang đăng nhập
        driver.get(LOGIN_URL)

        # 3. Định vị trường nhập tên đăng nhập bằng thuộc tính ID
        username_field = wait.until(
            EC.visibility_of_element_located((By.ID, "username"))
        )

        # 4. Định vị trường nhập mật khẩu bằng thuộc tính ID
        password_field = driver.find_element(By.ID, "password")

        # 5. Định vị nút "Login" bằng CSS Selector (button kiểu submit)
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # 6. Nhập tên đăng nhập hợp lệ vào trường username
        username_field.send_keys(USERNAME)

        # 7. Nhập mật khẩu hợp lệ vào trường password
        password_field.send_keys(PASSWORD)

        # 8. Nhấn nút đăng nhập để gửi form
        login_button.click()

        # 9. Chờ cho đến khi URL thay đổi sang trang bảo mật sau đăng nhập
        wait.until(EC.url_contains("/secure"))

        # 10. Kiểm tra chuyển hướng: URL hiện tại phải chứa "/secure"
        actual_url = driver.current_url
        assert "/secure" in actual_url, (
            f"Chuyển hướng thất bại: URL hiện tại là '{actual_url}', "
            f"kỳ vọng chứa '/secure'"
        )

        # 11. Định vị thông báo flash message thành công
        flash_message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        # 12. Lấy nội dung văn bản của thông báo flash
        flash_text = flash_message.text

        # 13. Kiểm tra thông báo hiển thị đúng nội dung đăng nhập thành công
        assert "You logged into a secure area!" in flash_text, (
            f"Flash message không đúng: '{flash_text}'"
        )

        print("\n✅ Test PASSED: Đăng nhập thành công!")
        print(f"   URL sau đăng nhập : {actual_url}")
        print(f"   Flash message      : {flash_text.strip()}")

        # 14. Chụp ảnh màn hình làm bằng chứng thực thi và lưu vào tuan-05/anh/
        os.makedirs(os.path.dirname(SCREENSHOT_PATH), exist_ok=True)
        driver.save_screenshot(SCREENSHOT_PATH)
        print(f"   Screenshot đã lưu  : {SCREENSHOT_PATH}")

    finally:
        # 15. Đóng trình duyệt và giải phóng tài nguyên dù test pass hay fail
        driver.quit()


def test_login_invalid_password():
    """
    Kiểm thử đăng nhập thất bại với mật khẩu sai.
    Mục tiêu: Đảm bảo hệ thống từ chối mật khẩu không đúng và hiển thị
    thông báo lỗi "Your password is invalid!".
    """
    
    # Đường dẫn lưu ảnh chụp màn hình riêng của bạn
    # Sẽ lưu thành tuan-05/anh/thang.png
    thang_screenshot_path = os.path.join(os.path.dirname(__file__), "anh", "thang.png")
    
    # Khởi tạo trình duyệt
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(LOGIN_URL)

        # 1. Định vị các phần tử bằng chiến lược Locator
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # 2. Nhập dữ liệu (Username đúng, Password sai)
        username_field.send_keys(USERNAME)
        password_field.send_keys("WrongPassword123!")

        # 3. Kích hoạt hành động đăng nhập
        login_button.click()

        # 4. Chờ và định vị thông báo lỗi flash hiển thị (chứng tỏ đăng nhập bị từ chối)
        error_message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        error_text = error_message.text

        # 5. Assertion: Kiểm tra thông báo lỗi có chứa đoạn text mong đợi hay không
        # Dùng toán tử 'in' vì thẻ flash thường chứa cả nút 'x' đóng thông báo
        assert "Your password is invalid!" in error_text, (
            f"Kỳ vọng thấy lỗi 'Your password is invalid!' nhưng nhận được: '{error_text}'"
        )

        print("\n✅ Test PASSED: Đăng nhập thất bại hợp lệ (Bắt đúng thông báo lỗi mật khẩu)!")
        print(f"   Error message hiện ra: {error_text.strip()}")

        # 6. Lưu bằng chứng thực thi
        os.makedirs(os.path.dirname(thang_screenshot_path), exist_ok=True)
        driver.save_screenshot(thang_screenshot_path)
        print(f"   Screenshot đã lưu    : {thang_screenshot_path}")

    finally:
        # driver.quit()
        pass

# Cập nhật lại phần chạy file
if __name__ == "__main__":
    print("--- CHẠY TEST CASE 1: ĐĂNG NHẬP THÀNH CÔNG ---")
    test_login_valid_credentials()
    
    print("\n--- CHẠY TEST CASE 2: SAI MẬT KHẨU ---")
    test_login_invalid_password()
