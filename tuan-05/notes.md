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

1. **Với ô tên đăng nhập ở trang /login, nên xác định bằng cách nào là ổn định nhất, vì sao?**
   - Cách xác định ổn định và tối ưu nhất là sử dụng thuộc tính ID thông qua bộ định vị By.ID với giá trị username.
   - Lý do: Thuộc tính id theo tiêu chuẩn HTML là định danh duy nhất của phần tử trên toàn bộ trang web. Trên trang /login, trường nhập tài khoản có id="username" rất rõ ràng. Định vị bằng id mang lại tốc độ thực thi nhanh nhất do trình duyệt có cơ chế tối ưu riêng, đồng thời có tính bền vững cao nhất vì không bị ảnh hưởng nếu cấu trúc phân cấp thẻ bọc ngoài hoặc kiểu dáng CSS của giao diện thay đổi.

2. **Muốn nhập chữ vào một ô thì dùng lệnh gì?**
   - Muốn nhập chữ vào một ô nhập liệu trên trang web, ta sử dụng phương thức send_keys trên phần tử đã định vị được.
   - Cú pháp thực hiện: gọi phương thức send_keys trên phần tử và truyền vào chuỗi nội dung cần nhập. Ví dụ trong bài kiểm thử: username_field gọi send_keys với giá trị USERNAME. Trước khi nhập dữ liệu mới, nếu ô nhập đã có sẵn giá trị mặc định thì có thể gọi thêm phương thức clear để xóa sạch nội dung cũ.

3. **Làm thế nào để biết id của một ô nhập trên trang?**
   - Bước 1: Mở công cụ DevTools trên trình duyệt Chrome bằng cách nhấn phím F12 hoặc bấm chuột phải vào trang web rồi chọn mục Inspect hay Kiểm tra.
   - Bước 2: Bấm vào biểu tượng con trỏ chuột chọn phần tử ở góc trên bên trái cửa sổ DevTools hoặc dùng tổ hợp phím Ctrl + Shift + C.
   - Bước 3: Di chuyển chuột và nhấp trực tiếp vào ô nhập liệu cần kiểm tra trên màn hình trình duyệt.
   - Bước 4: Quan sát thẻ input đang được bôi đậm trong tab Elements của DevTools, tìm thuộc tính id và đọc giá trị nằm trong cặp dấu ngoặc kép sau id=, ví dụ id="username".

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

1. **Với ô tên đăng nhập ở trang /login, nên xác định bằng cách nào là ổn định nhất, vì sao?**
   - Xác định bằng By.ID với thuộc tính id="username" là phương án ổn định và an toàn nhất.
   - Lý do: Thuộc tính id là duy nhất trên trang, giúp WebDriver tìm kiếm trực tiếp và chính xác tuyệt đối mà không sợ nhầm lẫn với bất kỳ phần tử nào khác. So với XPath tương đối hay bộ chọn CSS, định vị theo id ít bị ảnh hưởng nhất khi giao diện web cập nhật thêm các thẻ cha bọc ngoài.

2. **Muốn nhập chữ vào một ô thì dùng lệnh gì?**
   - Để nhập chữ vào một ô nhập liệu, câu lệnh chuẩn trong Selenium WebDriver là phương thức send_keys.
   - Minh họa trong mã nguồn: tìm phần tử theo By.ID với giá trị username rồi gọi lệnh send_keys với chuỗi tomsmith. Lệnh này mô phỏng hành động gõ từng phím của người dùng vào ô đang được chọn.

3. **Làm thế nào để biết id của một ô nhập trên trang?**
   - Bước 1: Mở giao diện lập trình DevTools bằng cách nhấn F12 trên bàn phím.
   - Bước 2: Kích hoạt công cụ soi phần tử bằng cách bấm vào biểu tượng mũi tên góc trái tab Elements.
   - Bước 3: Nhấp chuột vào ô nhập tên đăng nhập trên form giao diện.
   - Bước 4: Nhìn vào đoạn mã HTML tương ứng được làm nổi bật trên cây cấu trúc DOM, tìm thuộc tính id="username" để lấy chính xác giá trị định danh của ô đó.

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

1. **Với ô tên đăng nhập ở trang /login, nên xác định bằng cách nào là ổn định nhất, vì sao?**
   - Nên dùng By.ID để xác định ô tên đăng nhập với giá trị là username.
   - Lý do: Thuộc tính id có tính độc nhất trong tài liệu HTML của trang. Khi dùng By.ID, thời gian tìm kiếm của trình duyệt là tức thời. Ngược lại, nếu dùng XPath hoặc CSS Selector phức tạp, script dễ bị sai khi cấu trúc phân cấp trang bị chỉnh sửa. Do đó id luôn là lựa chọn ưu tiên số một về độ ổn định.

