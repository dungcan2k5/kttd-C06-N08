import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_login_fail_case():
    """
    Test case: Nhập sai mật khẩu nhưng cố tình chờ trang Dashboard tải.
    Kết quả mong đợi cho Week 7: Test phải trả về trạng thái FAILED.
    """
    # Bước 1: Khởi tạo trình duyệt
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    # Khởi tạo Explicit Wait (đợi tối đa 5 giây cho mỗi thao tác)
    wait = WebDriverWait(driver, 5)

    try:
        # Bước 2: Điều hướng đến trang Đăng nhập (thay bằng URL thực tế của bạn)
        driver.get("https://localhost:3000/login")

        # Bước 3: Đợi các phần tử input tải xong bằng Explicit Wait (Tuyệt đối không dùng time.sleep)
        email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
        password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "btn-login")))

        # Bước 4: Cố tình nhập dữ liệu không hợp lệ (sai mật khẩu)
        email_input.send_keys("admin@smartclinic.com")
        password_input.send_keys("wrong_password_123")

        # Bước 5: Thực hiện click đăng nhập
        submit_button.click()

        # Bước 6: Cố tình đợi trang chuyển hướng đến Dashboard. 
        # Vì mật khẩu sai, hệ thống sẽ hiện thông báo lỗi chứ không tải Dashboard.
        # Hàm wait này sẽ văng ra lỗi TimeoutException sau 5 giây -> Làm test thất bại (Fail)
        dashboard_header = wait.until(EC.presence_of_element_located((By.ID, "dashboard-header")))
        
        # Câu lệnh assert này đặt để đảm bảo nếu somehow web lỗi mà cho qua thì test vẫn sẽ fail
        assert dashboard_header.is_displayed(), "Lỗi: Đăng nhập thành công với sai mật khẩu!"

    finally:
        # Bước 7: Dọn dẹp, đóng trình duyệt
        driver.quit()