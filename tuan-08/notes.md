# Ghi chú Tuần 8 - Kiểm thử chức năng Upload

## 1. Kiến thức học được (Learning Notes)

- **Cách upload file bằng Selenium:** Thay vì click vào nút upload để mở hộp thoại của hệ điều hành (Selenium không tương tác được với OS dialog), ta dùng phương thức `.send_keys("đường_dẫn_tuyệt_đối")` truyền thẳng vào thẻ `<input type="file">`.
- **Explicit Wait:** Tiếp tục sử dụng `WebDriverWait` kết hợp `expected_conditions` để chờ thông báo lỗi render xong trên DOM, đảm bảo kịch bản không bị vỡ do mạng chậm. Tuyệt đối loại bỏ `time.sleep()`.

## 2. Kịch bản Fail case (Reading Answers)

- Để đáp ứng yêu cầu "The test result must be a failure", script được thiết kế theo dạng **Intentional Failure**.
- Hệ thống xử lý đúng khi chặn file `.txt` không hợp lệ và quăng ra thông báo lỗi. Tuy nhiên, hàm `assert` ở cuối được cố tình viết sai logic (kỳ vọng thông báo thành công). Điều này ép `pytest` trả về **FAILED** kèm theo dòng `AssertionError`, chứng minh script có khả năng bắt lỗi chính xác khi kết quả thực tế lệch với kỳ vọng.
