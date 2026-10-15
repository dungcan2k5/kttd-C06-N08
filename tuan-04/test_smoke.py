
from selenium import webdriver

def test_title_internet():
    # Khởi tạo trình duyệt Chrome bằng Selenium WebDriver.
    # Biến driver được dùng để điều khiển trình duyệt trong suốt bài kiểm thử.
    driver = webdriver.Chrome()

    try:
        # Mở trang web cần kiểm thử bằng URL được cung cấp.
        driver.get("https://the-internet.herokuapp.com/")

        # Lấy tiêu đề của trang web hiện tại.
        # Giá trị trả về được lưu vào biến title_page.
        title_page = driver.title

        # In tiêu đề thực tế ra Terminal để quan sát kết quả.
        print("Tiêu đề trang:", title_page)

        # Khai báo tiêu đề mong đợi của trang web.
        # Đây là giá trị dùng để so sánh với tiêu đề thực tế.
        true_title = "The Internet"

        # Kiểm tra tiêu đề thực tế có bằng tiêu đề mong đợi hay không.
        # Nếu điều kiện đúng, chương trình tiếp tục chạy.
        # Nếu điều kiện sai, AssertionError được phát sinh và thông báo
        # sẽ cho biết tiêu đề mong đợi và tiêu đề thực tế.
        assert title_page == true_title, (
            f"Tiêu đề sai! Mong đợi: '{true_title}', "
            f"Thực tế: '{title_page}'"
        )

        # Chỉ in TEST PASSED khi câu lệnh assert phía trên không thất bại.
        print("TEST PASSED")

    finally:
        # Luôn thực hiện khi rời khỏi khối try, kể cả khi có lỗi.
        # Đóng toàn bộ cửa sổ thuộc phiên WebDriver và giải phóng tài nguyên.
        driver.quit()


if __name__ == "__main__":
    test_title_internet()
