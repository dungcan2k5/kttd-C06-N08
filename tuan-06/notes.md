# Ghi chú tuần 06 – Retrospective & Phản hồi sau buổi báo cáo

**Thành viên phụ trách:** Tiến Dũng  
**Vai trò tuần này:** Timekeeper & ghi nhận phản hồi trong buổi thuyết trình

---

## Slide 7 – Khó khăn, lỗi locator và AI hỗ trợ như thế nào

### Những khó khăn gặp phải trong dự án

1. **Lỗi locator không ổn định (flaky locators)**  
   - Vấn đề: Một số phần tử trên trang web thay đổi `id` hoặc `class` sau mỗi lần tải lại trang, khiến test bị fail ngẫu nhiên.  
   - Cách xử lý: Chuyển sang dùng XPath tương đối (`//button[contains(text(),'Login')]`) thay vì `id` động. Kết hợp `WebDriverWait` để chờ phần tử xuất hiện thay vì dùng `time.sleep()` cứng.

2. **Khó debug khi test chạy headless**  
   - Vấn đề: Khi chạy CI/CD không có giao diện, rất khó biết test fail ở bước nào.  
   - Cách xử lý: Chụp screenshot tự động vào thư mục `anh/` khi test thất bại, dùng `driver.save_screenshot()` trong khối `except`.

3. **Quản lý phiên WebDriver – rò rỉ tài nguyên**  
   - Vấn đề: Quên gọi `driver.quit()` khiến tiến trình Chrome "zombie" chiếm RAM.  
   - Cách xử lý: Dùng `try/finally` để đảm bảo `driver.quit()` luôn được gọi dù test pass hay fail.

### AI hỗ trợ nhóm như thế nào

- **Gợi ý cấu trúc test:** AI (Gemini/GitHub Copilot) gợi ý cách tổ chức test theo Page Object Model, giúp code dễ bảo trì hơn.
- **Debug locator:** Khi paste XPath bị lỗi vào chat AI, AI giải thích lý do và đề xuất XPath thay thế chính xác hơn.
- **Giải thích lỗi Selenium:** Khi gặp `StaleElementReferenceException`, AI giải thích nguyên nhân (DOM bị render lại) và cách dùng `EC.presence_of_element_located` để xử lý.
- **Lưu ý quan trọng:** Mọi đoạn code do AI gợi ý đều được nhóm đọc kỹ, hiểu từng dòng, và kiểm tra thực tế trước khi commit – không copy-paste mù quáng.

---

## Ghi nhận phản hồi và câu hỏi trong buổi báo cáo

> **Timekeeper note:** Buổi thuyết trình diễn ra đúng 7 phút + 3 phút Q&A theo kế hoạch.

### Phản hồi / Câu hỏi 1 – Từ giảng viên

**Câu hỏi:** "Tại sao nhóm chọn `WebDriverWait` thay vì `time.sleep()` cố định?"

**Trả lời của nhóm:** `time.sleep()` luôn chờ đúng thời gian đã đặt dù phần tử đã xuất hiện sớm hơn, gây lãng phí thời gian chạy test. `WebDriverWait` chỉ chờ đến khi điều kiện thỏa mãn (hoặc hết timeout), giúp test nhanh hơn và tin cậy hơn.

**Cải tiến rút ra:** Chuẩn hóa toàn bộ dự án – thay thế mọi `time.sleep()` bằng `WebDriverWait` + `expected_conditions`.

---

### Phản hồi / Câu hỏi 2 – Từ nhóm khác

**Câu hỏi:** "Nhóm có test trên Firefox không hay chỉ Chrome?"

**Trả lời của nhóm:** Hiện tại nhóm chỉ test trên Chrome vì đây là yêu cầu cơ bản của bài. Tuy nhiên Selenium hỗ trợ đa trình duyệt thông qua việc thay đổi WebDriver.

**Cải tiến rút ra:** Xem xét dùng `pytest` parametrize để chạy cùng test case trên nhiều trình duyệt trong các tuần sau (cross-browser testing).

---

### Phản hồi / Câu hỏi 3 – Từ thành viên trong lớp

**Câu hỏi:** "Làm sao nhóm biết test đã pass khi chạy ở chế độ headless (không có màn hình)?"

**Trả lời của nhóm:** Kết quả pass/fail được pytest báo cáo trực tiếp qua terminal. Ngoài ra, nhóm cấu hình chụp screenshot tự động khi có lỗi, lưu vào thư mục `anh/` để kiểm chứng.

**Cải tiến rút ra:** Bổ sung HTML report bằng `pytest-html` plugin để có báo cáo trực quan hơn cho các buổi sau.

---

## Tổng kết cải tiến sau tuần 06

| # | Vấn đề phát hiện | Cải tiến đề xuất | Ưu tiên |
|---|---|---|---|
| 1 | Dùng `time.sleep()` cứng | Chuyển sang `WebDriverWait` toàn bộ | 🔴 Cao |
| 2 | Chỉ test trên Chrome | Bổ sung cross-browser testing | 🟡 Trung bình |
| 3 | Thiếu HTML report | Tích hợp `pytest-html` | 🟡 Trung bình |
| 4 | Locator dễ vỡ | Áp dụng Page Object Model | 🟢 Dài hạn |
