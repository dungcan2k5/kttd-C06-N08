# Tuần 08: Test Report & Learning Notes

## 1. Documenting Failing and Flaky Tests (Để xử lý vào Tuần 9)

Quá trình chạy test suite với `pytest-html` ghi nhận kết quả như sau:

*   **`test_upload_invalid_file_fail_case` (Cố ý Fail): FAILED**
    *   **Nguyên nhân:** Web thiếu tính năng kiểm tra định dạng (Validation). Test case kỳ vọng hệ thống chặn file `.exe` và báo `Unsupported file format`, nhưng hệ thống lại hiển thị `File Uploaded!`.
    *   **Hướng xử lý Tuần 9:** Ghi nhận đây là một Bug của ứng dụng. Cần cập nhật lại kịch bản test hoặc report bug cho Dev.
*   **`test_upload_file_invalid` (Không đính kèm file): PASSED (nhưng chứa tiềm ẩn)**
    *   **Nguyên nhân:** Khi nhấn Upload mà không có file, server trả về lỗi `500 Internal Server Error`. Mặc dù test case PASS do bắt được chuỗi "Internal Server Error", nhưng việc server sập thay vì hiển thị thông báo UI (ví dụ: "Please select a file") là một lỗi UX/Backend nghiêm trọng.
    *   **Hướng xử lý Tuần 9:** Đưa case này vào danh sách Flaky/Bug cần refactor. Nên assert trạng thái HTTP thay vì chỉ check text trên UI.

## 2. Personal Learning Notes & Reading Answers

*   **Cách thức gom nhóm code:** Rút ra bài học về cách tối ưu hóa WebDriver. Thay vì mỗi test case tự khởi tạo và tắt trình duyệt gây tốn thời gian, việc sử dụng chung `@pytest.fixture` với thuộc tính `yield` giúp code sạch và chạy nhanh hơn.
*   **Cấu hình Pytest-HTML:** Việc sử dụng flag `--self-contained-html` rất hữu ích vì nó nhúng toàn bộ CSS/JS vào chung một file `report.html` duy nhất, giúp việc chia sẻ file báo cáo cho team dễ dàng mà không bị mất định dạng.
*   **Waits mechanisms:** Hiểu rõ hơn lý do tại sao cấm dùng `time.sleep()`. Thay vì bắt hệ thống phải chờ chết 5 giây, `WebDriverWait` (Explicit Wait) kết hợp với `expected_conditions` giúp kịch bản test chủ động đi tiếp ngay khi phần tử xuất hiện, giảm thiểu thời gian chạy test suite.

## 3. Lệnh cài đặt và tạo báo cáo
*   **Cài đặt thư viện bắt buộc: pip install pytest selenium pytest-html
*   **Chạy test suite và xuất báo cáo HTML:pytest tuan-08/test_upload.py --html=tuan-08/report.html --self-contained-html