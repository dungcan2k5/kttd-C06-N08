# Ghi chú tuần 09 – Tổng hợp kiến thức, khắc phục lỗi Tuần 7–8 & Chuẩn bị Demo Vòng 2

**Nhóm:** C06-N08  
**Nhánh làm việc:** `t09-tiendung` (Issue `#64`)  
**Thành viên phụ trách tổng hợp:** Nguyễn Tiến Dũng

---

## 1. Ghi nhận học tập & Nhật ký sử dụng AI của 5 thành viên

### 1.1. Phùng Dũng – Nhóm trưởng _(Issue #60 – Ổn định bộ test, chạy 3x log & tích hợp nhánh `week-09`)_

#### Điều đã học

- Nắm vững quy trình kiểm soát chất lượng bộ kiểm thử trước buổi bảo vệ Vòng 2: khởi tạo nhánh `week-09`, rà soát đồng bộ các bộ test từ Tuần 5 đến Tuần 8 (`tuan-05/`, `tuan-07/`, `tuan-08/`) để bảo đảm toàn bộ script đều dùng `WebDriverWait` + `expected_conditions` và mỗi tính năng đều có cả ca kiểm thử hợp lệ (Positive) lẫn kiểm thử tiêu cực (Negative).
- Hiểu tầm quan trọng của việc thực thi lặp lại nhiều lần liên tiếp (**3x consecutive execution**) trên cùng một phiên làm việc để phát hiện sớm **flaky test** (lỗi lúc chạy pass, lúc chạy fail do mạng, thời gian tải DOM hoặc rò rỉ tài nguyên WebDriver).
- Thành thạo cách ghi nhận bằng chứng kiểm thử tập trung vào `tuan-09/run_log.md`, kiểm tra chéo và hợp nhất (merge) các Pull Request từ 5 thành viên vào `week-09` trước khi đưa vào `main`.

#### Ghi chú sử dụng AI

- **Câu hỏi đã hỏi AI:** Làm sao chạy toàn bộ bộ test `pytest` 3 lần liên tiếp trong một lệnh duy nhất trên PowerShell để kiểm tra flaky test và xuất log tổng hợp?
- **Tóm tắt câu trả lời:** AI hướng dẫn có thể dùng vòng lặp trong PowerShell (`1..3 | ForEach-Object { ... }`) hoặc cài plugin `pytest-repeat` (`pytest --count=3`) để chạy lặp tự động nhiều lần, kèm chuyển hướng kết quả ra tệp log để đối chiếu thời gian và trạng thái từng lượt chạy.
- **Đánh giá câu trả lời:** Chính xác, dễ áp dụng trực tiếp cho yêu cầu chạy 3x của nhóm mà không phải chạy thủ công rời rạc từng file.
- **Điều hiểu thêm:** Chạy lặp nhiều lần giúp phát hiện ngay các lỗi tiềm ẩn như tạo file tạm trùng tên trong thư mục gốc, quên `driver.quit()` hoặc trộn `implicitly_wait` với `WebDriverWait`.

---

### 1.2. Nguyễn Phúc Hưng _(Issue #63 – Debug & sửa flaky/failing tests Tuần 7–8)_

#### Điều đã học

- Học được cách đọc log lỗi (`tuan-08/report.html`) và truy vết nguyên nhân gốc rễ các bài test chạy không ổn định hoặc luôn fail trong `tuan-07/test_checkboxes.py` và `tuan-08/test_upload.py`.
- Hiểu rõ sự khác biệt giữa lỗi thực sự của ứng dụng web (Application Bug) với lỗi do cách viết script (Test Script Bug như: khai báo trùng fixture `driver`, tự khởi tạo `webdriver.Chrome()` rời rạc, trộn `implicitly_wait` với `WebDriverWait`, hoặc assert sai thông báo thực tế).
- Biết cách chuẩn hóa thao tác chờ từ `EC.presence_of_element_located` sang `EC.visibility_of_element_located` / `EC.element_to_be_clickable` và dùng fixture `tmp_path` thay cho file cứng tại thư mục làm việc.

