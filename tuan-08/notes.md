### Thành viên:Lê Thị Nga - Kiểm thử tính năng Upload (/upload)

### Điều đã học
- Đã xây dựng kịch bản kiểm thử cố tình gây lỗi (Negative Testing) cho tính năng tải lên tệp tin (/upload) bằng cách không chọn tệp trước khi gửi form.
- Áp dụng thành thạo Explicit Wait (`WebDriverWait` và `expected_conditions`) để chờ phần tử UI sẵn sàng tương tác mà không cần dùng `time.sleep()`.

### Trả lời câu hỏi đọc tài liệu:
1. **Tại sao việc thực hiện Negative Test cho tính năng Upload lại quan trọng?**
   - Giúp đảm bảo hệ thống phản hồi chính xác khi người dùng quên đính kèm tệp hoặc gửi tệp không hợp lệ, tránh việc ứng dụng bị treo hoặc tràn bộ nhớ.