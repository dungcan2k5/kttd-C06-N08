# Hướng dẫn cài đặt và chạy kiểm thử (Tuần 04)

## 1. Yêu cầu môi trường (Prerequisites)

| Công cụ | Môi trường / Phiên bản | Chú thích |
| :--- | :--- | :--- |
| **Python** | 3.10 trở lên | Phải được thêm vào biến môi trường PATH |
| **Trình duyệt** | Google Chrome | Cập nhật phiên bản mới nhất |
| **Browser Driver** | Tự động qua Selenium Manager | Tích hợp sẵn từ Selenium 4.6+ |

## 2. Cài đặt thư viện (Environment Setup)
Mở Terminal/Command Prompt và chạy lệnh sau để cài đặt Selenium và pytest:
```bash
pip install selenium pytest
```

## 3. Lấy mã nguồn (Clone Repository)

git clone [https://github.com/dungcan2k5/kttd-C06-N08.git](https://github.com/dungcan2k5/kttd-C06-N08.git)
cd kttd-C06-N08

## 4. Chạy kiểm thử (Test Execution)
python tuan-04/test_smoke.py