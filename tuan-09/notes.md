# Ghi chú tuần 09 – Tổng hợp kiến thức, khắc phục lỗi Tuần 7–8 & Chuẩn bị Demo Vòng 2

**Nhóm:** C06-N08  
**Nhánh làm việc:** `t09-tiendung` (Issue `#64`)  
**Thành viên phụ trách tổng hợp:** Nguyễn Tiến Dũng  

> **Lưu ý trạng thái đồng bộ:** Tài liệu đã hoàn thiện phần của Nguyễn Tiến Dũng, phần trả lời câu hỏi đọc tài liệu Tuần 9, bảng phân tích các lỗi/vấn đề phát hiện từ mã nguồn Tuần 7–8, và khung điều phối buổi diễn tập 12 phút + Mock Q&A. Các mục riêng của 4 thành viên còn lại, kết quả sau khi fix từ Issue `#63`, và biên bản giờ chạy dry run thực tế đang để khung `[Chờ bổ sung]` để cập nhật ngay khi nhóm hoàn tất các nhánh `t09-*` và buổi diễn tập.

---

## 1. Ghi nhận học tập & Nhật ký sử dụng AI của 5 thành viên

### 1.1. Nguyễn Tiến Dũng *(Issue #64 – Tổng hợp ghi chú & Timekeeper diễn tập 12 phút)*

#### Điều đã học
- Nắm vững cách tổ chức và chuẩn hóa tài liệu kỹ thuật nhóm: đối chiếu mã nguồn thực tế (`tuan-07/test_checkboxes.py`, `tuan-08/test_upload.py`, `tuan-08/report.html`) với ghi chú của từng thành viên để phát hiện điểm không nhất quán trước khi chốt bộ test Vòng 2.
- Hiểu sâu hơn về nhóm điều kiện chờ `expected_conditions` (EC) trong Selenium (phân biệt `presence_of_element_located`, `visibility_of_element_located`, `element_to_be_clickable`, `url_contains`), cách cấu hình **Headless mode** cho Chrome trong CI/CD, và tư duy tách lớp bằng **Page Object Model (POM)** để tránh lặp locator.
- Rèn luyện kỹ năng điều phối buổi diễn tập (rehearsal) đúng khung thời gian 12 phút và chuẩn bị bộ câu hỏi phản biện (Mock Q&A) giúp cả nhóm trả lời thống nhất, không bị lúng túng khi bảo vệ.

#### Ghi chú sử dụng AI
- **Câu hỏi đã hỏi AI:** Khi nhiều thành viên cùng gộp test vào một file như `tuan-08/test_upload.py`, những lỗi cấu trúc nào dễ xảy ra và mô hình Page Object Model giúp xử lý ra sao?
- **Tóm tắt câu trả lời:** AI chỉ ra việc định nghĩa trùng `@pytest.fixture def driver()` trong cùng file sẽ khiến fixture sau ghi đè fixture trước, việc trộn `implicitly_wait` với `WebDriverWait` dễ gây thời gian chờ khó đoán, và tự tạo `webdriver.Chrome()` rời rạc ngoài fixture dễ gây rò rỉ tiến trình. Page Object Model giải quyết vấn đề bảo trì bằng cách gom locator và thao tác của mỗi trang vào một class riêng, còn file test chỉ gọi hàm nghiệp vụ và `assert`.
- **Đánh giá câu trả lời:** Rất sát với lỗi thực tế đang tồn tại trong `tuan-08/test_upload.py` của nhóm. Nhóm đã kiểm tra lại mã nguồn từng dòng để xác nhận chính xác các điểm trùng lặp trước khi ghi vào bảng tổng hợp lỗi.
- **Điều hiểu thêm:** Code test muốn chạy ổn định qua nhiều lần liên tiếp (3x run) không chỉ cần `WebDriverWait`, mà còn cần test isolation (dùng `tmp_path`, dùng chung một fixture chuẩn qua `conftest.py`) và tách bạch giữa *lỗi của ứng dụng* với *test cố tình fail*.

---

### 1.2. Phùng Dũng – Nhóm trưởng *(Issue #60 – Ổn định bộ test, chạy 3x log & tích hợp nhánh `week-09`)*

#### Điều đã học
- `[Chờ bổ sung sau khi hoàn thành Issue #60]`

#### Ghi chú sử dụng AI
- **Câu hỏi đã hỏi AI:** `[Chờ bổ sung]`
- **Tóm tắt câu trả lời:** `[Chờ bổ sung]`
- **Đánh giá câu trả lời:** `[Chờ bổ sung]`
- **Điều hiểu thêm:** `[Chờ bổ sung]`

