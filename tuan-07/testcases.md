# Test Cases – Hộp kiểm (Checkboxes)

## TC01 – Đánh dấu checkbox đang bỏ chọn thành công (Positive Case)

### Mục tiêu: Kiểm tra người dùng có thể nhấp vào ô checkbox đang ở trạng thái bỏ chọn (unchecked) để chuyển nó sang trạng thái đã chọn (checked) thành công.

- **Các bước thực hiện:**
  1. Mở trình duyệt Chrome và truy cập đường dẫn `/checkboxes`.
  2. Quan sát trang và xác nhận có 2 ô checkbox hiển thị ("checkbox 1" và "checkbox 2").
  3. Kiểm tra trạng thái ban đầu: checkbox 1 đang bỏ chọn (unchecked), checkbox 2 đang được chọn (checked).
  4. Nhấp vào **checkbox 1** (ô checkbox đang ở trạng thái unchecked).
  5. Quan sát phản hồi trên giao diện sau khi nhấp.

- **Dữ liệu đầu vào:**
  - Không có dữ liệu nhập bằng văn bản.
  - Hành động click: checkbox 1 (ô checkbox đầu tiên trong danh sách).

- **Kết quả mong đợi:**
  - Sau bước 4: Ô checkbox 1 chuyển sang trạng thái đã chọn (checked), dấu tích xuất hiện bên trong ô.
  - Thuộc tính `is_selected()` của phần tử trả về `True`.
  - Ô checkbox 2 không bị ảnh hưởng, vẫn giữ nguyên trạng thái đã chọn (checked).

---

## TC02 – Bỏ chọn checkbox đang được chọn thành công (Positive Case)

### Mục tiêu: Kiểm tra người dùng có thể nhấp vào ô checkbox đang ở trạng thái đã chọn (checked) để chuyển nó sang trạng thái bỏ chọn (unchecked) thành công.

- **Các bước thực hiện:**
  1. Mở trình duyệt Chrome và truy cập đường dẫn `/checkboxes`.
  2. Quan sát trang và xác nhận có 2 ô checkbox hiển thị.
  3. Xác nhận trạng thái ban đầu: checkbox 2 đang ở trạng thái đã chọn (checked).
  4. Nhấp vào **checkbox 2** (ô checkbox đang ở trạng thái checked).
  5. Quan sát phản hồi trên giao diện sau khi nhấp.

- **Dữ liệu đầu vào:**
  - Không có dữ liệu nhập bằng văn bản.
  - Hành động click: checkbox 2 (ô checkbox thứ hai trong danh sách).

- **Kết quả mong đợi:**
  - Sau bước 4: Ô checkbox 2 chuyển sang trạng thái bỏ chọn (unchecked), dấu tích biến mất khỏi ô.
  - Thuộc tính `is_selected()` của phần tử trả về `False`.
  - Ô checkbox 1 không bị ảnh hưởng, vẫn giữ nguyên trạng thái bỏ chọn ban đầu (unchecked).

---

## TC03 – Trạng thái checkbox không được lưu sau khi tải lại trang (Negative / Fail Case)

### Mục tiêu: Kiểm tra rằng trạng thái checkbox đã thay đổi bởi người dùng sẽ bị mất sau khi tải lại trang, xác nhận trang không có cơ chế lưu trạng thái bền vững (no persistence).

- **Các bước thực hiện:**
  1. Mở trình duyệt Chrome và truy cập đường dẫn `/checkboxes`.
  2. Xác nhận trạng thái ban đầu: checkbox 1 đang bỏ chọn (unchecked), checkbox 2 đang được chọn (checked).
  3. Nhấp vào **checkbox 1** để đổi sang trạng thái checked.
  4. Nhấp vào **checkbox 2** để đổi sang trạng thái unchecked.
  5. Xác nhận cả hai checkbox đã đổi trạng thái thành công (checkbox 1 = checked, checkbox 2 = unchecked).
  6. Tải lại trang (nhấn phím **F5** hoặc nút Refresh trên trình duyệt).
  7. Quan sát trạng thái của cả hai checkbox sau khi tải lại.

- **Dữ liệu đầu vào:**
  - Hành động click: checkbox 1, checkbox 2.
  - Hành động tải lại trang: F5 / Refresh.

- **Kết quả mong đợi:**
  - Sau bước 6-7: Trang quay về trạng thái mặc định ban đầu.
  - Checkbox 1 trở về trạng thái **unchecked** (bỏ chọn).
  - Checkbox 2 trở về trạng thái **checked** (đã chọn).
  - Hệ thống không lưu lại thay đổi mà người dùng đã thực hiện trước khi tải lại trang.

---

# ID, CSS selector, XPath

- **Toàn bộ vùng chứa các checkbox:**
  - XPath: `//form[@id='checkboxes']`
  - id: `checkboxes`
  - CSS Selector: `#checkboxes`

- **Checkbox 1 (ô checkbox đầu tiên – mặc định unchecked):**
  - XPath: `//form[@id='checkboxes']/input[1]`
  - CSS Selector: `#checkboxes input:nth-of-type(1)`

- **Checkbox 2 (ô checkbox thứ hai – mặc định checked):**
  - XPath: `//form[@id='checkboxes']/input[2]`
  - CSS Selector: `#checkboxes input:nth-of-type(2)`

- **Tất cả checkbox trên trang:**
  - XPath: `//form[@id='checkboxes']/input[@type='checkbox']`
  - CSS Selector: `#checkboxes input[type="checkbox"]`