#### Ghi chú sử dụng AI

- **Câu hỏi đã hỏi AI:** Vì sao hàm `test_upload_invalid_file_fail_case` tự tạo `webdriver.Chrome()` và tạo file `virus_gia.exe` bằng `os.path.abspath` dễ gây lỗi/rác khi chạy lặp lại nhiều lần, và nên sửa theo chuẩn pytest như thế nào?
- **Tóm tắt câu trả lời:** AI giải thích rằng tự khởi tạo `Chrome()` bên ngoài fixture sẽ không dùng chung được cấu hình test harness chuẩn của dự án (như headless, timeout, teardown), còn tạo file trực tiếp trong working directory dễ gặp xung đột hoặc để lại file rác nếu test dừng đột ngột. Giải pháp chuẩn là nhận cả `driver` và `tmp_path` từ pytest fixture.
- **Đánh giá câu trả lời:** Giải thích đúng bản chất vấn đề cô lập dữ liệu (test isolation) và phù hợp với cấu trúc mà nhóm đã áp dụng ở hàm `test_upload_valid_file`.
- **Điều hiểu thêm:** Không nên dùng `"chuỗi" in driver.page_source` để kiểm tra thông báo lỗi vì dễ bắt nhầm vào mã HTML/script ẩn; cần định vị đúng thẻ hiển thị (`h1`, `h3`, `#flash`) bằng `WebDriverWait`.

---

### 1.3. Nguyễn Tiến Dũng _(Issue #64 – Tổng hợp ghi chú, câu hỏi đọc tài liệu & Timekeeper diễn tập 12 phút)_

#### Điều đã học

- Nắm vững cách tổng hợp và đối chiếu thông tin kỹ thuật của cả nhóm: kiểm tra chéo mã nguồn thực tế (`tuan-07/test_checkboxes.py`, `tuan-08/test_upload.py`, `tuan-08/report.html`, `tuan-08/notes.md`) để lập bảng tổng hợp lỗi và nguyên nhân gốc rễ chính xác.
- Hiểu sâu hơn về nhóm điều kiện chờ `expected_conditions` (EC) trong Selenium, cách chạy Chrome ở chế độ **Headless mode** (`--headless=new`, `--window-size=1920,1080`) phục vụ CI/CD, và kiến trúc **Page Object Model (POM)** để tách biệt locator khỏi kịch bản kiểm thử.
- Rèn luyện kỹ năng điều phối buổi diễn tập (rehearsal) đúng khung thời lượng 12 phút và chuẩn bị bộ câu hỏi Mock Q&A sát với thực tế code của nhóm.

#### Ghi chú sử dụng AI

- **Câu hỏi đã hỏi AI:** Khi nhiều thành viên cùng gộp test vào một file như `tuan-08/test_upload.py`, những lỗi cấu trúc nào dễ xảy ra và mô hình Page Object Model giúp xử lý ra sao?
- **Tóm tắt câu trả lời:** AI chỉ ra việc định nghĩa trùng `@pytest.fixture def driver()` trong cùng file sẽ khiến fixture sau ghi đè fixture trước, việc trộn `implicitly_wait` với `WebDriverWait` dễ gây thời gian chờ khó đoán, và tự tạo `webdriver.Chrome()` rời rạc dễ gây rò rỉ tiến trình. Page Object Model giải quyết bằng cách gom locator và thao tác của từng trang vào một class riêng, còn file test chỉ gọi hàm nghiệp vụ và `assert`.
- **Đánh giá câu trả lời:** Rất sát với lỗi thực tế đang tồn tại trong `tuan-08/test_upload.py` của nhóm. Đã đối chiếu lại từng dòng mã nguồn để kiểm chứng trước khi ghi vào bảng tổng hợp lỗi.
- **Điều hiểu thêm:** Bộ test muốn chạy ổn định qua nhiều lần liên tiếp (3x run) không chỉ cần `WebDriverWait`, mà còn cần cô lập dữ liệu test (`tmp_path`), dùng chung một fixture chuẩn (`conftest.py`) và tách bạch giữa lỗi ứng dụng với test cố tình fail.