---

### 1.3. Nguyễn Phúc Hưng *(Issue #63 – Debug & sửa flaky/failing tests Tuần 7–8)*

#### Điều đã học
- `[Chờ bổ sung sau khi hoàn thành Issue #63]`

#### Ghi chú sử dụng AI
- **Câu hỏi đã hỏi AI:** `[Chờ bổ sung]`
- **Tóm tắt câu trả lời:** `[Chờ bổ sung]`
- **Đánh giá câu trả lời:** `[Chờ bổ sung]`
- **Điều hiểu thêm:** `[Chờ bổ sung]`

---

### 1.4. Ngô Quyết Thắng *(Issue #61 – Kiểm thử Basic/Digest Auth & quay video backup 3 phút)*

#### Điều đã học
- `[Chờ bổ sung sau khi hoàn thành Issue #61]`

#### Ghi chú sử dụng AI
- **Câu hỏi đã hỏi AI:** `[Chờ bổ sung]`
- **Tóm tắt câu trả lời:** `[Chờ bổ sung]`
- **Đánh giá câu trả lời:** `[Chờ bổ sung]`
- **Điều hiểu thêm:** `[Chờ bổ sung]`

---

### 1.5. Lê Thị Nga *(Issue #62 – Test case thủ công Auth & bộ slide Vòng 2 <= 10 trang)*

#### Điều đã học
- `[Chờ bổ sung sau khi hoàn thành Issue #62]`

#### Ghi chú sử dụng AI
- **Câu hỏi đã hỏi AI:** `[Chờ bổ sung]`
- **Tóm tắt câu trả lời:** `[Chờ bổ sung]`
- **Đánh giá câu trả lời:** `[Chờ bổ sung]`
- **Điều hiểu thêm:** `[Chờ bổ sung]`

---

## 2. Trả lời câu hỏi đọc tài liệu Tuần 9

### Câu 1: `expected_conditions` (EC) trong Selenium hoạt động như thế nào và khác nhau gì giữa các điều kiện phổ biến?
- **Cơ chế hoạt động:** `expected_conditions` (`from selenium.webdriver.support import expected_conditions as EC`) cung cấp các điều kiện kiểm tra dựng sẵn để dùng cùng `WebDriverWait(driver, timeout).until(...)`. Thay vì dừng cứng như `time.sleep()`, `WebDriverWait` sẽ thăm dò (poll) điều kiện liên tục (mặc định mỗi 500ms) cho đến khi điều kiện trả về giá trị hợp lệ (khác `False`/`None`) hoặc ném `TimeoutException` khi hết thời gian chờ.
- **So sánh các điều kiện thường dùng trong dự án:**
  - `EC.presence_of_element_located(locator)`: Chỉ kiểm tra phần tử đã xuất hiện trong cây DOM hay chưa (phần tử có thể vẫn đang ẩn). Phù hợp với thẻ `<input type="file">` ẩn hoặc chỉ cần đọc thuộc tính DOM.
  - `EC.visibility_of_element_located(locator)`: Kiểm tra phần tử vừa có trong DOM vừa hiển thị trên giao diện (kích thước > 0, không bị `display: none` hay `visibility: hidden`). Phù hợp khi đọc thông báo kết quả (`#flash`, `h3`, `#uploaded-files`).
  - `EC.element_to_be_clickable(locator)`: Kiểm tra phần tử đã hiển thị và đang ở trạng thái kích hoạt (enabled), sẵn sàng nhận thao tác `.click()`. Phù hợp với nút bấm (`button`, `#file-submit`) hoặc checkbox.
  - `EC.url_contains(substring)` / `EC.text_to_be_present_in_element(locator, text)`: Chờ trạng thái chuyển hướng URL hoặc văn bản cập nhật bất đồng bộ sau khi gửi form.
- **Lưu ý thực hành:** Không nên kết hợp `driver.implicitly_wait()` cùng với `WebDriverWait`, vì khi phần tử chưa có ngay, hai cơ chế có thể cộng dồn thời gian chờ gây chậm hoặc khó dự đoán hành vi timeout.

---

### Câu 2: `headless` mode là gì? Khi nào nên dùng và cần lưu ý gì khi chạy kiểm thử ở chế độ này?
- **Khái niệm:** **Headless mode** là chế độ chạy trình duyệt (như Chrome) mà không mở cửa sổ giao diện đồ họa (GUI) lên màn hình. Trong Selenium 4 với Chrome, ta cấu hình qua `ChromeOptions`:
  ```python
  options = webdriver.ChromeOptions()
  options.add_argument("--headless=new")
  options.add_argument("--window-size=1920,1080")
  ```
