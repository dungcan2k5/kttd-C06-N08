# Ghi chú Báo cáo - Tuần 07

## 1. Thu hoạch cá nhân & Trả lời câu hỏi tài liệu

### Thành viên 1: [Họ và tên]
* **Bài học thu hoạch:**
  > [Nhập 2-3 câu bằng câu chữ cá nhân về những gì đã học được trong tuần này...]
* **Trả lời câu hỏi tài liệu:**
  1. **Câu hỏi 1:** [Nội dung câu hỏi 1]
     - *Trả lời:* [Câu trả lời]
  2. **Câu hỏi 2:** [Nội dung câu hỏi 2]
     - *Trả lời:* [Câu trả lời]

---

### Thành viên 2: [Họ và tên]
* **Bài học thu hoạch:**
  > [Nhập 2-3 câu bằng câu chữ cá nhân...]
* **Trả lời câu hỏi tài liệu:**
  1. **Câu hỏi:** [Nội dung câu hỏi]
     - *Trả lời:* [Câu trả lời]

---

## 2. Quan sát & Nhận xét Thí nghiệm (Lệnh Wait)

### Thí nghiệm KHÔNG sử dụng lệnh `wait`
* **Hiện tượng quan sát được:** 
  - Tiến trình cha kết thúc trước khi tiến trình con hoàn thành công việc.
  - Kết quả in ra trên terminal bị lẫn lộn giữa tiến trình cha và tiến trình con.
  - Tiến trình con có thể rơi vào trạng thái Zombie hoặc được tiến trình `init`/`systemd` nhận làm cha (Orphan).
* **Nhận xét/Kết luận:** Việc không đồng bộ khiến luồng thực thi bị mất kiểm soát và thứ tự đầu ra không thể dự đoán trước.

### Thí nghiệm CÓ sử dụng lệnh `wait`
* **Hiện tượng quan sát được:**
  - Tiến trình cha tạm dừng thực thi cho đến khi tiến trình con hoàn tất và gửi tín hiệu kết thúc.
  - Thứ tự xuất dữ liệu diễn ra đúng theo trình tự thiết kế.
  - Tiến trình cha nhận được trạng thái kết thúc (exit status) từ tiến trình con.
* **Nhận xét/Kết luận:** Lệnh `wait` giúp đồng bộ hóa các tiến trình, ngăn ngừa hiện tượng tiến trình rác (zombie process) và đảm bảo tính toàn vẹn dữ liệu.

---

## 3. Sử dụng AI / Thuật toán hỗ trợ (Nếu có)

* **Công cụ AI sử dụng:** [Ví dụ: ChatGPT / Claude / Gemini / GitHub Copilot]
* **Câu hỏi / Prompt đã đặt ra:**
  > "[Dán câu hỏi bạn đã dùng để hỏi AI vào đây, ví dụ: Phân biệt tiến trình Zombie và Orphan trong Linux và cách wait() giải quyết?]"
* **Đánh giá độ chính xác:**
  - [ ] Đúng hoàn toàn
  - [ ] Đúng một phần (Chi tiết: ...)
  - [ ] Sai sót / Chưa rõ ràng
* **Kiến thức / Insight mới thu nhận được:**
  - [Ghi lại những insight mới, ví dụ: Hiểu rõ cơ chế kernel thu dọn bảng tiến trình (Process Table) khi lệnh wait() được gọi...]