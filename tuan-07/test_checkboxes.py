import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture
def driver():
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

def test_checkboxes_fail_case_invalid_action(driver):
    """
    Negative Case: Kiểm tra thao tác click đúp (2 lần) vào Checkbox 1.
    Mục tiêu: Xác nhận click 2 lần liên tiếp khiến checkbox được chọn rồi bị bỏ chọn lại.
    """
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkbox_1 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//form[@id='checkboxes']/input[1]"))
    )

    # Click 2 lần liên tiếp (bật rồi tắt)
    checkbox_1.click()
    checkbox_1.click()

    # Sau 2 lần click, checkbox quay về trạng thái chưa chọn (False)
    assert not checkbox_1.is_selected(), (
        "Lỗi: Checkbox 1 vẫn đang được chọn sau khi click 2 lần"
    )

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

def test_checkbox_not_persisted_after_refresh(driver):
    """
    TC03 (Negative Case): Trạng thái checkbox không được lưu sau khi tải lại trang.
    Mục tiêu: Xác nhận khi người dùng đổi trạng thái checkbox rồi refresh (F5),
    trang quay về trạng thái mặc định (checkbox 1: unchecked, checkbox 2: checked).
    """
    wait = WebDriverWait(driver, 10)
    checkboxes_locator = (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    # Bước 1: Mở trang Checkboxes và chờ cả 2 checkbox hiển thị trên giao diện
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = wait.until(EC.visibility_of_all_elements_located(checkboxes_locator))
    checkbox_1, checkbox_2 = checkboxes[0], checkboxes[1]

    # Bước 2: Xác nhận trạng thái mặc định ban đầu
    assert not checkbox_1.is_selected(), "Checkbox 1 mặc định phải chưa được chọn"
    assert checkbox_2.is_selected(), "Checkbox 2 mặc định phải đang được chọn"

    # Bước 3: Đổi trạng thái cả 2 checkbox và kiểm tra đã thay đổi thành công
    wait.until(EC.element_to_be_clickable(checkbox_1)).click()
    wait.until(EC.element_to_be_clickable(checkbox_2)).click()
    assert checkbox_1.is_selected(), "Checkbox 1 phải chuyển sang đã chọn sau khi click"
    assert not checkbox_2.is_selected(), "Checkbox 2 phải chuyển sang bỏ chọn sau khi click"

    # Bước 4: Tải lại trang (Refresh) và tìm lại phần tử mới để tránh StaleElementReferenceException
    driver.refresh()
    refreshed_checkboxes = wait.until(EC.visibility_of_all_elements_located(checkboxes_locator))
    checkbox_1_after, checkbox_2_after = refreshed_checkboxes[0], refreshed_checkboxes[1]

    # Bước 5: Kiểm tra trạng thái quay về mặc định (không lưu persistence)
    assert not checkbox_1_after.is_selected(), (
        "Lỗi: Checkbox 1 vẫn giữ trạng thái đã chọn sau khi refresh trang"
    )
    assert checkbox_2_after.is_selected(), (
        "Lỗi: Checkbox 2 không quay về trạng thái mặc định sau khi refresh trang"
    )