- **Ưu điểm & khi nào nên dùng:**
  - Tiêu tốn ít RAM/CPU hơn và khởi chạy nhanh hơn so với chế độ có giao diện.
  - Bắt buộc dùng khi chạy kiểm thử tự động trong pipeline CI/CD (ví dụ GitHub Actions, Docker, máy chủ Linux không có màn hình hiển thị).
  - Rất phù hợp khi chạy lặp lại toàn bộ bộ kiểm thử (regression / 3x consecutive run) để kiểm chứng độ ổn định.
- **Nhược điểm & cách khắc phục khi debug:**
  - Không quan sát trực tiếp được thao tác trình duyệt bằng mắt thường nên khó thấy lỗi giao diện khi fail.
  - Kích thước viewport mặc định ở headless có thể nhỏ hơn màn hình thật, dễ làm phần tử bị che khuất hoặc thay đổi responsive layout (vì vậy cần truyền `--window-size=1920,1080` thay vì chỉ dựa vào `maximize_window()`).
  - **Giải pháp:** Kết hợp chụp ảnh màn hình tự động (`driver.save_screenshot()`) khi lỗi và xuất báo cáo `pytest-html --self-contained-html` để xem lại log/ảnh chứng minh sau khi chạy.

---

### Câu 3: Cấu trúc `Page Object Model` (POM) là gì và mang lại lợi ích gì cho bộ test của nhóm?
- **Khái niệm:** **Page Object Model (POM)** là mẫu thiết kế (design pattern) trong kiểm thử tự động nhằm tách biệt hoàn toàn giữa **lớp định nghĩa giao diện & thao tác trang** (Page Classes) và **lớp kịch bản kiểm thử** (Test Scripts). Mỗi trang web (hoặc thành phần dùng chung) được biểu diễn thành một class Python riêng.
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
  - **Dễ bảo trì:** Khi một `id` hay `CSS selector` trên trang web thay đổi, chỉ cần sửa đúng 1 chỗ trong file Page Class thay vì tìm sửa rải rác ở nhiều hàm test.
  - **Tái sử dụng mã nguồn:** Nhiều test case (Pass/Fail/Negative) dùng lại cùng các phương thức thao tác và hàm chờ chuẩn hóa từ `BasePage`.
  - **Code test sạch, dễ đọc:** File test chỉ tập trung vào luồng nghiệp vụ và `assert`, giúp các thành viên đọc chéo code của nhau nhanh hơn.

---

## 3. Tổng hợp lỗi và nguyên nhân gốc rễ từ Tuần 7–8

> Phần dưới đây ghi nhận các lỗi/vấn đề thực tế đã rà soát trực tiếp từ mã nguồn trên nhánh `main` (`tuan-07/test_checkboxes.py`, `tuan-08/test_upload.py`, `tuan-08/notes.md`, `tuan-08/report.html`). Các bản sửa lỗi chính thức từ nhánh `t09-hung` (Issue `#63`) sẽ được đối chiếu và cập nhật trạng thái `Đã sửa` sau khi PR của Hưng được mở.