---

### 1.4. Ngô Quyết Thắng _(Issue #61 – Kiểm thử Basic/Digest Auth & quay video backup 3 phút)_

#### Điều đã học

- Nắm được cách kiểm thử tự động các cơ chế xác thực trình duyệt **Basic Authentication** (`/basic_auth`) và **Digest Authentication** (`/digest_auth`) bằng Selenium WebDriver.
- Hiểu lý do Selenium không thể thao tác trực tiếp vào cửa sổ popup đăng nhập mức trình duyệt (browser native authentication dialog) như các phần tử HTML thông thường, từ đó áp dụng kỹ thuật truyền thông tin xác thực qua URL (`https://admin:admin@the-internet.herokuapp.com/basic_auth`) cho ca hợp lệ và kiểm tra phản hồi khi sai thông tin xác thực.
- Biết cách quay video backup tối đa 3 phút trình diễn toàn bộ bộ kiểm thử (`pytest` + `report.html`) để dự phòng rủi ro mạng hoặc môi trường khi thuyết trình Vòng 2.

#### Ghi chú sử dụng AI

- **Câu hỏi đã hỏi AI:** Vì sao `driver.switch_to.alert` không bắt được hộp thoại đăng nhập của trang `/basic_auth` và `/digest_auth`, và làm thế nào để kiểm thử cả ca thành công lẫn ca thất bại trong Selenium?
- **Tóm tắt câu trả lời:** AI giải thích rằng hộp thoại Basic/Digest Auth là giao diện gốc (native UI) do trình duyệt vẽ khi nhận HTTP `401 Unauthorized`, không phải JavaScript `alert()` trong DOM nên `switch_to.alert` không tương tác được. Để tự động hóa, có thể truyền `username:password@` trực tiếp trong URL cho ca hợp lệ, hoặc kiểm tra trạng thái không được phép truy cập / thông báo lỗi khi bỏ trống hoặc truyền sai thông tin đăng nhập.
- **Đánh giá câu trả lời:** Đúng với cơ chế hoạt động thực tế của Selenium và trình duyệt Chrome khi kiểm thử trên `the-internet.herokuapp.com`.
- **Điều hiểu thêm:** Khi viết chú thích tiếng Việt cho kỹ thuật chèn credentials vào URL, cần lưu ý rõ rằng cách này chỉ phù hợp cho môi trường kiểm thử/demo, không nên ghi mật khẩu thật trực tiếp trong mã nguồn sản phẩm.

---

### 1.5. Lê Thị Nga _(Issue #62 – Test case thủ công Auth & bộ slide Vòng 2 <= 10 trang)_

#### Điều đã học

- Nắm vững quy trình **viết đặc tả test case thủ công trước khi viết mã kiểm thử tự động** (`tuan-09/testcases.md`) cho cả hai tính năng `/basic_auth` và `/digest_auth` (bao gồm các bước thực hiện, dữ liệu đầu vào hợp lệ/không hợp lệ và kết quả mong đợi).
- Hiểu được sự khác biệt về cơ chế bảo mật giữa Basic Auth (gửi thông tin mã hóa Base64 trực tiếp theo header) và Digest Auth (trao đổi challenge-response dùng hàm băm MD5 để tránh gửi mật khẩu thô).
- Biết cách cô đọng nội dung kỹ thuật của 5 tuần (Tuần 5 đến Tuần 9) vào bộ slide Vòng 2 giới hạn tối đa **10 slide**, tập trung vào bằng chứng chạy test, xử lý lỗi và bài học kinh nghiệm thực tế.

