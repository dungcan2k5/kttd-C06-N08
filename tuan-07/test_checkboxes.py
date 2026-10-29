import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkboxes_fail_case():
    """
    Test case (Fail): Kiểm tra tính năng Checkboxes.
    Sử dụng Explicit Wait để chờ phần tử, tuyệt đối không dùng time.sleep().
    Kết quả: Bắt buộc FAILED do cố tình assert sai trạng thái của checkbox.
    """
    # Bước 1: Khởi tạo trình duyệt
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    # Khởi tạo Explicit Wait (đợi tối đa 5 giây)
    wait = WebDriverWait(driver, 5)

    try:
        # Bước 2: Điều hướng đến trang test Checkboxes
        driver.get("https://the-internet.herokuapp.com/checkboxes")

        # Bước 3: Đợi Checkbox 1 tải lên và có thể tương tác bằng Explicit Wait
        # Sử dụng XPath để trỏ chính xác vào ô checkbox đầu tiên
        checkbox_1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//form[@id='checkboxes']/input[1]")))

        # Bước 4: Thực hiện hành động click (Checkbox 1 mặc định chưa chọn, click xong sẽ thành đã chọn)
        checkbox_1.click()

        # Bước 5: Cố tình Assert sai để đảm bảo test FAILED theo yêu cầu Week 7
        # checkbox_1.is_selected() lúc này trả về True, nhưng ta thêm 'not' để kỳ vọng False
        assert not checkbox_1.is_selected(), "LỖI CỐ TÌNH: Checkbox 1 đã được chọn thành công, nhưng test kỳ vọng là chưa chọn!"

    finally:
        # Bước 6: Đóng trình duyệt
        driver.quit()