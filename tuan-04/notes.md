# Ghi chú tuần 04

## Phùng Dũng

### Điều đã học
- Đã cài đặt và làm quen với Selenium WebDriver, chạy test case cơ bản trên Chrome.
- Nắm được cách vận hành của pytest để gom và thực thi các bài kiểm thử tự động.

### Trả lời câu hỏi đọc tài liệu:
1. **Một script Selenium gồm những bước nào?**
   - Khởi tạo WebDriver (trình duyệt).
   - Mở URL đích (`driver.get`).
   - Tương tác hoặc truy xuất dữ liệu từ phần tử/trang (`driver.title`, `find_element`).
   - Kiểm tra kết quả thực tế với mong đợi (Assert).
   - Đóng phiên làm việc của WebDriver (`driver.quit`).
2. **pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?**
   - File có tiền tố `test_*.py` hoặc hậu tố `*_test.py`.
   - Hàm test bắt đầu bằng `test_*`.

---

## Nguyễn Phúc Hưng

### Điều đã học
- Hiểu được cấu trúc 5 bước cơ bản của một kịch bản kiểm thử Selenium.
- Biết cách tìm và xác định lỗi sai cố ý trong đoạn code kiểm thử để sửa lại cho đúng.
- Nắm được quy trình đẩy code lên GitHub qua Pull Request bằng nhánh phụ (branch) để làm việc nhóm.

### Trả lời câu hỏi đọc tài liệu:
1. **Một script Selenium gồm những bước nào?**
   - Bước 1: Khởi tạo trình duyệt (`driver = webdriver.Chrome()`).
   - Bước 2: Điều hướng URL trang web (`driver.get(...)`).
   - Bước 3: Tìm phần tử và lấy dữ liệu trên trang (`driver.title`, `find_element`).
   - Bước 4: Kiểm tra kết quả, so sánh thực tế với mong đợi (Assert).
   - Bước 5: Đóng phiên làm việc (`driver.quit()`).
2. **pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?**
   - Pytest tự động tìm và chạy các file kiểm thử có tên bắt đầu bằng `test_*.py` hoặc kết thúc bằng `*_test.py`.
   - Bên trong file, các hàm kiểm thử bắt buộc phải bắt đầu bằng tiền tố `test_` (ví dụ: `def test_the_internet_title():`).

### Việc sử dụng AI
- **Đã hỏi AI điều gì:** Hỏi cách sửa lỗi "The browser path is not a valid file" khi Selenium không tìm thấy Chrome trên ổ C và cách tạo Pull Request.
- **Hiểu thêm được gì:** Hiểu được cách cấu hình đường dẫn thủ công cho WebDriver khi trình duyệt không nằm ở vị trí mặc định và cách sử dụng quy trình Git chuẩn trong làm việc nhóm.
