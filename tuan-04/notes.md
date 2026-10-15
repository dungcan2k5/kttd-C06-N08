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