# Ghi chú tuần 05 – Kiểm thử tự động form Đăng nhập với Selenium và Pytest

Nhóm C06-N08

---

## 1. Phùng Dũng - Nhóm trưởng

### Điều đã học
- Nắm vững cách thiết kế cấu trúc test harness trong Pytest bằng việc sử dụng fixture kết hợp từ khóa yield cho chu trình khởi tạo và dọn dẹp của WebDriver.
- Hiểu rõ tầm quan trọng của việc tự động hóa dọn dẹp trình duyệt sau lệnh yield, đảm bảo lệnh đóng trình duyệt luôn được thực thi kể cả khi bài kiểm thử phát sinh lỗi, tránh rò rỉ các tiến trình chạy ngầm chiếm bộ nhớ máy tính.
- Nắm được quy trình tổng hợp mã nguồn, đánh giá và tích hợp các nhánh tính năng của các thành viên vào nhánh chung week-05.
- Thực thi toàn bộ bộ kiểm thử gồm 3 ca đăng nhập thành công bằng công cụ pytest.

### Trả lời câu hỏi đọc tài liệu:

1. **Một script Selenium gồm những bước nào, và mỗi bước ứng với dòng nào trong bài kiểm thử của bạn?**
   Theo tài liệu chuẩn Write your first Selenium script, một kịch bản kiểm thử Selenium gồm 8 bước cơ bản:
   - Bước 1: Khởi tạo phiên làm việc với trình duyệt WebDriver. Trong bài kiểm thử, bước này ứng với dòng 24 đến dòng 26 trong fixture driver, khởi tạo trình duyệt Chrome và mở rộng toàn màn hình.
   - Bước 2: Điều hướng đến trang web mục tiêu. Bước này ứng với dòng 42, sử dụng phương thức get để mở trang đăng nhập LOGIN_URL.
   - Bước 3: Định vị các phần tử giao diện trên trang web. Bước này ứng với dòng 45 đến dòng 47 tìm ô tên đăng nhập, dòng 50 tìm ô mật khẩu, dòng 53 tìm nút đăng nhập.
   - Bước 4: Thiết lập chiến lược chờ đợi phần tử sẵn sàng. Bước này ứng với dòng 39 khai báo đối tượng WebDriverWait, cùng các dòng 45 đến 47, dòng 65 và dòng 75 đến 77 chờ phần tử hiển thị hoặc URL thay đổi.
   - Bước 5: Thao tác tương tác với phần tử. Bước này ứng với dòng 56 điền tên đăng nhập, dòng 59 điền mật khẩu, dòng 62 nhấn chuột vào nút đăng nhập.
   - Bước 6: Lấy thông tin trạng thái từ trang web. Bước này ứng với dòng 68 lấy địa chỉ URL hiện tại của trình duyệt, dòng 79 đến dòng 80 đọc nội dung văn bản của thông báo flash.
   - Bước 7: Kiểm tra kết quả thực tế với kết quả mong đợi. Bước này ứng với dòng 69 đến dòng 72 kiểm tra URL chuyển hướng sang secure, dòng 83 đến dòng 85 kiểm tra thông báo đăng nhập thành công bằng câu lệnh assert.
   - Bước 8: Đóng phiên làm việc và giải phóng tài nguyên trình duyệt. Bước này ứng với dòng 28 trong fixture driver, tự động gọi lệnh quit sau khi hoàn thành ca kiểm thử.

2. **pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?**
   pytest tự động khám phá các bài kiểm thử trong dự án dựa trên 3 quy tắc đặt tên chuẩn sau:
   - Tên tệp kiểm thử: Phải bắt đầu bằng tiền tố test_ hoặc kết thúc bằng hậu tố _test.py. Ví dụ trong bài là tệp test_login.py.
   - Tên lớp kiểm thử: Nếu gom nhóm bằng lớp thì tên lớp phải bắt đầu bằng từ khóa Test và lớp đó không được chứa hàm khởi tạo init.
   - Tên hàm kiểm thử: Các hàm kiểm thử bên ngoài hoặc bên trong lớp phải luôn bắt đầu bằng tiền tố test_, ví dụ hàm test_login_valid_credentials, hàm test_login_invalid_password, hàm test_login_invalid_username.