#### Ghi chú sử dụng AI

- **Câu hỏi đã hỏi AI:** Cách thiết kế bố cục bộ slide báo cáo kiểm thử tự động Vòng 2 tối đa 10 trang để đủ thông tin (tính năng T5–T9, báo cáo kết quả, lỗi đã sửa, AI usage) mà vẫn gọn gàng, dễ thuyết trình trong 12 phút?
- **Tóm tắt câu trả lời:** AI đề xuất chia 10 slide theo mạch logic: (1) Trang bìa & thành viên; (2) Tổng quan phạm vi T5–T9 & quy trình GitHub; (3–5) Kiến trúc test, `expected_conditions` / POM và minh chứng `report.html`; (6–7) Phân tích lỗi Tuần 7–8 & cách khắc phục; (8) Chế độ Headless & kết quả chạy 3x ổn định; (9) Nhật ký dùng AI có kiểm chứng; (10) Tổng kết & Q&A.
- **Đánh giá câu trả lời:** Rất mạch lạc, giúp cân đối thời lượng giữa phần lý thuyết và phần demo trực tiếp trong khung 12 phút.
- **Điều hiểu thêm:** Slide kỹ thuật không nên dán nguyên đoạn code dài, mà chỉ giữ sơ đồ/bảng so sánh ngắn gọn và ảnh chụp kết quả chạy thực tế để người nghe dễ theo dõi.

---

## 2. Trả lời câu hỏi đọc tài liệu Tuần 9

### Câu 1: `expected_conditions` (EC) trong Selenium hoạt động như thế nào và khác nhau gì giữa các điều kiện phổ biến?

- **Cơ chế hoạt động:** `expected_conditions` (`from selenium.webdriver.support import expected_conditions as EC`) cung cấp các điều kiện kiểm tra dựng sẵn dùng kèm với `WebDriverWait(driver, timeout).until(...)`. Thay vì dừng cứng thời gian như `time.sleep()`, `WebDriverWait` sẽ thăm dò (poll) điều kiện định kỳ (mặc định mỗi 500ms) cho đến khi điều kiện đạt yêu cầu hoặc ném ngoại lệ `TimeoutException` khi hết `timeout`.
- **So sánh các điều kiện thường dùng trong dự án:**
  - `EC.presence_of_element_located(locator)`: Chỉ kiểm tra phần tử đã xuất hiện trong cây DOM hay chưa (phần tử có thể vẫn đang ẩn). Phù hợp với thẻ `<input type="file">` bị ẩn hoặc khi chỉ cần đọc thuộc tính DOM.
  - `EC.visibility_of_element_located(locator)`: Kiểm tra phần tử vừa có trong DOM vừa hiển thị rõ trên màn hình (kích thước > 0, không bị `display: none` hay `visibility: hidden`). Phù hợp khi kiểm tra thông báo kết quả (`#flash`, `h3`, `#uploaded-files`).
  - `EC.element_to_be_clickable(locator)`: Kiểm tra phần tử đã hiển thị và đang ở trạng thái kích hoạt (enabled), sẵn sàng nhận thao tác `.click()`. Phù hợp cho nút bấm (`button`, `#file-submit`) hoặc checkbox.
  - `EC.url_contains(substring)` / `EC.text_to_be_present_in_element(locator, text)`: Chờ URL chuyển hướng đúng trang đích hoặc nội dung văn bản cập nhật bất đồng bộ sau khi gửi form.
- **Lưu ý quan trọng:** Không nên trộn `driver.implicitly_wait()` chung với `WebDriverWait`, vì khi phần tử chưa tồn tại ngay, hai cơ chế có thể cộng dồn thời gian chờ gây chậm và sai lệch ngưỡng timeout mong muốn.

---

### Câu 2: `headless` mode là gì? Khi nào nên dùng và cần lưu ý gì khi chạy kiểm thử ở chế độ này?

