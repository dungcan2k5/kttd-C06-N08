# Giải thích các lệnh Selenium quan trọng

## 1. `find_element()`

**Chức năng:** Tìm và xác định một phần tử HTML trên trang web để Selenium có thể tương tác với phần tử đó.

Ví dụ:

```python
username_field = driver.find_element(By.ID, "username")
```

**Giải thích:**
- `driver`: đối tượng điều khiển trình duyệt.
- `find_element()`: tìm một phần tử trên trang web.
- `By.ID`: tìm phần tử dựa trên thuộc tính `id` của HTML.
- `"username"`: giá trị thuộc tính `id` của ô nhập tên đăng nhập.

Trong bài kiểm thử, Selenium dùng lệnh này để xác định ô username, ô password và nút đăng nhập.

Một số cách xác định phần tử phổ biến:
- `By.ID`: tìm theo thuộc tính `id`.
- `By.NAME`: tìm theo thuộc tính `name`.
- `By.CSS_SELECTOR`: tìm bằng CSS Selector.
- `By.XPATH`: tìm bằng biểu thức XPath.

**Lưu ý:** `find_element()` trả về phần tử đầu tiên phù hợp với locator. Nếu không tìm thấy phần tử, Selenium sẽ phát sinh lỗi `NoSuchElementException`.

## 2. `send_keys()`

**Chức năng:** Nhập dữ liệu hoặc gửi các phím bấm đến một phần tử có thể nhận dữ liệu, chẳng hạn như ô nhập liệu.

Ví dụ:

```python
username_field.send_keys("tomsmith")
password_field.send_keys("WrongPassword123!")
```

**Giải thích:**
- `username_field` và `password_field` là các phần tử đã được Selenium tìm thấy.
- `send_keys()` đưa chuỗi ký tự vào các ô tương ứng.
- Ví dụ trên nhập tên đăng nhập hợp lệ và mật khẩu sai để kiểm tra trường hợp đăng nhập thất bại.

**Lưu ý:** Phần tử cần sẵn sàng nhận dữ liệu trước khi gọi `send_keys()`. Nếu cần, có thể dùng `WebDriverWait` để đợi phần tử xuất hiện và có thể tương tác.

## 3. `assert`

**Chức năng:** Kiểm tra kết quả thực tế có đáp ứng điều kiện mong đợi hay không.

Ví dụ:

```python
assert "Your password is invalid!" in message.text
```

**Giải thích:**
- `message.text`: nội dung thông báo thực tế trên trang web.
- `"Your password is invalid!"`: thông báo lỗi mong đợi.
- `in`: kiểm tra chuỗi mong đợi có nằm trong thông báo thực tế hay không.

Nếu điều kiện đúng, test tiếp tục chạy. Nếu điều kiện sai, pytest đánh dấu test thất bại và hiển thị thông tin giúp xác định nguyên nhân.

Ví dụ kiểm tra đăng nhập thành công:

```python
assert "/secure" in driver.current_url
```

Lệnh này kiểm tra URL hiện tại có chứa `/secure`, là trang được mong đợi sau khi đăng nhập thành công.

## Kết luận

Ba thành phần trên đảm nhiệm ba vai trò chính trong kiểm thử tự động bằng Selenium:

1. `find_element()` — tìm phần tử cần thao tác.
2. `send_keys()` — nhập dữ liệu kiểm thử.
3. `assert` — xác minh kết quả thực tế so với kết quả mong đợi.

Kết hợp các thao tác này với `click()` để nhấn nút đăng nhập và `WebDriverWait` để chờ trang phản hồi giúp bài kiểm thử rõ ràng và ổn định hơn.