2. **Muốn nhập chữ vào một ô thì dùng lệnh gì?**
   - Dùng phương thức send_keys truyền vào chuỗi ký tự muốn điền.
   - Ví dụ trong bài kiểm thử đăng nhập hợp lệ: gọi phương thức send_keys của biến username_field với giá trị USERNAME. Lệnh này sẽ truyền văn bản tài khoản tomsmith vào ô nhập liệu đã được định vị trước đó.

3. **Làm thế nào để biết id của một ô nhập trên trang?**
   - Bước 1: Mở trình duyệt Chrome tại trang đăng nhập, nhấn phím F12 để mở bảng điều khiển DevTools.
   - Bước 2: Nhấn vào biểu tượng trỏ phần tử ở góc trên bên trái DevTools.
   - Bước 3: Di chuột tới ô nhập và nhấn chuột trái.
   - Bước 4: Tại cửa sổ Elements, xem dòng mã nguồn thẻ input, quan sát thuộc tính id để lấy chuỗi định danh được đặt bên trong dấu nháy kép.

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

1. **Với ô tên đăng nhập ở trang /login, nên xác định bằng cách nào là ổn định nhất, vì sao?**
   - Xác định bằng By.ID với thuộc tính id="username" là phương án ổn định nhất.
   - Lý do: Thuộc tính id được gắn duy nhất cho phần tử này trên trang web. Sử dụng id giúp script chạy nhanh, định vị chuẩn xác và không bị gãy khi lập trình viên cập nhật lại các thuộc tính kiểu dáng như class hay thay đổi vị trí của phần tử trong cây DOM.

2. **Muốn nhập chữ vào một ô thì dùng lệnh gì?**
   - Lệnh được dùng là phương thức send_keys của phần tử Selenium WebElement.
   - Ví dụ áp dụng: gọi phương thức send_keys của biến password_field với chuỗi WrongPassword123!. Câu lệnh này sẽ đưa chuỗi mật khẩu sai vào trường nhập mật khẩu để kiểm thử kịch bản đăng nhập thất bại.

3. **Làm thế nào để biết id của một ô nhập trên trang?**
   - Bước 1: Nhấp chuột phải trực tiếp vào ô nhập liệu cần xem rồi chọn mục Kiểm tra hoặc Inspect trên menu ngữ cảnh.
   - Bước 2: Cửa sổ DevTools tự động mở ra và nhảy thẳng tới dòng mã HTML đại diện cho ô nhập đó.
   - Bước 3: Đọc thuộc tính id hiển thị trong thẻ input, giá trị của thuộc tính này chính là id cần tìm để đưa vào mã kiểm thử.

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

1. **Với ô tên đăng nhập ở trang /login, nên xác định bằng cách nào là ổn định nhất, vì sao?**
   - Nên xác định bằng cách dùng thuộc tính ID với bộ chọn By.ID giá trị username.
   - Lý do: ID luôn là bộ định vị có độ ưu tiên cao nhất trong kiểm thử tự động vì tính duy nhất trên toàn trang HTML. Việc dùng ID giúp tốc độ tìm kiếm của WebDriver đạt mức nhanh nhất và bài kiểm thử hoạt động ổn định nhất, không bị phụ thuộc vào các đường dẫn cấu trúc phức tạp như XPath.

2. **Muốn nhập chữ vào một ô thì dùng lệnh gì?**
   - Lệnh dùng để nhập chữ vào một ô là phương thức send_keys.
   - Ví dụ trong mã nguồn: gọi phương thức send_keys của biến username_field với giá trị invalid_username. Lệnh này sẽ mô phỏng việc gõ chuỗi tên người dùng không tồn tại vào ô tài khoản.

3. **Làm thế nào để biết id của một ô nhập trên trang?**
   - Bước 1: Bấm phím F12 để mở công cụ DevTools của trình duyệt Chrome.
   - Bước 2: Bấm vào nút có biểu tượng mũi tên chọn phần tử ở góc trên bên trái khung DevTools.
   - Bước 3: Bấm chuột vào ô nhập liệu cần kiểm tra trên giao diện trang web.
   - Bước 4: Xem đoạn mã HTML tương ứng trong cây phần tử ở tab Elements, tìm từ khóa id và lấy giá trị nằm sau dấu bằng.

### Ghi chú sử dụng AI
- Câu hỏi đã hỏi AI: Làm cách nào để script tự động tạo thư mục ảnh nếu thư mục đó chưa tồn tại nhằm tránh lỗi đường dẫn khi lưu ảnh màn hình?
- Tóm tắt câu trả lời: AI hướng dẫn dùng hàm os.makedirs kết hợp tham số exist_ok bằng True để tạo thư mục một cách an toàn.
- Đánh giá câu trả lời: Giải pháp ngắn gọn, an toàn và tương thích tốt trên các hệ điều hành khác nhau.
- Điều hiểu thêm: Việc xử lý đường dẫn tệp tin bằng thư viện chuẩn giúp mã kiểm thử chạy ổn định trên mọi môi trường máy tính của các thành viên.