- **Khái niệm:** **Headless mode** là chế độ chạy trình duyệt (Chrome/Edge) ở chế độ nền mà không mở cửa sổ giao diện đồ họa (GUI). Trong Selenium 4 với Chrome, ta cấu hình qua `ChromeOptions`:
  ```python
  options = webdriver.ChromeOptions()
  options.add_argument("--headless=new")
  options.add_argument("--window-size=1920,1080")
  ```
- **Ưu điểm & khi nào nên dùng:**
  - Tiêu tốn ít RAM/CPU hơn và khởi tạo nhanh hơn so với chế độ mở giao diện đầy đủ.
  - Bắt buộc sử dụng trong môi trường CI/CD (GitHub Actions, Docker, máy chủ Linux không có màn hình hiển thị).
  - Rất phù hợp khi chạy lặp lại toàn bộ bộ test nhiều lần liên tiếp (regression / 3x consecutive run).
- **Nhược điểm & cách khắc phục khi debug:**
  - Không quan sát trực tiếp được luồng thao tác trên màn hình để phát hiện lỗi giao diện.
  - Viewport mặc định ở headless có thể nhỏ hơn màn hình desktop thật, làm thay đổi bố cục hoặc che mất nút bấm (cần ép kích thước `--window-size=1920,1080` thay vì chỉ gọi `maximize_window()`).
  - **Giải pháp:** Luôn kết hợp chụp ảnh màn hình tự động (`driver.save_screenshot()`) khi xảy ra lỗi và xuất báo cáo `pytest-html --self-contained-html` để xem lại chi tiết trạng thái trình duyệt.

---

### Câu 3: Cấu trúc `Page Object Model` (POM) là gì và mang lại lợi ích gì cho bộ test của nhóm?

- **Khái niệm:** **Page Object Model (POM)** là mẫu thiết kế (design pattern) giúp tách biệt hoàn toàn giữa **lớp mô tả giao diện & thao tác trang** (Page Classes) và **lớp kịch bản kiểm thử** (Test Scripts). Mỗi trang web được đóng gói thành một class Python riêng.
- **Cấu trúc thư mục tiêu chuẩn:**
  ```text
  pages/
    base_page.py        # Chứa driver, WebDriverWait và các hàm dùng chung (find, click, input_text, get_text)
    login_page.py       # Locator + các hành động trên /login (enter_username, enter_password, submit)
    upload_page.py      # Locator + hành động trên /upload (upload_file, get_result_heading)
    auth_page.py        # Logic cho /basic_auth và /digest_auth
  tests/
    conftest.py         # Fixture driver dùng chung cho toàn dự án
    test_login.py       # Chỉ gọi phương thức từ LoginPage và thực hiện assert
    test_upload.py      # Chỉ gọi phương thức từ UploadPage và thực hiện assert
  ```
- **Lợi ích đối với dự án nhóm:**
  - **Dễ bảo trì:** Khi `id`, `CSS selector` hay `XPath` của một phần tử thay đổi, chỉ cần cập nhật tại một nơi duy nhất trong Page Class thay vì sửa hàng loạt file test.
  - **Tái sử dụng cao:** Các ca kiểm thử (Positive/Negative) dùng chung phương thức thao tác và logic `WebDriverWait` từ `BasePage`, tránh lặp code như tình trạng trùng fixture ở Tuần 8.
  - **Mã nguồn test sạch, dễ đọc:** File test tập trung vào các bước nghiệp vụ và `assert`, thuận tiện cho việc review chéo giữa các thành viên.

---

## 3. Tổng hợp lỗi và nguyên nhân gốc rễ từ Tuần 7–8

### 3.1. Nhật ký cập nhật & Kết quả kiểm chứng (Issue #63 – Nguyễn Phúc Hưng)

