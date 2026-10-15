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

**### Điều đã học**
- Đã làm quen với Selenium WebDriver bằng Python và chạy bài kiểm thử tự động cơ bản trên trình duyệt Chrome.
- Biết sử dụng `webdriver.Chrome()` để khởi tạo trình duyệt và `driver.get()` để truy cập trang web cần kiểm thử.
- Hiểu cách lấy tiêu đề trang bằng `driver.title` và sử dụng biến để lưu kết quả thực tế.
- Biết sử dụng câu lệnh `assert` để so sánh kết quả thực tế với kết quả mong đợi. Nếu hai giá trị không bằng nhau, chương trình sẽ phát sinh `AssertionError`.
- Hiểu vai trò của khối `try...finally` và `driver.quit()` trong việc đảm bảo trình duyệt được đóng khi kết thúc bài kiểm thử, kể cả khi xảy ra lỗi.

### Trả lời câu hỏi đọc tài liệu:**

1. Một script Selenium gồm những bước nào?\*\***
   - Khởi tạo WebDriver bằng `webdriver.Chrome()` để điều khiển trình duyệt.
   - Mở URL đích bằng `driver.get("https://the-internet.herokuapp.com/")`.
   - Lấy thông tin cần kiểm tra bằng `driver.title` và lưu vào biến `title_page`.
   - Khai báo kết quả mong đợi bằng biến `true_title = "The Internet"`.
   - Sử dụng `assert title_page == true_title` để xác nhận tiêu đề thực tế có đúng với tiêu đề mong đợi hay không.
   - In thông báo `TEST PASSED` nếu điều kiện kiểm thử đúng.
   - Sử dụng `driver.quit()` để đóng phiên WebDriver sau khi hoàn thành.

2 .pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?\*\***
   - File kiểm thử mặc định thường có tiền tố `test_`, ví dụ `test_smoke.py`, hoặc hậu tố `_test.py`, ví dụ `smoke_test.py`.
   - Hàm kiểm thử thông thường có tên bắt đầu bằng `test_`, ví dụ `test_smoke()`.
   - pytest dựa vào các quy tắc khám phá bài kiểm thử để tự động tìm và thực thi những bài kiểm thử phù hợp.

### Ghi chú sử dụng AI**
- Câu hỏi đã hỏi AI: Giải thích chức năng của `driver.title`, `assert`, `try...finally` và `driver.quit()` trong script Selenium.
- Tóm tắt câu trả lời: `driver.title` lấy tiêu đề trang hiện tại; `assert` kiểm tra điều kiện mong đợi; `finally` đảm bảo đoạn lệnh dọn dẹp được thực hiện khi rời khỏi khối `try`; `driver.quit()` đóng toàn bộ phiên WebDriver.
- Đánh giá câu trả lời: Nội dung phù hợp với cách sử dụng các thành phần trong đoạn code. Có thể kiểm tra lại bằng cách chạy chương trình và thay đổi giá trị tiêu đề mong đợi để quan sát kết quả.
- Điều hiểu thêm: Một bài kiểm thử không chỉ cần thực hiện thao tác trên trình duyệt mà còn phải có điều kiện kiểm tra rõ ràng để xác định kết quả đạt hay không đạt.

---

## Nguyễn Phúc Hưng

### Điều đã học
- Đã tìm hiểu cách viết một bài kiểm thử tự động đơn giản bằng Python.
- Biết cách khởi tạo trình duyệt Chrome, truy cập một trang web và lấy thông tin tiêu đề trang bằng Selenium.
- Hiểu rằng bài kiểm thử tự động cần có bước kiểm tra kết quả, thay vì chỉ mở trình duyệt và quan sát bằng mắt.

### Trả lời câu hỏi đọc tài liệu

1. **Một script Selenium gồm những bước nào?**
   - Import thư viện Selenium cần thiết.
   - Khởi tạo trình duyệt bằng `webdriver.Chrome()`.
   - Mở trang web bằng `driver.get()`.
   - Thực hiện thao tác hoặc lấy dữ liệu cần kiểm tra.
   - So sánh kết quả thực tế với kết quả mong đợi bằng câu lệnh `assert`.
   - Đóng trình duyệt bằng `driver.quit()`.

2. **pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?**
   - File kiểm thử có thể có tên dạng `test_*.py` hoặc `*_test.py`.
   - Các hàm kiểm thử thông thường bắt đầu bằng `test_`.
   - pytest dựa vào quy tắc khám phá bài kiểm thử để xác định những file và hàm cần chạy.

### Ghi chú sử dụng AI
- Câu hỏi đã hỏi AI: Tại sao một script Selenium mở được trang web nhưng chưa thể khẳng định bài kiểm thử đã thành công?
- Tóm tắt câu trả lời: Việc mở trang web chỉ chứng minh trình duyệt đã được điều khiển. Muốn kiểm thử một điều kiện cụ thể, cần kiểm tra kết quả bằng các khẳng định như `assert`.
- Đánh giá câu trả lời: Hợp lý vì thao tác mở trang không tự xác nhận rằng nội dung trang đúng như mong đợi.
- Điều hiểu thêm: Có thể kiểm tra tiêu đề trang bằng `assert driver.title == "The Internet"` nếu tiêu đề mong đợi của trang là `The Internet`.

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
