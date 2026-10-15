# Ghi chú tuần 04

## Phùng Mạnh Dũng

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
## Ngô Quyết Thắng

### Điều đã học
- Hiểu được cấu trúc 5 bước cơ bản của một kịch bản kiểm thử Selenium.
- Biết cách tìm và xác định lỗi sai cố ý trong đoạn code kiểm thử để sửa lại cho đúng.
- Nắm được quy trình đẩy code lên GitHub qua Pull Request bằng nhánh phụ (branch) để làm việc nhóm.
### Trả lời câu hỏi đọc tài liệu:
Một script Selenium gồm những bước nào?

 - Bước 1: Khởi tạo trình duyệt (ví dụ: driver = webdriver.Chrome()).
 - Bước 2: Điều hướng URL trang web (ví dụ: driver.get("link_trang_web")).
 - Bước 3: Tìm phần tử và lấy dữ liệu trên trang (ví dụ: driver.title).
 - Bước 4: Kiểm tra kết quả, so sánh thực tế với mong đợi (Assert).
 - Bước 5: Đóng trình duyệt (Teardown) bằng driver.quit().
### Việc sử dụng AI
Đã hỏi AI điều gì: Hỏi cách sửa lỗi "The browser path is not a valid file" khi Selenium không tìm thấy Chrome trên ổ C và cách tạo Pull Request.
Hiểu thêm được gì: Hiểu được cách cấu hình đường dẫn thủ công cho WebDriver khi trình duyệt không nằm ở vị trí mặc định và cách sử dụng quy trình Git chuẩn trong làm việc nhóm.

---

## Lê Thị Nga

### Điều đã học
- Đã tìm hiểu quy trình chạy kiểm thử tự động trên trình duyệt bằng Selenium WebDriver.
- Biết rằng WebDriver cần được khởi tạo trước khi thực hiện các thao tác trên trình duyệt.
- Hiểu được tầm quan trọng của việc đóng trình duyệt sau khi kiểm thử để tránh để lại tiến trình không cần thiết.

### Trả lời câu hỏi đọc tài liệu

1. **Một script Selenium gồm những bước nào?**
   - Khởi tạo WebDriver.
   - Truy cập URL cần kiểm thử.
   - Tìm phần tử hoặc lấy thông tin cần thiết từ trang web.
   - Kiểm tra kết quả bằng điều kiện hoặc câu lệnh `assert`.
   - Đóng phiên WebDriver bằng `driver.quit()`.

2. **pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?**
   - pytest mặc định nhận diện các file như `test_*.py` và `*_test.py`.
   - Các hàm kiểm thử thường có tên bắt đầu bằng `test_`.
   - Nếu đặt tên không đúng quy tắc, bài kiểm thử có thể không được pytest tự động phát hiện theo cấu hình mặc định.

### Ghi chú sử dụng AI
- Câu hỏi đã hỏi AI: Sự khác nhau giữa `driver.close()` và `driver.quit()` trong Selenium là gì?
- Tóm tắt câu trả lời: `driver.close()` đóng cửa sổ trình duyệt hiện tại; `driver.quit()` kết thúc phiên WebDriver và đóng tất cả cửa sổ trình duyệt thuộc phiên đó.
- Đánh giá câu trả lời: Phù hợp với cách sử dụng thông thường của Selenium.
- Điều hiểu thêm: Khi kết thúc một bài kiểm thử độc lập, `driver.quit()` thường phù hợp hơn vì giúp kết thúc toàn bộ phiên WebDriver.

---

## Nguyễn Tiến Dũng

### Điều đã học
- Đã tìm hiểu cách sử dụng pytest để tổ chức và chạy các bài kiểm thử Python.
- Hiểu rằng việc đặt tên file và hàm theo quy ước giúp công cụ tự động tìm ra các bài kiểm thử.
- Biết rằng kết quả chạy kiểm thử có thể cho biết bài kiểm thử đạt hay thất bại, từ đó hỗ trợ phát hiện lỗi.

### Trả lời câu hỏi đọc tài liệu

1. **Một script Selenium gồm những bước nào?**
   - Tạo đối tượng WebDriver để điều khiển trình duyệt.
   - Mở trang web cần kiểm thử.
   - Thực hiện các thao tác hoặc lấy thông tin từ trang.
   - Dùng điều kiện kiểm tra để xác định kết quả có đúng mong đợi không.
   - Đóng trình duyệt sau khi hoàn thành.

2. **pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?**
   - Tên file mặc định thường theo dạng `test_*.py` hoặc `*_test.py`.
   - Tên hàm kiểm thử thường bắt đầu bằng `test_`.
   - Các quy tắc này có thể được điều chỉnh trong cấu hình pytest, nhưng nên tuân theo mặc định khi mới bắt đầu.

### Ghi chú sử dụng AI
- Câu hỏi đã hỏi AI: Làm thế nào để chạy một file kiểm thử Python bằng pytest?
- Tóm tắt câu trả lời: Cài đặt pytest bằng `pip install pytest`, mở Terminal tại thư mục chứa bài kiểm thử và chạy lệnh `pytest` hoặc `python -m pytest`.
- Đánh giá câu trả lời: Đây là cách chạy cơ bản; cần bảo đảm đang sử dụng đúng môi trường Python đã cài đặt pytest.
- Điều hiểu thêm: Nếu muốn pytest hiển thị chi tiết từng bài kiểm thử, có thể dùng `pytest -v`. Nếu bài kiểm thử không được phát hiện, cần kiểm tra tên file, tên hàm và thư mục đang chạy lệnh.
