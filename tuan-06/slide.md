# Slide Draft & Opening Script - Week 06

## 1. Slide Draft (Slides 1 - 3)
1. Tự động kiểm thử là gì? ROI là gì?
1.1. Tự động kiểm thử (Test Automation) là gì?
Tự động kiểm thử (Test Automation) là quá trình sử dụng phần mềm, công cụ hoặc các đoạn mã để thực hiện các bước kiểm thử, so sánh kết quả thực tế với kết quả mong đợi và đưa ra kết quả đạt hoặc không đạt mà không cần con người thực hiện thủ công toàn bộ các bước.

Ví dụ: Kiểm thử chức năng đăng nhập của một website bán hàng.
- Kiểm thử thủ công: Người kiểm thử mở website, nhập tài khoản và mật khẩu, nhấn nút đăng nhập rồi quan sát kết quả.
- Kiểm thử tự động: Viết chương trình sử dụng Selenium hoặc Playwright để tự động mở website, nhập thông tin, nhấn nút đăng nhập và kiểm tra xem người dùng có đăng nhập thành công hay không.
Quy trình kiểm thử tự động
1. Chuẩn bị dữ liệu kiểm thử
Ví dụ: tài khoản và mật khẩu hợp lệ
2. Chương trình tự động thực hiện
Mở website → nhập dữ liệu → nhấn đăng nhập
3. Kiểm tra kết quả thực tế
-> Có chuyển đến trang chủ như mong đợi không?
** PASS
    Kết quả đúng mong đợi
**FAIL
    Kết quả không đúng mong đợi
1.2. Mục đích của tự động kiểm thử
Tự động kiểm thử được sử dụng để:
1. Tiết kiệm thời gian: Chạy nhiều test case nhanh hơn khi phải kiểm tra đi kiểm tra lại.
2. Giảm thao tác thủ công: Hạn chế những sai sót do con người nhập liệu hoặc thực hiện không nhất quán.
3. Tăng khả năng kiểm thử hồi quy (Regression Testing): Kiểm tra xem các chức năng cũ có bị lỗi sau khi cập nhật phần mềm hay không.
4. Tăng độ bao phủ kiểm thử: Có thể chạy nhiều bộ dữ liệu và trường hợp kiểm thử.
5. Hỗ trợ tích hợp liên tục (CI/CD): Tự động chạy kiểm thử mỗi khi lập trình viên cập nhật mã nguồn.
6. Phát hiện lỗi sớm: Giúp nhóm phát triển phát hiện vấn đề trước khi phần mềm được đưa đến người dùng.
1.3. Ưu điểm và nhược điểm
            Ưu điểm                                                 Nhược điểm
Chạy kiểm thử nhanh khi lặp lại nhiều lần   	Tốn thời gian và chi phí xây dựng ban đầu
Có thể chạy nhiều lần với kết quả nhất quán 	Cần bảo trì khi phần mềm thay đổi
Giảm công sức kiểm thử thủ công             	Có thể phát sinh kết quả sai do script hoặc môi trường
Hỗ trợ kiểm thử hồi quy và CI/CD               	Không thay thế hoàn toàn khả năng đánh giá của con người
Có thể kiểm thử trên nhiều bộ dữ liệu       	Cần người có kỹ năng viết và quản lý test script
-------------

1.4. ROI trong tự động kiểm thử là gì?
ROI (Return on Investment) là tỷ suất hoàn vốn hoặc tỷ suất lợi nhuận trên khoản đầu tư. Trong kiểm thử phần mềm, ROI giúp đánh giá liệu chi phí đầu tư vào tự động hóa có mang lại lợi ích kinh tế tương xứng hay không.

ROI thường được đánh giá dựa trên việc so sánh chi phí xây dựng, vận hành và bảo trì kiểm thử tự động với chi phí có thể tiết kiệm được so với kiểm thử thủ công.

Công thức tổng quát:
(lợi ích - Chi phí đầu tư)/chi phí đầu tư x 100%
Trong đó:
- Lợi ích: Giá trị tiết kiệm được nhờ tự động hóa, chẳng hạn chi phí nhân công kiểm thử giảm.
- Chi phí đầu tư: Chi phí xây dựng script, công cụ, hạ tầng, vận hành và bảo trì.
Ví dụ tính ROI
** Một nhóm phát triển quyết định tự động hóa bộ kiểm thử hồi quy.
        Khoản mục	                                Chi phí
Xây dựng test script ban đầu	                10 triệu đồng
Công cụ và hạ tầng	                            2 triệu đồng
Bảo trì trong kỳ đánh giá	                    3 triệu đồng
Tổng chi phí đầu tư	                            15 triệu đồng
Giá trị tiết kiệm được so với kiểm thử thủ công	24 triệu đồng

Áp dụng công thức:
-- ROI = (24-15)/15 x 100% = 60%
Kết quả: ROI bằng 60%. Theo các giả định trên, lợi ích ròng là 9 triệu đồng, tương đương 60% tổng chi phí đầu tư.

