# Ghi chú tuần 08 – Kiểm thử tự động tính năng Tải tệp lên (File Upload)

**Thành viên phụ trách:** Nguyễn Tiến Dũng
**Nhánh:** `t08-tiendung`

---

## Điều đã học

- Nắm vững cách kiểm thử tự động chức năng tải tệp lên (File Upload) bằng Selenium WebDriver trên trang `/upload` của `the-internet.herokuapp.com`.
- Hiểu được cách Selenium xử lý thẻ `<input type="file">` thông qua phương thức `send_keys()` với đường dẫn tệp đầy đủ, thay vì phải mô phỏng hộp thoại chọn tệp của hệ điều hành.
- Áp dụng thành thạo cơ chế **Explicit Wait** (`WebDriverWait`) để chờ trang kết quả tải xong trước khi thực hiện kiểm tra kết quả, tuyệt đối không dùng `time.sleep()`.
- Làm quen với fixture `tmp_path` của pytest để tạo tệp tạm thời trong test – một kỹ thuật chuyên nghiệp giúp test độc lập, không phụ thuộc vào file hệ thống cố định.

---

## Trả lời câu hỏi đọc tài liệu

### 1. Explicit Wait và Implicit Wait khác nhau như thế nào? Khi nào dùng loại nào?

- **Implicit Wait** là cơ chế chờ toàn cục, áp dụng cho tất cả lần tìm kiếm phần tử (`find_element`) trong suốt vòng đời của WebDriver. Khi khai báo `driver.implicitly_wait(10)`, mỗi lần WebDriver tìm không thấy phần tử ngay, nó sẽ tự động thử lại trong vòng tối đa 10 giây trước khi báo lỗi.

- **Explicit Wait** là cơ chế chờ có điều kiện, chỉ áp dụng cho một thao tác cụ thể tại một thời điểm cụ thể. Ví dụ: `WebDriverWait(driver, 10).until(EC.visibility_of_element_located(...))` – chờ đến khi phần tử cụ thể xuất hiện và nhìn thấy được, với thời gian tối đa là 10 giây.

- **Khi nào dùng loại nào:**
  - Dùng **Implicit Wait** khi toàn bộ trang web có thời gian phản hồi tương đối đồng đều và cần áp dụng thời gian chờ chung cho tất cả phần tử.
  - Dùng **Explicit Wait** (ưu tiên hơn) khi có các phần tử tải chậm bất thường hoặc tải bất đồng bộ (async), cần kiểm tra điều kiện cụ thể (xuất hiện, có thể click, URL thay đổi...) trước khi tiếp tục.
  - **Không nên kết hợp cả hai** (Implicit + Explicit) trong cùng một test vì có thể gây ra hành vi chờ không dự đoán được.

---

### 2. Tại sao nghiêm cấm dùng `time.sleep()` trong kiểm thử tự động chuyên nghiệp?

- **`time.sleep(n)`** bắt chương trình dừng hoàn toàn đúng `n` giây bất kể trang web đã tải xong hay chưa:
  - Nếu trang tải xong sau 1 giây nhưng `time.sleep(5)` vẫn bắt chờ thêm 4 giây → **lãng phí thời gian**.
  - Nếu mạng chậm hơn bình thường, `time.sleep(5)` không đủ → test **thất bại vô lý** (Flaky test).

- **Explicit Wait** thì ngược lại: chủ động kiểm tra điều kiện mỗi 500ms, và dừng chờ ngay khi điều kiện thỏa mãn → **nhanh hơn, ổn định hơn, chuyên nghiệp hơn**.

---

## Ghi chú sử dụng AI

- **Câu hỏi đã hỏi AI:** Làm thế nào để Selenium WebDriver tải tệp lên mà không cần mở hộp thoại chọn tệp của hệ điều hành?
- **Tóm tắt câu trả lời:** AI giải thích rằng thẻ `<input type="file">` trong HTML có thể nhận đường dẫn tệp trực tiếp thông qua phương thức `send_keys()`. Trình duyệt sẽ tự điền đường dẫn vào ô input mà không cần mở hộp thoại file picker của hệ điều hành, giúp tự động hóa hoàn toàn bước này.
- **Đánh giá câu trả lời:** Chính xác và thực tế. Phương pháp này là chuẩn mực trong ngành kiểm thử tự động với Selenium.
- **Điều hiểu thêm:** Chỉ có thể dùng `send_keys()` trực tiếp trên thẻ `input[type="file"]`. Nếu nút upload được tùy biến bằng CSS/JS ẩn thẻ input thật, cần dùng JavaScript executor để hiển thị lại trước khi gọi `send_keys()`.
