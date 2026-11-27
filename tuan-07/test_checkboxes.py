import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Đóng trình duyệt sau khi test xong
    driver.quit()

def test_checkboxes_fail_case_invalid_action(driver):
    """
    Test case (Fail): Kiểm tra tính năng Checkboxes.
    Sử dụng Explicit Wait để chờ phần tử, tuyệt đối không dùng time.sleep().
    Kết quả: FAILED do thao tác sai (người dùng click đúp) làm sai lệch trạng thái.
    """
    # Khởi tạo Explicit Wait (đợi tối đa 5 giây)
    wait = WebDriverWait(driver, 5)

    # Bước 1: Điều hướng đến trang test Checkboxes
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # Bước 2: Đợi Checkbox 1 tải lên và có thể tương tác bằng Explicit Wait
    checkbox_1 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//form[@id='checkboxes']/input[1]"))
    )

    # Bước 3: THAO TÁC SAI (Invalid input/action)
    # Cố tình click 2 lần (double-click) khiến checkbox được chọn rồi lại bị bỏ chọn
    checkbox_1.click()
    checkbox_1.click()

    # Bước 4: Kiểm tra trạng thái
    # Test sẽ FAILED ngay tại đây vì kỳ vọng là True nhưng thực tế là False
    assert not checkbox_1.is_selected(), "Checkbox 1 phải trở về trạng thái chưa chọn sau khi click 2 lần!"

def test_checkbox_happy_path(driver):
    # 1. Truy cập trang web
    url = "https://the-internet.herokuapp.com/checkboxes"
    driver.get(url)

    # 2. Khai báo Explicit Wait (Chờ tối đa 10 giây)
    wait = WebDriverWait(driver, 10)

    # 3. Chờ cho đến khi các checkbox xuất hiện trên DOM
    # Thay thế hoàn toàn cho time.sleep(). Script sẽ chạy tiếp ngay khi element sẵn sàng.
    checkboxes = wait.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']"))
    )
    
    checkbox_1 = checkboxes[0]
    checkbox_2 = checkboxes[1]

    # 4. Kiểm tra trạng thái mặc định trước khi thao tác
    assert not checkbox_1.is_selected(), "Lỗi: Checkbox 1 mặc định phải ở trạng thái chưa chọn"
    assert checkbox_2.is_selected(), "Lỗi: Checkbox 2 mặc định phải ở trạng thái đã chọn"
    # 5. Thực hiện thao tác: Click để đảo ngược trạng thái
    checkbox_1.click()
    checkbox_2.click()

    # 6. Kiểm tra lại trạng thái sau khi click (Happy Path)
    assert checkbox_1.is_selected(), "Lỗi: Checkbox 1 thao tác click không thành công"
    assert not checkbox_2.is_selected(), "Lỗi: Checkbox 2 thao tác bỏ click không thành công"