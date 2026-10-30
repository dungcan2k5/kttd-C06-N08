def test_checkbox_happy_path(driver):
    # 1. Truy cập trang web
    url = "https://the-internet.herokuapp.com/checkboxes"
    driver.get(url)

    # 2. Khai báo Explicit Wait (Chờ tối đa 10 giây)
    wait = WebDriverWait(driver, 10)

    # 3. Chờ cho đến khi các checkbox xuất hiện trên DOM
    # Thay thế hoàn toàn cho time.sleep(). Script sẽ chạy tiếp ngay khi element sẵn sàng.
    checkboxes = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']"))
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