- **Các điểm đã xử lý trong code:**
  - `tuan-07/test_checkboxes.py`: Sửa `assert not checkbox_1.is_selected()` trong `test_checkboxes_fail_case_invalid_action` để kiểm chứng đúng trạng thái bỏ chọn sau khi click 2 lần; đổi `presence_of_all_elements_located` sang `visibility_of_all_elements_located` ở `test_checkbox_happy_path`.
  - `tuan-08/test_upload.py`: Gộp 2 fixture `driver` trùng lặp thành 1 fixture chuẩn (bỏ `implicitly_wait(10)`), chuyển `test_upload_invalid_file_fail_case` sang dùng fixture `(driver, tmp_path)` và cập nhật `assert` khớp với `'File type not allowed'`; thay kiểm tra `page_source` ở `test_upload_file_invalid` bằng `WebDriverWait` đọc văn bản hiển thị trên thẻ body.
- **Kết quả chạy kiểm chứng 3 lần liên tiếp (`pytest -v tuan-07/ tuan-08/`):**
  - Lần 1: `5 passed`
  - Lần 2: `5 passed`
  - Lần 3: `5 passed`

Bảng dưới đây tổng hợp các lỗi/vấn đề kỹ thuật được phát hiện từ bộ mã nguồn Tuần 7 (`tuan-07/test_checkboxes.py`) và Tuần 8 (`tuan-08/test_upload.py`, `tuan-08/notes.md`, `tuan-08/report.html`), nguyên nhân gốc rễ và hướng xử lý chuẩn hóa cho Vòng 2:

