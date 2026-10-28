# Test Cases – Điều khiển động (Dynamic Controls)

## TC01 – Xóa và thêm lại phần tử Checkbox thành công (Positive Case)

### Mục tiêu: Kiểm tra hệ thống có thể xóa phần tử checkbox khỏi giao diện và thêm lại thành công một cách bất đồng bộ sau khi người dùng nhấn nút điều khiển tương ứng.

- **Các bước thực hiện:**
  1. Mở trình duyệt Chrome và truy cập đường dẫn `/dynamic_controls`.
  2. Quan sát và xác nhận ô checkbox ("A checkbox") đang xuất hiện trên màn hình.
  3. Nhấn vào nút **Remove** trong khu vực Checkbox.
  4. Chờ thanh trạng thái tải (loading bar - "Wait for it...") biến mất và thông báo xuất hiện.
  5. Xác nhận checkbox đã biến mất khỏi giao diện và thông báo `"It's gone!"` hiển thị.
  6. Nhấn vào nút **Add** (nút Remove đã tự động đổi tên thành Add).
  7. Chờ thanh trạng thái tải biến mất.
  8. Quan sát phản hồi trên giao diện, kiểm tra sự xuất hiện trở lại của ô checkbox và thông báo thành công.

- **Dữ liệu đầu vào:**
  - Không có dữ liệu nhập bằng văn bản.
  - Hành động click: nút "Remove", sau đó nút "Add".

- **Kết quả mong đợi:**
  - Sau bước 3-5: Ô checkbox không còn hiển thị trên giao diện; xuất hiện thông báo text `"It's gone!"`; nút đổi nhãn thành `"Add"`.
  - Sau bước 6-8: Ô checkbox xuất hiện trở lại trên giao diện; xuất hiện thông báo text `"It's back!"`; nút đổi nhãn lại thành `"Remove"`.

---

## TC02 – Kích hoạt và nhập dữ liệu vào ô nhập liệu thành công (Positive Case)

### Mục tiêu: Kiểm tra ô nhập liệu được kích hoạt (enabled) từ trạng thái bị vô hiệu hóa (disabled) và cho phép người dùng nhập dữ liệu văn bản thành công.

- **Các bước thực hiện:**
  1. Mở trình duyệt Chrome và truy cập đường dẫn `/dynamic_controls`.
  2. Xác nhận ô nhập liệu (input) ban đầu đang ở trạng thái bị vô hiệu hóa (thuộc tính `disabled` kích hoạt).
  3. Nhấn vào nút **Enable** trong khu vực Input.
  4. Chờ thanh trạng thái tải (loading bar - "Wait for it...") biến mất.
  5. Xác nhận thông báo trạng thái xuất hiện và ô nhập liệu đã chuyển sang trạng thái sẵn sàng nhận dữ liệu.
  6. Nhập một chuỗi ký tự hợp lệ vào ô nhập liệu.
  7. Quan sát kết quả và kiểm tra giá trị thực tế hiển thị bên trong ô nhập liệu.

- **Dữ liệu đầu vào:**
  - Hành động click: nút "Enable".
  - Dữ liệu nhập vào ô input: `"Kiem thu tu dong nhom 08"`.

- **Kết quả mong đợi:**
  - Sau khi nhấn "Enable" và hoàn tất chờ: Hệ thống hiển thị thông báo text `"It's enabled!"`; nút chuyển nhãn thành `"Disable"`.
  - Ô input không còn thuộc tính `disabled` (trạng thái `is_enabled() == True`).
  - Người dùng có thể nhập văn bản thành công; giá trị trong ô input hiển thị đúng chuỗi `"Kiem thu tu dong nhom 08"`.

---

## TC03 – Thao tác nhập liệu thất bại khi ô input đang bị vô hiệu hóa (Negative / Fail Case)

### Mục tiêu: Kiểm tra cơ chế kiểm soát giao diện khi người dùng hoặc script cố gắng gửi dữ liệu / thao tác vào ô nhập liệu khi ô này chưa được kích hoạt (đang ở trạng thái disabled).

- **Các bước thực hiện:**
  1. Mở trình duyệt Chrome và truy cập đường dẫn `/dynamic_controls`.
  2. Xác nhận ô nhập liệu đang ở trạng thái bị khóa / vô hiệu hóa (`disabled = true`).
  3. Không thực hiện nhấn nút "Enable", trực tiếp thực hiện hành vi nhập dữ liệu văn bản vào ô input (thông qua phương thức `send_keys`).
  4. Quan sát phản hồi của trình duyệt và hệ thống kiểm thử tự động.
  5. Kiểm tra giá trị bên trong ô nhập liệu.

- **Dữ liệu đầu vào:**
  - Dữ liệu cố gắng nhập: `"Du lieu kiem thu khi chua kich hoat"`.
  - Trạng thái phần tử: Ô input đang bị disabled (chưa nhấn "Enable").

- **Kết quả mong đợi:**
  - Trình duyệt không cho phép người dùng nhập văn bản vào ô input.
  - Khi thực thi kiểm thử tự động bằng Selenium WebDriver, câu lệnh gọi `send_keys` trên ô input bị disabled sẽ bị chặn và phát sinh ngoại lệ lỗi tương tác (`ElementNotInteractableException`).
  - Giá trị trong ô nhập liệu vẫn là rỗng (`""`), không bị thay đổi bởi thao tác nhập dữ liệu không hợp lệ.

---

# ID, CSS selector, XPath

### 1. Khu vực điều khiển Checkbox (Remove / Add)

- **Checkbox element:**
  - XPath: `//form[@id='checkbox-example']//input[@type='checkbox']` hoặc `//div[@id='checkbox']/input`
  - id: `checkbox` (id của thẻ div bao ngoài)
  - CSS Selector: `#checkbox-example input[type="checkbox"]` hoặc `#checkbox input`

- **Nút Remove / Add (Checkbox button):**
  - XPath: `//form[@id='checkbox-example']/button`
  - CSS Selector: `#checkbox-example button`

- **Thanh trạng thái tải Checkbox (Loading):**
  - XPath: `//form[@id='checkbox-example']/div[@id='loading']`
  - id: `loading`
  - CSS Selector: `#checkbox-example #loading`

- **Thông báo kết quả Checkbox (Message):**
  - XPath: `//form[@id='checkbox-example']/p[@id='message']`
  - id: `message`
  - CSS Selector: `#checkbox-example #message`

---

### 2. Khu vực điều khiển Input (Enable / Disable)

- **Ô nhập liệu (Input field):**
  - XPath: `//form[@id='input-example']/input`
  - CSS Selector: `#input-example input`

- **Nút Enable / Disable (Input button):**
  - XPath: `//form[@id='input-example']/button`
  - CSS Selector: `#input-example button`

- **Thanh trạng thái tải Input (Loading):**
  - XPath: `//form[@id='input-example']/div[@id='loading']`
  - id: `loading`
  - CSS Selector: `#input-example #loading`

- **Thông báo kết quả Input (Message):**
  - XPath: `//form[@id='input-example']/p[@id='message']`
  - id: `message`
  - CSS Selector: `#input-example #message`