-- Lưu ý, con số tiết kiệm 24 triệu đồng phải được tính sau khi đã xác định rõ phần chi phí kiểm thử thủ công được tránh hoặc tiết kiệm; không nên tính trùng các khoản chi phí.
Khi nào ROI của tự động kiểm thử cao?
- Chức năng được kiểm thử thường xuyên.
- Bộ test case ổn định và có thể tái sử dụng.
- Số lượng test case lớn.
- Dự án có nhiều lần phát hành phần mềm.
- Kiểm thử thủ công mất nhiều thời gian và chi phí.
Khi nào ROI thấp?
- Chức năng chỉ được kiểm thử một vài lần.
- Giao diện thay đổi liên tục.
- Chi phí xây dựng và bảo trì script cao.
- Kiểm thử thủ công vốn đã nhanh, đơn giản và ít tốn kém.
Kết luận: Không phải cứ tự động hóa càng nhiều thì ROI càng cao. Cần lựa chọn đúng loại kiểm thử và những chức năng có khả năng tái sử dụng để tối ưu chi phí.
### Slide 2: Khi nào không nên tự động hóa kiểm thử giao diện người dùng (UI Testing)?
2. Khi nào không nên tự động hóa kiểm thử giao diện người dùng (UI Testing)?
2.1. Kiểm thử giao diện người dùng là gì?
UI Testing (User Interface Testing) là quá trình kiểm tra giao diện mà người dùng trực tiếp tương tác, bao gồm các nút bấm, ô nhập liệu, menu, biểu mẫu, hình ảnh, bố cục và cách các thành phần hiển thị trên màn hình.

Ví dụ: Với trang đăng nhập, kiểm thử UI có thể kiểm tra:
- Ô nhập tên đăng nhập và mật khẩu có hiển thị không.
- Nút Đăng nhập có hoạt động khi được nhấn không.
- Thông báo lỗi có xuất hiện khi nhập sai mật khẩu không.
- Giao diện có hiển thị đúng trên máy tính và điện thoại không.

Trường hợp          	        Lý do không nên tự động hóa ngay	    Hướng xử lý
UI thay đổi liên tục	        Script dễ bị lỗi, tốn công sửa	    Kiểm thử thủ công trước, tự động hóa khi ổn định
Prototype chưa hoàn thiện	    Có thể phải viết lại toàn bộ	    Ưu tiên kiểm tra thiết kế và yêu cầu
Đánh giá UX, cảm xúc	        Máy khó thay thế đánh giá của 	    Thử nghiệm với người dùng thật                            con người
Chức năng đơn giản, ít lặp lại	Lợi ích thấp hơn chi phí	        Kiểm thử thủ công
Giao diện động, thiếu ổn định	Dễ phát sinh flaky test	            Ổn định dữ liệu và bộ chọn trước
ROI thấp	                    Không hiệu quả về kinh tế	        Chọn chức năng khác có tần suất cao hơn
### Slide 3: Phân tích cấu trúc kim tự tháp bài kiểm tra thực hành
3.1. Khái niệm
- Kim tự tháp kiểm thử (Test Pyramid) là mô hình mô tả cách phân bổ số lượng bài kiểm thử ở các cấp độ khác nhau trong quá trình phát triển phần mềm. Mô hình khuyến khích thực hiện nhiều kiểm thử ở tầng thấp, ít kiểm thử ở tầng cao nhằm phát hiện lỗi sớm, giảm chi phí và tăng hiệu quả kiểm thử.
3.2. Cấu trúc kim tự tháp kiểm thử
- Tầng 1: Unit Testing (Kiểm thử đơn vị)
Đây là tầng đáy của kim tự tháp, bao gồm nhiều bài kiểm thử nhất. Unit Testing kiểm tra các thành phần nhỏ của chương trình như hàm, phương thức hoặc lớp. Các bài kiểm thử này thường có tốc độ chạy nhanh, chi phí thấp và dễ xác định nguyên nhân gây lỗi.
- Ví dụ: Kiểm tra hàm tính tổng tiền của đơn hàng có trả về kết quả chính xác hay không
- Tầng 2: Integration Testing/API Testing (Kiểm thử tích hợp/API)
Tầng giữa kiểm tra sự phối hợp giữa các thành phần hoặc khả năng giao tiếp giữa các hệ thống thông qua API. Các bài kiểm thử này giúp phát hiện lỗi trong quá trình trao đổi dữ liệu và tích hợp chức năng.
-Ví dụ: Kiểm tra API đăng nhập có xác thực tài khoản và trả về kết quả chính xác hay không.
-Tầng 3: UI Testing/End-to-End Testing (Kiểm thử giao diện/đầu-cuối)
Đây là tầng đỉnh của kim tự tháp, thường có số lượng bài kiểm thử ít nhất. Tầng này kiểm tra các chức năng thông qua giao diện người dùng hoặc toàn bộ quy trình nghiệp vụ. Tuy nhiên, các bài kiểm thử này thường chạy chậm và tốn nhiều công sức bảo trì hơn.
- Ví dụ: Mở website, nhập tài khoản và mật khẩu, nhấn nút đăng nhập rồi kiểm tra xem người dùng có được chuyển đến trang chủ hay không.
3.3. Ý nghĩa của kim tự tháp kiểm thử
Kim tự tháp kiểm thử giúp phân bổ nguồn lực hợp lý bằng cách ưu tiên các bài kiểm thử nhanh, ít tốn kém ở tầng thấp và chỉ sử dụng kiểm thử giao diện cho những luồng quan trọng.
Nếu có quá nhiều bài kiểm thử giao diện nhưng quá ít Unit Testing, bộ kiểm thử có thể chạy chậm, khó bảo trì và khó xác định nguyên nhân lỗi. Ngược lại, kết hợp hợp lý cả ba tầng sẽ giúp tăng độ tin cậy của phần mềm và giảm chi phí kiểm thử.