| STT | Phạm vi / File                                                              | Mô tả lỗi / Vấn đề quan sát được                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Nguyên nhân gốc rễ (Root Cause)                                                                                                                                                                                                                        | Hướng khắc phục chuẩn hóa                                                                                                                                                                                                                                                                                       |
| --- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `tuan-08/test_upload.py` (dòng 8–13 và 80–92)                               | Khai báo trùng `@pytest.fixture def driver()` hai lần trong cùng một file; fixture đầu tiên dùng `driver.implicitly_wait(10)` nhưng không `maximize_window()`, fixture thứ hai lại không có `implicitly_wait`.                                                                                                                                                                                                                                                                                          | Khi gộp script của 3 thành viên vào chung `tuan-08/test_upload.py` ở Tuần 8, các đoạn fixture không được tách ra `conftest.py` hoặc hợp nhất, khiến fixture sau ghi đè fixture trước và trộn Implicit Wait với `WebDriverWait`.                        | Giữ duy nhất một `@pytest.fixture def driver()` (hoặc tách vào `conftest.py`), loại bỏ hoàn toàn `implicitly_wait(10)` và chỉ sử dụng Explicit Wait (`WebDriverWait` + `EC`).                                                                                                                                   |
| 2   | `tuan-08/test_upload.py` (`test_upload_invalid_file_fail_case`, dòng 32–75) | (a) Hàm test tự khởi tạo `webdriver.Chrome()` trong `try/finally` thay vì nhận fixture `driver`.<br>(b) Tạo file `virus_gia.exe` trực tiếp bằng `os.path.abspath("virus_gia.exe")` tại thư mục chạy lệnh thay vì `tmp_path`.<br>(c) Test thất bại ở lệnh `assert result_message.text == "Unsupported file format"`: trong `tuan-08/report.html` ghi nhận thực tế `AssertionError` với text `'File type not allowed'`, còn `tuan-08/notes.md` ghi nhận trường hợp trang web hiển thị `'File Uploaded!'`. | Chưa tái sử dụng test harness fixture và `tmp_path` của `pytest`; đồng thời kịch bản được viết theo dạng intentional failure với chuỗi kỳ vọng không khớp phản hồi thực tế của server `/upload`.                                                       | Chuẩn hóa nhận `(driver, tmp_path)` từ fixture; đồng bộ assertion theo phản hồi thực tế hoặc đánh dấu `@pytest.mark.xfail` nếu muốn giữ case kiểm chứng thiếu validation nhất quán của server mà vẫn đảm bảo test suite pass 3 lần liên tiếp.                                                                   |
| 3   | `tuan-08/test_upload.py` (`test_upload_file_invalid`, dòng 15–31)           | Khi nhấn nút Upload mà không chọn tệp, trang web trả về lỗi `500 Internal Server Error` (lỗi xử lý phía backend thay vì thông báo UX hợp lệ). Ngoài ra, script dùng `in driver.page_source` để kiểm tra trên toàn bộ mã nguồn HTML.                                                                                                                                                                                                                                                                     | Ứng dụng đích không kiểm tra dữ liệu đầu vào rỗng trước khi xử lý trên server; đồng thời script tìm chuỗi trên toàn bộ `page_source` thay vì định vị phần tử hiển thị thông báo cụ thể (như thẻ `h1`).                                                 | Chờ và định vị đúng phần tử hiển thị thông báo bằng `WebDriverWait` + `EC.visibility_of_element_located` thay cho tìm trên `page_source`; ghi nhận lỗi `500 Internal Server Error` vào báo cáo bug của ứng dụng.                                                                                                |
| 4   | `tuan-07/test_checkboxes.py` (dòng 16–68)                                   | (a) `test_checkboxes_fail_case_invalid_action` cố tình click đúp 2 lần vào checkbox 1 rồi `assert checkbox_1.is_selected()` nên luôn báo `FAILED` mỗi lần chạy suite.<br>(b) `test_checkbox_happy_path` dùng `EC.presence_of_all_elements_located` thay vì điều kiện sẵn sàng hiển thị/click.                                                                                                                                                                                                           | (a) Thiết kế theo bài tập intentional fail của Tuần 7 làm gián đoạn kết quả Pass chung khi chạy kiểm chứng ổn định 3x ở Tuần 9.<br>(b) `presence_of_all_elements_located` chỉ kiểm tra phần tử có trong DOM chứ chưa bảo đảm sẵn sàng nhận `.click()`. | (a) Chuyển negative case về đúng đặc tả `TC03` trong `tuan-07/testcases.md` (tải lại trang F5 để xác nhận trạng thái checkbox không được lưu) hoặc đánh dấu `xfail` riêng nếu giữ case cố tình fail.<br>(b) Nâng cấp điều kiện chờ sang `EC.element_to_be_clickable` / `EC.visibility_of_all_elements_located`. |
| 5   | `tuan-07/` & `tuan-08/` (Phạm vi kịch bản)                                  | Issue `#63` đề cập rà soát `/dynamic_controls` (Tuần 7) và `/download` (Tuần 8), trong khi trên `main` hiện tại `tuan-07/` triển khai `/checkboxes` (đã đổi từ Dynamic Controls ở commit `ba63041`) và `tuan-08/` chỉ mới có `/upload`.                                                                                                                                                                                                                                                                 | Nhóm đã điều chỉnh đề tài Tuần 7 sang `/checkboxes` và Tuần 8 mới tập trung hoàn thành `/upload`, chưa bổ sung script cho `/dynamic_controls` và `/download`.                                                                                          | Thống nhất chốt phạm vi bộ test Vòng 2 gồm `/login` (T5), `/checkboxes` (T7), `/upload` (T8), `/basic_auth` & `/digest_auth` (T9), hoặc bổ sung thêm script ổn định nếu nhóm trưởng yêu cầu.                                                                                                                    |

---

## 4. Kế hoạch điều phối Diễn tập Demo Vòng 2 (12 phút) & Mock Q&A

**Vai trò điều phối & Timekeeper:** Nguyễn Tiến Dũng  
**Mục tiêu:** Hoàn thành tối thiểu 01 buổi chạy thử (dry run) đúng tổng thời lượng **12 phút** kèm phần hỏi đáp giả lập (Mock Q&A).

### 4.1. Phân bổ thời lượng 12 phút (Timekeeping Plan)

