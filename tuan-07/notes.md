# Ghi chú tuần 07 – Báo cáo Kiểm thử tự động và Cơ chế Wait

Nhóm C06-N08

---

## 1. Phùng Dũng - Nhóm trưởng

### Điều đã học
- Trong tuần này, với vai trò Team Leader, em đã điều phối nhóm hoàn thành các Pull Request vào nhánh `week-07`, đồng thời tổ chức buổi họp nhóm (team meeting) để các thành viên giải thích chéo (cross-explain) mã nguồn của nhau.
- Em đã kéo nhánh `week-07` về máy để chạy tổng thể toàn bộ bộ kiểm thử (test suite), trực tiếp rà soát và đảm bảo không có mã nguồn nào sử dụng `time.sleep()`.
- Cuối cùng, em đã tạo Pull Request từ `week-07` sang `main`, xin phê duyệt từ thành viên và tiến hành merge mã nguồn thành công.

### Trả lời câu hỏi đọc tài liệu:

1. **Tại sao việc rà soát chéo mã nguồn (Code Review/Cross-explanation) và kiểm tra tập trung (Running Test Suite) lại quan trọng trước khi merge vào nhánh `main`?**
   - Quá trình này giúp đảm bảo tất cả các kịch bản kiểm thử riêng lẻ của các thành viên hoạt động trơn tru khi tích hợp chung, phát hiện sớm các xung đột mã nguồn (merge conflicts) hoặc vi phạm quy chuẩn (như dùng `time.sleep()`), đồng thời nâng cao sự hiểu biết đồng đều về toàn bộ hệ thống giữa các thành viên.

2. **Quy trình chuẩn để đưa mã nguồn từ nhánh phát triển tuần (`week-07`) vào nhánh chính (`main`) diễn ra như thế nào?**
   - Quy trình gồm 4 bước: (1) Đảm bảo tất cả các PR thành viên đã merge vào `week-07`; (2) Chạy kiểm thử lại toàn bộ hệ thống trên `week-07`; (3) Tạo Pull Request từ `week-07` vào `main`; (4) Yêu cầu ít nhất 1 thành viên review, approve và tiến hành Merge mã nguồn.

---

## 2. Nguyễn Phúc Hưng

### Điều đã học
- Trong tuần này, em đã học được cách xây dựng kịch bản kiểm thử cố tình kích hoạt lỗi (Negative Testing / Failure Case) để kiểm tra khả năng xử lý của hệ thống khi nhận dữ liệu đầu vào không hợp lệ.
- Bên cạnh đó, em đã làm quen và áp dụng thành thạo cơ chế Wait (Implicit Wait và Explicit Wait) để xử lý độ trễ tải trang bất đồng bộ.
- Việc hiểu rõ tác hại của lệnh cố định `time.sleep()` giúp em viết mã kiểm thử chuyên nghiệp, tối ưu thời gian thực thi và tránh các lỗi Flaky test không đáng có.

### Trả lời câu hỏi đọc tài liệu:

1. **Tại sao lại cần viết test case cố tình làm cho bài test thất bại (Failure test case / Negative testing)?**
   - Negative testing giúp đảm bảo ứng dụng không chỉ hoạt động đúng khi nhận dữ liệu chuẩn (Happy path) mà còn có khả năng phát hiện, xử lý lỗi mượt mà và hiển thị thông báo hợp lý khi người dùng nhập sai dữ liệu hoặc thực hiện thao tác bất hợp lệ.

2. **Phân biệt Explicit Wait và `time.sleep()`, tại sao tuyệt đối không dùng `time.sleep()` trong kiểm thử tự động?**
   - `time.sleep()` bắt chương trình dừng lại đúng số giây cố định dù trang web đã tải xong, gây lãng phí thời gian và làm giảm hiệu năng test runner. Ngược lại, **Explicit Wait** (`WebDriverWait`) sẽ liên tục kiểm tra điều kiện (ví dụ: phần tử xuất hiện hay có thể click) và tiếp tục thực thi ngay khi điều kiện thỏa mãn, giúp bài test vừa chạy nhanh vừa ổn định.

---

## 3. Nguyễn Tiến Dũng

### Điều đã học
- Trong tuần này, em đã nắm vững cách thiết kế kịch bản kiểm thử (Test Cases) chi tiết cho tính năng Hộp kiểm (Checkboxes) trên trang `/checkboxes`.
- Em đã phân biệt rõ ràng giữa kiểm thử tích cực (Positive testing - chọn/bỏ chọn checkbox) và kiểm thử tiêu cực (Negative testing - xác nhận trạng thái không được lưu sau khi tải lại trang F5).
- Đồng thời, em cũng đã biết cách lập bảng định vị phần tử (sử dụng ID, CSS Selector, XPath) làm cơ sở dữ liệu chuẩn bị cho việc viết mã tự động hóa ở tuần tiếp theo.

### Trả lời câu hỏi đọc tài liệu:

