# Test Cases - Tuần 09 (Basic & Digest Auth)

Môi trường test: `https://the-internet.herokuapp.com`  
Tài khoản mặc định: `admin` / `admin`

## 1. Basic Authentication 

| ID | Mô tả | Các bước thực hiện | Dữ liệu test | Kết quả mong đợi |

| TC01 | Đăng nhập thành công | 
1. Mở trang `/basic_auth`<br>
2. Nhập user/pass vào popup của trình duyệt<br>
3. Bấm Sign in | User: `admin`<br>Pass: `admin` | Vào được trang, hiện dòng chữ: *"Congratulations! You must have the proper credentials."* |

| TC02 | Nhập sai mật khẩu | 
1. Mở trang `/basic_auth`<br>
2. Nhập đúng user, sai pass<br>
3. Bấm Sign in | User: `admin`<br>Pass: `123456` | Không đăng nhập được, popup yêu cầu nhập lại tiếp tục hiện ra |

| TC03 | Bỏ trống thông tin | 
1. Mở trang `/basic_auth`<br>
2. Để trống cả 2 ô rồi bấm Sign in | User: *(trống)*<br>Pass: *(trống)* | Không vào được trang, trình duyệt bắt nhập lại |

| TC04 | Bấm hủy (Cancel) | 
1. Mở trang `/basic_auth`<br>
2. Bấm Cancel trên popup | N/A | Popup tắt, màn hình báo lỗi 401 (hoặc trang trắng) |

## 2. Digest Authentication 

| ID | Mô tả | Các bước thực hiện | Dữ liệu test | Kết quả mong đợi |

| TC05 | Đăng nhập thành công | 
1. Mở trang `/digest_auth`<br>
2. Điền đúng user/pass<br>
3. Bấm Sign in | User: `admin`<br>Pass: `admin` | Vào được trang, hiện thông báo *"Congratulations! You must have the proper credentials."* |

| TC06 | Nhập sai tài khoản | 
1. Mở trang `/digest_auth`<br>
2. Điền sai user hoặc pass<br>
3. Bấm Sign in | User: `test`<br>Pass: `test` | Đăng nhập thất bại, popup hiện lại yêu cầu nhập đúng |

| TC07 | Bấm hủy (Cancel) | 
1. Mở trang `/digest_auth`<br>
2. Bấm Cancel trên popup | N/A | Popup tắt, trang báo lỗi 401 |