| STT | Phạm vi / File | Mô tả lỗi / Vấn đề quan sát được | Nguyên nhân gốc rễ (Root Cause) | Hướng khắc phục đề xuất | Trạng thái |
|---|---|---|---|---|---|
| 1 | `tuan-08/test_upload.py` (dòng 8–13 và 80–92) | Định nghĩa trùng `@pytest.fixture def driver()` hai lần trong cùng file; fixture đầu tiên gọi `driver.implicitly_wait(10)` nhưng không `maximize_window()`, fixture thứ hai lại không có `implicitly_wait`. | Khi gộp script của 3 thành viên vào chung `tuan-08/test_upload.py`, các đoạn fixture không được tách ra `conftest.py` hoặc hợp nhất, khiến fixture sau ghi đè fixture trước và trộn Implicit Wait với `WebDriverWait`. | Giữ duy nhất một fixture `driver` (nên đưa vào `conftest.py`), bỏ `implicitly_wait(10)` và chỉ dùng Explicit Wait (`WebDriverWait` + `EC`). | Chờ fix (`#63`) |
| 2 | `tuan-08/test_upload.py` (`test_upload_invalid_file_fail_case`, dòng 32–75) | Hàm test không sử dụng fixture `driver` và `tmp_path` mà tự khởi tạo `webdriver.Chrome()` trong `try/finally`, tạo tệp `virus_gia.exe` trực tiếp bằng `os.path.abspath(...)` trong thư mục chạy lệnh. Ngoài ra, assertion kỳ vọng `"Unsupported file format"` bị `FAILED` (trong `tuan-08/report.html` ghi nhận server trả `'File type not allowed'`, còn `tuan-08/notes.md` ghi nhận trường hợp server chấp nhận và báo `'File Uploaded!'`). | Chưa chuẩn hóa sử dụng test harness fixture; sử dụng đường dẫn tương đối ở working directory thay vì `tmp_path`; thiết kế test theo dạng intentional failure dựa trên chuỗi lỗi kỳ vọng không khớp phản hồi thực tế của trang `/upload`. | Chuyển sang nhận `(driver, tmp_path)` từ fixture; đồng bộ kỳ vọng theo phản hồi thực tế của ứng dụng đích hoặc đánh dấu `@pytest.mark.xfail` nếu muốn ghi nhận đây là lỗi thiếu validation nhất quán của server. | Chờ fix (`#63`) |
| 3 | `tuan-08/test_upload.py` (`test_upload_file_invalid`, dòng 15–31) | Khi bấm Upload mà không chọn tệp, trang web trả về `500 Internal Server Error` (lỗi xử lý phía server thay vì thông báo UX hợp lệ). Test dùng `in driver.page_source` để kiểm tra lỗi trên toàn bộ mã HTML trang. | Ứng dụng đích không có bước kiểm tra rỗng trước khi xử lý form; đồng thời script kiểm tra chuỗi trên `page_source` thay vì định vị phần tử thông báo cụ thể (như `h1`). | Định vị phần tử tiêu đề/thông báo bằng `WebDriverWait` + `EC.visibility_of_element_located` thay cho tìm trên `page_source`, đồng thời ghi nhận lỗi HTTP 500 vào báo cáo bug của hệ thống. | Chờ fix (`#63`) |
| 4 | `tuan-07/test_checkboxes.py` (dòng 16–68) | (a) `test_checkboxes_fail_case_invalid_action` cố tình click 2 lần rồi `assert checkbox_1.is_selected()` nên luôn `FAILED` mỗi khi chạy suite.<br>(b) `test_checkbox_happy_path` dùng `EC.presence_of_all_elements_located` thay vì điều kiện sẵn sàng hiển thị/click. | (a) Thiết kế theo yêu cầu intentional fail của Tuần 7 nên làm hỏng kết quả Pass chung khi chạy lại 3 lần ở Tuần 9.<br>(b) `presence_of_all_elements_located` chỉ kiểm tra phần tử có mặt trong DOM chứ chưa đảm bảo tương tác được. | (a) Chuyển negative case sang đúng kịch bản `TC03` trong `tuan-07/testcases.md` (tải lại trang F5 để xác nhận trạng thái không được lưu – Pass khi hành vi khớp đặc tả) hoặc tách/đánh dấu `xfail` nếu giữ intentional fail.<br>(b) Dùng `EC.element_to_be_clickable` / `EC.visibility_of_all_elements_located`. | Chờ fix (`#63`) |
| 5 | `tuan-07/` & `tuan-08/` (Phạm vi kiểm thử) | Issue `#63` đề cập rà soát `/dynamic_controls` (Tuần 7) và `/download` (Tuần 8), nhưng trên `main` hiện tại `tuan-07/` mới có `/checkboxes` (đã đổi ở commit `ba63041`) và `tuan-08/` mới có `/upload` (chưa có script `/download`). | Nhóm đã chuyển đề tài Tuần 7 sang Checkboxes và Tuần 8 mới tập trung `/upload`, chưa bổ sung script cho hai trang còn lại. | Xác nhận lại phạm vi với Nhóm trưởng (`#60`) và Hưng (`#63`): giữ ổn định bộ script hiện có (`/login`, `/checkboxes`, `/upload`, `/basic_auth`, `/digest_auth`) hay bổ sung thêm test ổn định. | Chờ xác nhận (`#60`, `#63`) |

### Chi tiết các bản vá đã áp dụng từ Issue #63 *(Cập nhật sau khi `t09-hung` mở PR)*
- `[Chờ bổ sung danh sách commit / thay đổi cụ thể từ Nguyễn Phúc Hưng]`

---

## 4. Kế hoạch điều phối Diễn tập Demo Vòng 2 (12 phút) & Mock Q&A