1. **Phân biệt kiểm thử tích cực (Positive Testing) và kiểm thử tiêu cực (Negative Testing) qua ví dụ kịch bản tính năng Checkbox?**
   - **Positive Testing** (ví dụ TC01, TC02): Kiểm tra xem hệ thống có hoạt động đúng theo luồng mong muốn hay không khi người dùng tương tác chuẩn (click đánh dấu hoặc bỏ chọn ô checkbox).
   - **Negative Testing** (ví dụ TC03): Kiểm tra cách hệ thống xử lý các tình huống ngoại lệ hoặc hành vi không mong muốn (ví dụ F5 tải lại trang để xác nhận trạng thái checkbox không bị lưu sai lệch).

2. **Tại sao cần lập bảng định vị phần tử (ID, CSS Selector, XPath) trước khi viết mã test tự động?**
   - Việc lập bảng định vị giúp người viết mã kiểm thử (Automation Tester) xác định chính xác phần tử UI cần tương tác trên trang web, tránh việc viết sai selector khiến kịch bản chạy bị lỗi `NoSuchElementException`, đồng thời giúp quản lý mã nguồn gọn gàng và dễ bảo trì hơn.

---

## 4. Ngô Quyết Thắng

### Điều đã học
- Trong tuần này, em đã nắm vững cách áp dụng cơ chế Wait (Implicit Wait và Explicit Wait) trong Selenium/Playwright để xử lý các phần tử tải chậm trên trang web.
- Bài học giúp em hiểu rõ tác hại của việc dùng lệnh cố định `time.sleep()`, gây tốn tài nguyên và dễ làm bài test thất bại vô lý.
- Ngoài ra, em cũng đã biết cách thiết lập quy trình kiểm thử tự động cho một kịch bản thành công (happy path) hoàn chỉnh.

### Trả lời câu hỏi đọc tài liệu:

1. **Sự khác biệt chính giữa Implicit Wait và Explicit Wait là gì? Khi nào nên sử dụng loại nào?**
   - **Implicit Wait** áp dụng cho toàn bộ các phần tử trong suốt chu kỳ sống của WebDriver với một khoảng thời gian chờ tối đa cố định.
   - **Explicit Wait** chỉ áp dụng cho một phần tử cụ thể với một điều kiện nhất định (như hiển thị, có thể click, v.v.).
   - Nên dùng Explicit Wait cho các phần tử bất đồng bộ hoặc tải chậm đặc thù để tối ưu thời gian chạy test.

2. **Tại sao nghiêm cấm sử dụng `time.sleep()` trong kiểm thử tự động chuyên nghiệp?**
   - Lệnh `time.sleep()` bắt chương trình dừng lại đúng số giây quy định cho dù trang web đã tải xong từ trước, gây lãng phí thời gian thực thi test suite.
   - Ngược lại, nếu mạng chậm hơn dự kiến, `time.sleep()` vẫn bị timeout dẫn đến test case thất bại vô lý (flaky test).
   ---

## 5. Lê Thị Nga

### Điều đã học
- Trong tuần này, em đã tiến hành thực nghiệm và trực tiếp so sánh hành vi thực thi của kịch bản kiểm thử khi CÓ và KHÔNG có sử dụng các cơ chế chờ (Wait mechanisms).
- Em đã nắm rõ cách nhận biết các lỗi phát sinh do bất đồng bộ tốc độ giữa WebDriver và phản hồi của trang web (trang chưa tải kịp phần tử nhưng code đã vội tìm kiếm).
- Hiểu được tầm quan trọng của việc cấu hình thời gian chờ thông minh để giúp bộ test suite vận hành ổn định, chính xác trên các môi trường mạng khác nhau.

### Trả lời câu hỏi đọc tài liệu:

1. **Nêu rõ các quan sát từ thí nghiệm KHÔNG có lệnh chờ (Wait)?**
   - **Hiện tượng:** Kịch bản kiểm thử bị dừng đột ngột và báo lỗi `NoSuchElementException` hoặc `ElementNotInteractableException` ngay tại các bước thao tác trên phần tử tải chậm.
   - **Thứ tự & Hành vi:** Tiến trình mã lệnh chạy quá nhanh so với tốc độ phản hồi của trình duyệt. Dù phần tử xuất hiện ngay sau đó vài miligiây, kịch bản vẫn thất bại lập tức do không có cơ chế chờ.
   - **Kết luận:** Kiểm thử hoàn toàn không ổn định (Flaky test), kết quả phụ thuộc vào tốc độ mạng và cấu hình máy chạy test.

2. **Nêu rõ các quan sát từ thí nghiệm CÓ sử dụng lệnh chờ (Implicit / Explicit Wait)?**
   - **Hiện tượng:** Bài test vận hành mượt mà, trình duyệt chủ động tạm dừng và liên tục kiểm tra cho đến khi phần tử xuất hiện/sẵn sàng tương tác rồi mới thực hiện bước tiếp theo.
   - **Thứ tự & Hành vi:** Khi phần tử xuất hiện (ví dụ ở giây thứ 2 trong tổng số 10 giây chờ tối đa), kịch bản lập tức tiếp tục thực thi ngay mà không bắt chương trình phải chờ hết 10 giây.
   - **Kết luận:** Tối ưu hóa tối đa thời gian chạy test, loại bỏ các lỗi vô lý do mạng chậm và giúp kịch bản đạt kết quả nhất quán trên mọi môi trường.