### Ghi chú sử dụng AI
- Câu hỏi đã hỏi AI: Làm thế nào để viết một fixture Pytest chuẩn quản lý việc mở và đóng trình duyệt Chrome cho cả 3 ca kiểm thử đăng nhập?
- Tóm tắt câu trả lời: AI hướng dẫn định nghĩa hàm fixture với từ khóa yield, phần trước yield thực hiện khởi tạo trình duyệt, phần sau yield gọi phương thức quit để dọn dẹp tài nguyên.
- Đánh giá câu trả lời: Đoạn mã gợi ý chuẩn xác theo mô hình của Pytest, giúp loại bỏ các khối lệnh xử lý ngoại lệ lặp lại ở từng bài kiểm thử.
- Điều hiểu thêm: Quản lý fixture giúp các bài kiểm thử độc lập hoàn toàn với nhau, bài kiểm thử phía trước không làm ảnh hưởng đến bài kiểm thử phía sau.

---

## 2. Ngô Quyết Thắng

### Điều đã học
- Nắm được quy trình phân tích và xây dựng tài liệu đặc tả kiểm thử testcases.md trước khi bắt tay vào viết mã kiểm thử tự động.
- Biết cách sử dụng công cụ DevTools trên Chrome để soi cây cấu trúc trang web, xác định các thuộc tính như id, name, type để tạo bộ định vị phần tử.
- Hiểu được sự khác biệt giữa các kiểu định vị phổ biến gồm thuộc tính id, bộ chọn CSS Selector và đường dẫn XPath.
- Nắm được cách thiết lập kết quả kỳ vọng cho cả trường hợp đăng nhập đúng và các trường hợp nhập sai hoặc bỏ trống.

### Trả lời câu hỏi đọc tài liệu:

1. **Một script Selenium gồm những bước nào, và mỗi bước ứng với dòng nào trong bài kiểm thử của bạn?**
   Dựa trên tài liệu hướng dẫn viết script Selenium đầu tiên, kịch bản gồm 8 bước được ánh xạ vào bài kiểm thử trong tệp test_login.py:
   - Bước 1: Khởi tạo phiên trình duyệt WebDriver, ứng với dòng 24 đến dòng 26 của fixture driver.
   - Bước 2: Truy cập trang web cần kiểm thử, ứng với dòng 42 mở địa chỉ trang đăng nhập.
   - Bước 3: Định vị các phần tử form trên trang, ứng với dòng 45 đến 47 tìm trường username theo id, dòng 50 tìm trường password theo id, dòng 53 tìm nút submit bằng CSS Selector button[type='submit'].
   - Bước 4: Chờ phần tử sẵn sàng tương tác, ứng với dòng 39 thiết lập thời gian chờ tối đa 10 giây, dòng 46 chờ ô nhập liệu xuất hiện.
   - Bước 5: Thực hiện các hành động nhập và bấm nút, ứng với dòng 56 điền tài khoản, dòng 59 điền mật khẩu, dòng 62 kích hoạt sự kiện bấm nút đăng nhập.
   - Bước 6: Trích xuất dữ liệu thực tế sau tương tác, ứng với dòng 68 lấy URL sau chuyển hướng và dòng 80 lấy nội dung phản hồi từ thông báo flash.
   - Bước 7: Khẳng định tính chính xác của kết quả, ứng với các dòng lệnh assert từ dòng 69 đến 72 và dòng 83 đến 85 so sánh dữ liệu thực tế với kết quả mong đợi.
   - Bước 8: Kết thúc phiên làm việc của trình duyệt, ứng với dòng 28 gọi lệnh quit để đóng cửa sổ Chrome.

2. **pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?**
   pytest nhận diện bài kiểm thử một cách tự động khi tuân thủ đúng quy ước đặt tên:
   - Tệp mã nguồn kiểm thử: Bắt đầu bằng test_ như test_login.py hoặc kết thúc bằng _test.py.
   - Lớp kiểm thử: Bắt đầu bằng chữ Test viết hoa chữ T đầu tiên và không có hàm khởi tạo init.
   - Hàm kiểm thử: Phải bắt đầu bằng tiền tố test_ viết thường, ví dụ test_login_valid_credentials hoặc test_login_invalid_password. Mọi hàm không bắt đầu bằng tiền tố này sẽ bị pytest bỏ qua.