**Vai trò điều phối & Timekeeper:** Nguyễn Tiến Dũng  
**Mục tiêu Definition of Done:** Hoàn thành ít nhất 01 buổi chạy thử (dry run) đúng tổng thời lượng **12 phút** + phần hỏi đáp giả lập (Mock Q&A).

### 4.1. Phân bổ thời lượng 12 phút (Timekeeping Plan)

| Mốc thời gian | Thời lượng | Nội dung trình bày | Phụ trách dự kiến | Tín hiệu Timekeeper |
|---|---|---|---|---|
| `00:00 – 02:00` | 2 phút | Giới thiệu nhóm C06-N08, mục tiêu Vòng 2, quy trình làm việc GitHub (Issue → Branch → PR → Review → `week-0X` → `main`) và tổng quan tính năng T5–T9. | Phùng Dũng / Lê Thị Nga | Nhắc nhẹ ở mốc `01:45` |
| `02:00 – 07:00` | 5 phút | **Demo trực tiếp (Live Demo):** chạy bộ test tự động các tính năng (`/login`, `/checkboxes`, `/upload`, `/basic_auth`, `/digest_auth`), trình chiếu kết quả `pytest-html` (`report.html`) và log chạy ổn định 3 lần (`run_log.md`). *(Dự phòng video 3 phút nếu mạng lỗi).* | Ngô Quyết Thắng / Phùng Dũng | Báo mốc còn 1 phút ở `06:00`, chốt chuyển phần ở `07:00` |
| `07:00 – 10:00` | 3 phút | Phân tích kỹ thuật: Các lỗi/flaky đã sửa từ Tuần 7–8, áp dụng `expected_conditions`, `headless` mode, cấu trúc `Page Object`, và cách nhóm dùng + kiểm chứng AI. | Nguyễn Phúc Hưng / Nguyễn Tiến Dũng | Báo mốc `09:30`, chốt ở `10:00` |
| `10:00 – 12:00` | 2 phút | Tổng kết bài học kinh nghiệm, kết quả đạt được so với Vòng 1 và chuyển sang phần Q&A. | Phùng Dũng | Chốt dứt điểm ở `12:00` |

### 4.2. Bộ câu hỏi Mock Q&A chuẩn bị cho buổi diễn tập

1. **Về cơ chế Wait & `expected_conditions`:** Tại sao nhóm thay toàn bộ `time.sleep()` bằng `WebDriverWait` + `expected_conditions`? Khi nào dùng `presence_of_element_located` thay vì `element_to_be_clickable`?
2. **Về gỡ lỗi & ổn định bộ test (Tuần 7–8):** Nhóm đã phát hiện những lỗi gì trong `tuan-07/test_checkboxes.py` và `tuan-08/test_upload.py` (ví dụ fixture trùng, trộn Implicit/Explicit Wait, test cố tình fail), và làm thế nào để đảm bảo bộ test chạy 3 lần liên tiếp đều ổn định?
3. **Về `headless` mode:** Nếu chạy test ở chế độ `headless` trên CI/CD mà bị fail thì nhóm làm sao biết lỗi xảy ra ở bước nào trên giao diện?
4. **Về cấu trúc `Page Object Model`:** Nếu giao diện trang `/login` hoặc `/upload` thay đổi selector, thiết kế Page Object giúp ích gì so với cách viết script phẳng hiện tại?
5. **Về kiểm thử Basic/Digest Auth:** Tại sao Selenium không thể thao tác trực tiếp vào hộp thoại popup đăng nhập trình duyệt của `/basic_auth`, và cách truyền `https://user:pass@...` giải quyết như thế nào?
6. **Về sử dụng AI có trách nhiệm:** Nhóm kiểm chứng code do AI gợi ý bằng cách nào để tránh lỗi ẩn (như trộn wait hoặc assertion sai logic)?

### 4.3. Biên bản ghi nhận buổi Dry Run 12 phút
- **Ngày giờ diễn tập:** `[Chờ thực hiện cùng cả nhóm]`
- **Thành viên tham gia:** `[Chờ ghi nhận: Phùng Dũng, Nguyễn Phúc Hưng, Nguyễn Tiến Dũng, Ngô Quyết Thắng, Lê Thị Nga]`
- **Tổng thời gian thực tế:** `[Chờ bấm giờ / mục tiêu <= 12:00]`
- **Nhận xét & điểm cần chỉnh trước buổi chấm Vòng 2:** `[Chờ ghi nhận sau dry run]`
