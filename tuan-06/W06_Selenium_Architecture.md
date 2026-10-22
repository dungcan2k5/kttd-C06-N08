# W06 - Selenium Architecture & Command Execution Flow (Task #24)

## Nội dung trình chiếu (Slide Content)

### Slide 4: Các thành phần cốt lõi của Selenium (Selenium Suite)
*   **Selenium IDE:** Tiện ích mở rộng (add-on) trên trình duyệt cung cấp tính năng Record & Playback. Cho phép tạo test script thông qua giao diện UI mà không cần viết code. Phù hợp để tạo prototype nhanh hoặc tái tạo bug đơn giản.
*   **Selenium WebDriver:** Giao diện lập trình ứng dụng (Core API) cho phép viết các kịch bản tự động hóa bằng các ngôn ngữ như Java, JavaScript/Node.js, C#, Python. Giao tiếp trực tiếp với trình duyệt ở mức độ native, là nền tảng để xây dựng các framework automation test linh hoạt và phức tạp.
*   **Selenium Grid:** Kiến trúc phân tán (Hub & Node) dùng để mở rộng quy mô. Cho phép thực thi song song nhiều bài test trên các máy ảo/vật lý khác nhau, với nhiều phiên bản trình duyệt và hệ điều hành khác nhau, giúp tối ưu hóa thời gian chạy test suite.

### Slide 5: Luồng thực thi câu lệnh (Command Execution Workflow)
Kiến trúc của Selenium hoạt động theo mô hình Client-Server. Đường đi của một lệnh từ code đến trình duyệt trải qua 4 bước:
1.  **Test Code (Client):** Đoạn mã automation (ví dụ: JavaScript hoặc Java) khởi tạo một lệnh tương tác (VD: `driver.findElement(By.id("login")).click()`).
2.  **Giao thức W3C WebDriver (API):** Lệnh được thư viện WebDriver chuyển đổi thành một HTTP Request với định dạng JSON và gửi qua mạng (RESTful API).
3.  **Driver Binary (Server trung gian):** Các file thực thi độc lập (như `chromedriver.exe` cho Chrome, `geckodriver.exe` cho Firefox) nhận HTTP Request, giải mã nội dung và dịch nó thành các lệnh native mà trình duyệt đó có thể hiểu được.
4.  **Browser (Thực thi & Trả kết quả):** Trình duyệt thực thi thao tác vật lý (click, gõ phím). Sau đó, trình duyệt trả trạng thái về cho Driver, Driver đóng gói thành HTTP Response và gửi ngược lại cho Test Code để ghi nhận pass/fail.

---

## Dàn ý thuyết trình cho Giáo viên (Main Presentation Points)

**1. Phân tích 3 thành phần của hệ sinh thái Selenium (Slide 4)**
*   **Selenium IDE:** Nhấn mạnh đây là tool dành cho việc test nhanh (Record & Playback), không yêu cầu kỹ năng code.
*   **Selenium WebDriver:** Nhấn mạnh đây là "trái tim" của Selenium, phục vụ việc viết automation framework phức tạp. Điểm mạnh là hỗ trợ đa ngôn ngữ (Java, C#, JS) và tương tác sâu (native) với trình duyệt.
*   **Selenium Grid:** Nhấn mạnh vai trò "mở rộng hiệu suất". Dùng để chạy test song song (parallel) trên nhiều môi trường khác nhau nhằm tiết kiệm tối đa thời gian thực thi.

**2. Giải thích luồng đi của một dòng code (Slide 5)**
*   **Bản chất kiến trúc:** Trình bày rằng Selenium hoạt động dựa trên mô hình Client-Server giao tiếp qua chuẩn HTTP.
*   **Bước 1 & 2 (Đóng gói lệnh):** Khi lập trình viên gọi lệnh (vd: `click`), thư viện WebDriver (Client) sẽ không nói chuyện trực tiếp với trình duyệt, mà đóng gói lệnh đó thành một **HTTP Request chuẩn W3C**.
*   **Bước 3 (Vai trò thông dịch):** Trình bày vai trò then chốt của **Driver Binary** (như ChromeDriver). Nó hoạt động như một server cục bộ, nhận HTTP request và "dịch" sang ngôn ngữ native của trình duyệt.
*   **Bước 4 (Thực thi & Phản hồi):** Trình duyệt thực thi thao tác thật. Kết quả được trả ngược về Driver, Driver bọc lại thành HTTP Response gửi về cho code để báo cáo Pass/Fail.
*   **Kết luận (Key Takeaway):** Nhờ kiến trúc "giao tiếp qua HTTP" và "dùng Driver làm trung gian" này, Selenium hoàn toàn độc lập với ngôn ngữ lập trình và loại trình duyệt.