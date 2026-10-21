
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Lưu ảnh bằng chứng với tên riêng, tránh ghi đè ảnh của thành viên khác
SCREENSHOT_PATH = os.path.join(
    os.path.dirname(__file__), "anh", "hwng.png"
)

# URL trang đăng nhập dùng để kiểm thử
LOGIN_URL = "https://the-internet.herokuapp.com/login"

# Tài khoản không tồn tại và mật khẩu bất kỳ để kiểm tra đăng nhập thất bại
USERNAME = "this_user_does_not_exist_123"
PASSWORD = "AnyRandomPassword123!"


def test_login_invalid_username():
    """
    Kiểm thử đăng nhập thất bại khi username không tồn tại.
    Mục tiêu: Xác nhận hệ thống hiển thị thông báo lỗi theo yêu cầu.
    """

    # Khởi tạo Chrome để thực hiện kiểm thử giao diện đăng nhập
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Chờ tối đa 10 giây để các phần tử cần kiểm thử xuất hiện
    wait = WebDriverWait(driver, 10)

    try:
        # Mở trang đăng nhập cần kiểm thử
        driver.get(LOGIN_URL)

        # Dùng ID 'username' để tìm ô nhập tên đăng nhập
        username_field = wait.until(
            EC.visibility_of_element_located((By.ID, "username"))
        )

        # Dùng ID 'password' để tìm ô nhập mật khẩu
        password_field = driver.find_element(By.ID, "password")

        # Dùng CSS Selector để tìm nút gửi form đăng nhập
        login_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )

        # Nhập username không tồn tại
        username_field.send_keys(USERNAME)

        # Nhập mật khẩu bất kỳ
        password_field.send_keys(PASSWORD)

        # Nhấn nút Login để gửi thông tin đăng nhập
        login_button.click()

        # Chờ thông báo lỗi xuất hiện trên trang
        flash_message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        # Lấy nội dung thông báo lỗi để đối chiếu với yêu cầu
        actual_message = flash_message.text

        # Xác nhận thông báo chứa đúng nội dung lỗi được yêu cầu
        assert "Your username is invalid!" in actual_message, (
            f"Thông báo lỗi không đúng. Nội dung thực tế: "
            f"'{actual_message}'"
        )

        print("\nTest PASSED: Hệ thống từ chối username không hợp lệ.")
        print(f"Thông báo thực tế: {actual_message.strip()}")

        # Tạo thư mục lưu ảnh nếu thư mục chưa tồn tại
        os.makedirs(os.path.dirname(SCREENSHOT_PATH), exist_ok=True)

        # Chụp màn hình sau khi thông báo lỗi được hiển thị
        driver.save_screenshot(SCREENSHOT_PATH)
        print(f"Ảnh bằng chứng đã lưu: {SCREENSHOT_PATH}")

    finally:
        # Luôn đóng trình duyệt kể cả khi kiểm thử xảy ra lỗi
        driver.quit()


if __name__ == "__main__":
    test_login_invalid_username()
