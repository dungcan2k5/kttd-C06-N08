from selenium import webdriver
 
# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()
 
# Mở trang web
driver.get("https://the-internet.herokuapp.com/")
 
# In ra tiêu đề trang
print(driver.title)

input("Nhấn Enter để đóng trình duyệt...")
# Đóng trình duyệt  
driver.quit()
