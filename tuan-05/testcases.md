# Test Cases – Đăng nhập

## TC01 – Đăng nhập thành công với thông tin hợp lệ

### Mục tiêu: Kiểm tra người dùng có thể đăng nhập khi nhập đúng tên đăng nhập và mật khẩu.

 - Các bước thực hiện:
   + Mở trình duyệt Chrome và truy cập trang /login.
   + Nhập tên đăng nhập hợp lệ vào ô tên đăng nhập.
   + Nhập mật khẩu chính xác vào ô mật khẩu.
   + Nhấn nút Đăng nhập.
   + Quan sát kết quả trên giao diện.

 - Dữ liệu đầu vào:
   + Tên đăng nhập: Tài khoản hợp lệ đã được tạo trong hệ thống.
   + Mật khẩu: Mật khẩu chính xác tương ứng với tài khoản.

 - Kết quả mong đợi:
   + Hệ thống chấp nhận thông tin đăng nhập.
   + Người dùng được chuyển đến trang sau đăng nhập hoặc giao diện chính theo thiết kế của ứng dụng.
   + Không xuất hiện thông báo lỗi đăng nhập.
   
## TC02 – Đăng nhập thất bại khi sai mật khẩu

### Mục tiêu: Kiểm tra hệ thống xử lý trường hợp người dùng nhập đúng tên đăng nhập nhưng sai mật khẩu.

 - Các bước thực hiện:

   + Mở trình duyệt Chrome và truy cập trang /login.
   + Nhập tên đăng nhập hợp lệ.
   + Nhập mật khẩu không chính xác.
   + Nhấn nút Đăng nhập.
   + Quan sát thông báo và trạng thái trang.

 - Dữ liệu đầu vào:
   + Tên đăng nhập: Tài khoản hợp lệ đã được tạo trong hệ thống.
   + Mật khẩu: Một mật khẩu sai, không trùng với mật khẩu của tài khoản.

 - Kết quả mong đợi:
   + Hệ thống từ chối đăng nhập.
   + Người dùng không được chuyển đến giao diện dành cho người đã đăng nhập.
   + Giao diện hiển thị thông báo lỗi phù hợp theo thiết kế của ứng dụng.

## TC03 – Đăng nhập khi bỏ trống tên đăng nhập và mật khẩu

### Mục tiêu: Kiểm tra hệ thống xử lý khi người dùng không nhập thông tin đăng nhập.

  - Các bước thực hiện:

    + Mở trình duyệt Chrome và truy cập trang /login.
    + Để trống ô tên đăng nhập.
    + Để trống ô mật khẩu.
    + Nhấn nút Đăng nhập.
    + Quan sát phản hồi của hệ thống.

  - Dữ liệu đầu vào:

    + Tên đăng nhập: Để trống.
    + Mật khẩu: Để trống.

  - Kết quả mong đợi:

    + Hệ thống không cho phép đăng nhập thành công.
    + Nếu các trường bắt buộc được kiểm tra ở giao diện, hệ thống hiển thị thông báo yêu cầu nhập thông tin.
    + Người dùng vẫn ở trang đăng nhập cho đến khi cung cấp thông tin hợp lệ.



# ID, CSS selector, XPath
- Uername:
    + XPath: //*[@id="username"]
    + id: username
    + CSS Selector: #username

- Password
    + XPath: //*[@id="password"]
    + id: password
    + CSS Selector: #password

- Login Button:
    + XPath: //button[@type="submit"]
    + CSS Selector: button[type="submit"]


