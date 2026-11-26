# Tuần 08: Test Report & Learning Notes

**Thành viên phụ trách:** Ngô Quyết Thắng
**Nhánh:** `t08-thang`

## 1. Documenting Failing and Flaky Tests (Để xử lý vào Tuần 9)

Quá trình chạy test suite với `pytest-html` ghi nhận kết quả như sau:

*   **`test_upload_invalid_file_fail_case` (Cố ý Fail): FAILED**
    *   **Nguyên nhân:** Web thiếu tính năng kiểm tra định dạng (Validation). Test case kỳ vọng hệ thống chặn file `.exe` và báo `Unsupported file format`, nhưng hệ thống lại hiển thị `File Uploaded!`.
    *   **Hướng xử lý Tuần 9:** Ghi nhận đây là một Bug của ứng dụng. Cần cập nhật lại kịch bản test hoặc report bug cho Dev.
*   **`test_upload_file_invalid` (Không đính kèm file): PASSED (nhưng chứa tiềm ẩn)**
    *   **Nguyên nhân:** Khi nhấn Upload mà không có file, server trả về lỗi `500 Internal Server Error`. Mặc dù test case PASS do bắt được chuỗi "Internal Server Error", nhưng việc server sập thay vì hiển thị thông báo UI (ví dụ: "Please select a file") là một lỗi UX/Backend nghiêm trọng.
    *   **Hướng xử lý Tuần 9:** Đưa case này vào danh sách Flaky/Bug cần refactor. Nên assert trạng thái HTTP thay vì chỉ check text trên UI.

## 2. Personal Learning Notes & Reading Answers

*   **Cách thức gom nhóm code:** Rút ra bài học về cách tối ưu hóa WebDriver. Thay vì mỗi test case tự khởi tạo và tắt trình duyệt gây tốn thời gian, việc sử dụng chung `@pytest.fixture` với thuộc tính `yield` giúp code sạch và chạy nhanh hơn.
*   **Cấu hình Pytest-HTML:** Việc sử dụng flag `--self-contained-html` rất hữu ích vì nó nhúng toàn bộ CSS/JS vào chung một file `report.html` duy nhất, giúp việc chia sẻ file báo cáo cho team dễ dàng mà không bị mất định dạng.
*   **Waits mechanisms:** Hiểu rõ hơn lý do tại sao cấm dùng `time.sleep()`. Thay vì bắt hệ thống phải chờ chết 5 giây, `WebDriverWait` (Explicit Wait) kết hợp với `expected_conditions` giúp kịch bản test chủ động đi tiếp ngay khi phần tử xuất hiện, giảm thiểu thời gian chạy test suite.

## 3. Lệnh cài đặt và tạo báo cáo
*   **Cài đặt thư viện bắt buộc: pip install pytest selenium pytest-html
*   **Chạy test suite và xuất báo cáo HTML:pytest tuan-08/test_upload.py --html=tuan-08/report.html --self-contained-html
# Ghi chú Tuần 8 - Kiểm thử chức năng Upload

### Thành viên:Lê Thị Nga - Kiểm thử tính năng Upload (/upload)

### Điều đã học
- Đã xây dựng kịch bản kiểm thử cố tình gây lỗi (Negative Testing) cho tính năng tải lên tệp tin (/upload) bằng cách không chọn tệp trước khi gửi form.
- Áp dụng thành thạo Explicit Wait (`WebDriverWait` và `expected_conditions`) để chờ phần tử UI sẵn sàng tương tác mà không cần dùng `time.sleep()`.

### Trả lời câu hỏi đọc tài liệu:
1. **Tại sao việc thực hiện Negative Test cho tính năng Upload lại quan trọng?**
   - Giúp đảm bảo hệ thống phản hồi chính xác khi người dùng quên đính kèm tệp hoặc gửi tệp không hợp lệ, tránh việc ứng dụng bị treo hoặc tràn bộ nhớ.

**Thành viên phụ trách:** Nguyễn Phúc Hưng
**Nhánh:** `t08-phuchung`

## 1. Kiến thức học được (Learning Notes)

- **Cách upload file bằng Selenium:** Thay vì click vào nút upload để mở hộp thoại của hệ điều hành (Selenium không tương tác được với OS dialog), ta dùng phương thức `.send_keys("đường_dẫn_tuyệt_đối")` truyền thẳng vào thẻ `<input type="file">`.
- **Explicit Wait:** Tiếp tục sử dụng `WebDriverWait` kết hợp `expected_conditions` để chờ thông báo lỗi render xong trên DOM, đảm bảo kịch bản không bị vỡ do mạng chậm. Tuyệt đối loại bỏ `time.sleep()`.

## 2. Kịch bản Fail case (Reading Answers)

- Để đáp ứng yêu cầu "The test result must be a failure", script được thiết kế theo dạng **Intentional Failure**.
- Hệ thống xử lý đúng khi chặn file `.txt` không hợp lệ và quăng ra thông báo lỗi. Tuy nhiên, hàm `assert` ở cuối được cố tình viết sai logic (kỳ vọng thông báo thành công). Điều này ép `pytest` trả về **FAILED** kèm theo dòng `AssertionError`, chứng minh script có khả năng bắt lỗi chính xác khi kết quả thực tế lệch với kỳ vọng.
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