| Mốc thời gian   | Thời lượng | Nội dung trình bày                                                                                                                                                                                                                                                          | Phụ trách                           | Tín hiệu Timekeeper                                      |
| --------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | -------------------------------------------------------- |
| `00:00 – 02:00` | 2 phút     | Giới thiệu nhóm C06-N08, mục tiêu Vòng 2, quy trình làm việc GitHub (Issue → Branch → PR → Review → `week-0X` → `main`) và tổng quan tính năng T5–T9.                                                                                                                       | Phùng Dũng / Lê Thị Nga             | Nhắc nhẹ ở mốc `01:45`                                   |
| `02:00 – 07:00` | 5 phút     | **Demo trực tiếp (Live Demo):** chạy bộ test tự động các tính năng (`/login`, `/checkboxes`, `/upload`, `/basic_auth`, `/digest_auth`), trình chiếu kết quả `pytest-html` (`report.html`) và log chạy ổn định 3 lần (`run_log.md`). _(Dự phòng video 3 phút nếu mạng lỗi)._ | Ngô Quyết Thắng / Phùng Dũng        | Báo mốc còn 1 phút ở `06:00`, chốt chuyển phần ở `07:00` |
| `07:00 – 10:00` | 3 phút     | Phân tích kỹ thuật: Các lỗi/flaky đã sửa từ Tuần 7–8, áp dụng `expected_conditions`, `headless` mode, cấu trúc `Page Object`, và cách nhóm dùng + kiểm chứng AI.                                                                                                            | Nguyễn Phúc Hưng / Nguyễn Tiến Dũng | Báo mốc `09:30`, chốt ở `10:00`                          |
| `10:00 – 12:00` | 2 phút     | Tổng kết bài học kinh nghiệm, kết quả đạt được so với Vòng 1 và chuyển sang phần Q&A.                                                                                                                                                                                       | Phùng Dũng                          | Chốt dứt điểm ở `12:00`                                  |

### 4.2. Bộ câu hỏi Mock Q&A chuẩn bị cho buổi diễn tập

1. **Về cơ chế Wait & `expected_conditions`:** Tại sao nhóm thay toàn bộ `time.sleep()` bằng `WebDriverWait` + `expected_conditions`? Khi nào dùng `presence_of_element_located` thay vì `element_to_be_clickable`?
2. **Về gỡ lỗi & ổn định bộ test (Tuần 7–8):** Nhóm đã phát hiện những lỗi gì trong `tuan-07/test_checkboxes.py` và `tuan-08/test_upload.py` (fixture trùng, trộn Implicit/Explicit Wait, tạo file tạm ngoài `tmp_path`, test cố tình fail), và đã xử lý ra sao để chạy ổn định 3 lần liên tiếp?
3. **Về `headless` mode:** Nếu chạy test ở chế độ `headless` trên CI/CD mà bị fail thì nhóm làm sao biết lỗi xảy ra ở bước nào trên giao diện?
4. **Về cấu trúc `Page Object Model`:** Nếu giao diện trang `/login` hoặc `/upload` thay đổi selector, thiết kế Page Object giúp ích gì so với cách viết script phẳng hiện tại?
5. **Về kiểm thử Basic/Digest Auth:** Tại sao Selenium không thể thao tác trực tiếp vào hộp thoại popup đăng nhập trình duyệt của `/basic_auth`, và cách truyền `https://user:pass@...` giải quyết như thế nào?
6. **Về sử dụng AI có trách nhiệm:** Nhóm kiểm chứng code do AI gợi ý bằng cách nào để tránh lỗi ẩn (như trộn wait hoặc assertion sai logic)?

### 4.3. Biên bản ghi nhận buổi Dry Run 12 phút

- **Trạng thái:** Đang chờ cả nhóm thực hiện buổi chạy thử có bấm giờ (sẽ cập nhật thời gian thực tế từng phần và nhận xét sau buổi rehearsal).