### Ghi chú sử dụng AI
- Câu hỏi đã hỏi AI: Hướng dẫn viết bảng đặc tả trường hợp kiểm thử cho form đăng nhập và so sánh độ ổn định giữa bộ chọn CSS Selector và đường dẫn XPath tương đối.
- Tóm tắt câu trả lời: AI phân tích cấu trúc bảng kiểm thử gồm mục tiêu, các bước thực hiện, dữ liệu thử nghiệm và kết quả kỳ vọng; đồng thời khuyên dùng CSS Selector cho nút submit vì cú pháp ngắn gọn và tốc độ tối ưu trên trình duyệt.
- Đánh giá câu trả lời: Câu trả lời rất hữu ích, giúp nhóm hoàn thiện tệp testcases.md một cách khoa học.
- Điều hiểu thêm: Tránh sử dụng đường dẫn XPath tuyệt đối vì cấu trúc trang web rất dễ thay đổi làm gãy bài kiểm thử.

---

## 3. Nguyễn Tiến Dũng

### Điều đã học
- Thực hành triển khai bài kiểm thử tự động cho trường hợp đăng nhập thành công với tài khoản và mật khẩu hợp lệ trong hàm test_login_valid_credentials.
- Sử dụng phương thức send_keys để đưa dữ liệu vào các ô nhập liệu và phương thức click để gửi biểu mẫu đăng nhập.
- Áp dụng kỹ thuật chờ tường minh WebDriverWait kết hợp điều kiện url_contains để kiểm tra việc trang web chuyển hướng sang khu vực an toàn secure.
- Kiểm tra nội dung thông báo thành công và lưu ảnh chụp màn hình chứng minh kết quả vào thư mục anh.

### Trả lời câu hỏi đọc tài liệu:

1. **Một script Selenium gồm những bước nào, và mỗi bước ứng với dòng nào trong bài kiểm thử của bạn?**
   Theo tài liệu Write your first Selenium script, bài kiểm thử đăng nhập hợp lệ test_login_valid_credentials thực hiện đầy đủ 8 bước sau:
   - Bước 1: Khởi tạo trình duyệt WebDriver, được thiết lập tại dòng 24 đến dòng 26 trong fixture driver chung của tệp.
   - Bước 2: Điều hướng đến trang web mục tiêu, ứng với dòng 42 gọi lệnh driver.get mở trang đăng nhập.
   - Bước 3: Định vị phần tử trên trang, ứng với dòng 45 đến 47 định vị ô nhập tên đăng nhập bằng ID username, dòng 50 định vị ô mật khẩu bằng ID password, dòng 53 định vị nút đăng nhập bằng CSS Selector.
   - Bước 4: Thiết lập chiến lược chờ đợi, ứng với dòng 39 tạo bộ chờ WebDriverWait 10 giây, dòng 46 chờ ô username hiển thị, dòng 65 chờ URL chứa đường dẫn secure, dòng 76 chờ thông báo flash xuất hiện.
   - Bước 5: Thực hiện thao tác người dùng, ứng với dòng 56 điền tên đăng nhập tomsmith, dòng 59 điền mật khẩu hợp lệ, dòng 62 bấm nút gửi form đăng nhập.
   - Bước 6: Lấy thông tin phản hồi từ giao diện, ứng với dòng 68 đọc đường dẫn URL hiện tại và dòng 80 lấy chuỗi văn bản của thông báo flash.
   - Bước 7: Kiểm tra kết quả thực tế với mong đợi, ứng với dòng 69 đến 72 assert URL chứa chuỗi secure, dòng 83 đến 85 assert thông báo flash chứa nội dung đăng nhập thành công.
   - Bước 8: Kết thúc phiên làm việc, ứng với dòng 28 đóng trình duyệt Chrome sau khi hoàn thành bài test.

2. **pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?**
   Cơ chế tìm kiếm tự động của pytest dựa trên các tiền tố và hậu tố quy ước:
   - Tên file: Bắt đầu bằng test_ hoặc kết thúc bằng _test.py. Trong dự án, tệp chứa mã kiểm thử được đặt tên là test_login.py nên pytest tự động quét được.
   - Tên class: Bắt đầu bằng Test nếu tổ chức bài kiểm thử theo hướng đối tượng.
   - Tên function: Bắt đầu bằng chữ test_ viết thường. Ví dụ bài kiểm thử đăng nhập thành công được đặt tên là test_login_valid_credentials, giúp pytest nhận diện chính xác đây là một bài kiểm thử cần chạy.

### Ghi chú sử dụng AI
- Câu hỏi đã hỏi AI: Tại sao khi kiểm tra chuyển hướng sau khi đăng nhập cần dùng WebDriverWait chờ URL thay đổi mà không nên đọc ngay thuộc tính current_url?
- Tóm tắt câu trả lời: AI giải thích rằng sau khi nhấn nút đăng nhập, trình duyệt cần thời gian gửi yêu cầu lên máy chủ và tải trang mới. Nếu đọc current_url ngay lập tức, kết quả có thể vẫn là URL cũ dẫn đến bài kiểm thử thất bại sai lệch.
- Đánh giá câu trả lời: Giải thích rất chính xác về bản chất xử lý bất đồng bộ của ứng dụng web.
- Điều hiểu thêm: Luôn kết hợp WebDriverWait với các điều kiện trạng thái trang để bài kiểm thử chạy ổn định nhất.

---

## 4. Lê Thị Nga

### Điều đã học
- Thực hành triển khai bài kiểm thử tự động cho trường hợp nhập sai mật khẩu trong hàm test_login_invalid_password.
- Biết cách thiết kế dữ liệu kiểm thử phủ định, giữ nguyên tên người dùng hợp lệ và đưa vào chuỗi mật khẩu sai để kiểm tra phản ứng của hệ thống.
- Sử dụng câu lệnh assert để xác thực thông báo từ chối truy cập và nội dung cảnh báo hiển thị trên màn hình.
- Thêm chú thích giải thích chi tiết các bước xử lý và chụp ảnh lưu minh chứng thực thi vào tệp nga.png.

### Trả lời câu hỏi đọc tài liệu:

1. **Một script Selenium gồm những bước nào, và mỗi bước ứng với dòng nào trong bài kiểm thử của bạn?**
   Theo tài liệu Write your first Selenium script, bài kiểm thử trường hợp sai mật khẩu test_login_invalid_password gồm 8 bước cụ thể:
   - Bước 1: Khởi tạo phiên làm việc WebDriver, ứng với dòng 24 đến dòng 26 trong fixture driver dùng chung.
   - Bước 2: Điều hướng tới trang web kiểm thử, ứng với dòng 108 gọi lệnh mở địa chỉ URL trang đăng nhập.
   - Bước 3: Định vị các trường dữ liệu và nút bấm, ứng với dòng 111 tìm trường tên đăng nhập, dòng 112 tìm trường mật khẩu, dòng 113 tìm nút bấm submit.
   - Bước 4: Thiết lập cơ chế chờ đợi, ứng với dòng 105 khởi tạo bộ chờ 10 giây, dòng 111 chờ ô tên đăng nhập sẵn sàng hiển thị, dòng 123 chờ thông báo lỗi flash xuất hiện.
   - Bước 5: Thực hiện nhập liệu và gửi biểu mẫu, ứng với dòng 116 nhập tên đăng nhập tomsmith, dòng 117 nhập mật khẩu sai WrongPassword123!, dòng 120 nhấn nút đăng nhập.
   - Bước 6: Lấy thông tin phản hồi từ trang web, ứng với dòng 124 trích xuất văn bản từ thông báo lỗi flash.
   - Bước 7: Kiểm tra khẳng định kết quả mong đợi, ứng với dòng 127 đến dòng 129 dùng assert xác nhận thông báo lỗi chứa đoạn văn bản Your password is invalid!.
   - Bước 8: Kết thúc phiên làm việc, ứng với dòng 28 đóng trình duyệt và dọn dẹp bộ nhớ máy tính.

2. **pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?**
   pytest áp dụng quy tắc đặt tên nhất quán để khám phá các bài kiểm thử:
   - Quy tắc đặt tên file: Tệp phải có tên bắt đầu bằng test_ hoặc có đuôi là _test.py.
   - Quy tắc đặt tên class: Lớp chứa bài kiểm thử phải có tên bắt đầu bằng Test và không sử dụng hàm khởi tạo init.
   - Quy tắc đặt tên hàm: Hàm thực thi kiểm thử phải bắt đầu bằng chữ test_, ví dụ hàm test_login_invalid_password. Nhờ tiền tố test_ này, khi gọi lệnh pytest từ dòng lệnh, công cụ sẽ tự động nạp và thực thi hàm này.

### Ghi chú sử dụng AI
- Câu hỏi đã hỏi AI: Làm cách nào để kiểm tra thông báo lỗi hiển thị trong thẻ flash khi thẻ này chứa cả ký tự nút đóng thông báo?
- Tóm tắt câu trả lời: AI hướng dẫn sử dụng toán tử in của ngôn ngữ Python để kiểm tra chuỗi thông báo cốt lõi nằm trong văn bản trích xuất được, thay vì dùng phép so sánh bằng tuyệt đối.
- Đánh giá câu trả lời: Cách tiếp cận rất thực tế, giúp bài kiểm thử không bị lỗi do các ký tự đặc biệt xung quanh thông báo.
- Điều hiểu thêm: Cần hiểu rõ cấu trúc cây phần tử HTML để đưa ra câu lệnh kiểm tra kết quả vừa chặt chẽ vừa bền vững.

---

## 5. Nguyễn Phúc Hưng

### Điều đã học
- Thực hành xây dựng bài kiểm thử cho trường hợp người dùng nhập tên đăng nhập không tồn tại trong hệ thống qua hàm test_login_invalid_username.
- Nắm được cách định vị nút gửi biểu mẫu bằng CSS Selector và kích hoạt hành vi nhấn chuột.
- Khẳng định hệ thống từ chối đăng nhập và trả về thông báo lỗi chính xác theo yêu cầu.
- Tự động hóa quá trình chụp ảnh bằng chứng màn hình và lưu trữ vào thư mục ảnh phục vụ báo cáo.

### Trả lời câu hỏi đọc tài liệu:

1. **Một script Selenium gồm những bước nào, và mỗi bước ứng với dòng nào trong bài kiểm thử của bạn?**
   Theo hướng dẫn chuẩn Write your first Selenium script, bài kiểm thử sai tên đăng nhập test_login_invalid_username được cấu thành từ 8 bước sau:
   - Bước 1: Khởi tạo phiên làm việc với trình duyệt WebDriver, ứng với dòng 24 đến dòng 26 trong fixture driver.
   - Bước 2: Điều hướng đến trang web mục tiêu, ứng với dòng 154 mở trang đăng nhập bằng lệnh driver.get.
   - Bước 3: Định vị các phần tử trên trang, ứng với dòng 157 đến 159 định vị ô tên đăng nhập, dòng 162 định vị ô mật khẩu, dòng 165 đến 167 định vị nút đăng nhập bằng CSS Selector.
   - Bước 4: Thiết lập chiến lược chờ đợi phần tử, ứng với dòng 147 tạo WebDriverWait, dòng 158 chờ ô nhập tên xuất hiện, dòng 179 đến 181 chờ thông báo lỗi xuất hiện trên màn hình.
   - Bước 5: Thao tác gửi dữ liệu và gửi biểu mẫu, ứng với dòng 170 điền tên người dùng không tồn tại, dòng 173 điền mật khẩu bất kỳ, dòng 176 nhấn nút đăng nhập.
   - Bước 6: Lấy thông tin phản hồi, ứng với dòng 184 đọc văn bản từ thẻ thông báo flash.
   - Bước 7: Khẳng định tính đúng đắn của kết quả, ứng với dòng 187 đến dòng 189 kiểm tra thông báo lỗi có chứa chuỗi Your username is invalid! bằng assert.
   - Bước 8: Kết thúc phiên làm việc, ứng với dòng 28 tự động giải phóng trình duyệt và tiến trình liên quan.

2. **pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?**
   pytest nhận biết và thu thập các bài kiểm thử thông qua các chuẩn đặt tên sau:
   - Chuẩn đặt tên file: Bắt đầu bằng test_ hoặc kết thúc bằng _test.py, chẳng hạn tệp test_login.py.
   - Chuẩn đặt tên class: Lớp nhóm bài kiểm thử bắt đầu bằng Test và không định nghĩa hàm init.
   - Chuẩn đặt tên hàm: Hàm bài kiểm thử bắt buộc phải bắt đầu bằng test_, chẳng hạn hàm test_login_invalid_username. Nếu đặt tên không có tiền tố này, pytest sẽ xem như hàm trợ giúp thông thường và bỏ qua không thực thi.

### Ghi chú sử dụng AI
- Câu hỏi đã hỏi AI: Làm cách nào để script tự động tạo thư mục ảnh nếu thư mục đó chưa tồn tại nhằm tránh lỗi đường dẫn khi lưu ảnh màn hình?
- Tóm tắt câu trả lời: AI hướng dẫn dùng hàm os.makedirs kết hợp tham số exist_ok bằng True để tạo thư mục một cách an toàn.
- Đánh giá câu trả lời: Giải pháp ngắn gọn, an toàn và tương thích tốt trên các hệ điều hành khác nhau.
- Điều hiểu thêm: Việc xử lý đường dẫn tệp tin bằng thư viện chuẩn giúp mã kiểm thử chạy ổn định trên mọi môi trường máy tính của các thành viên.
