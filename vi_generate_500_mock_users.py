import pandas as pd
import random
import unidecode

# 1. Khởi tạo danh sách dữ liệu mẫu để trộn
last_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Phan", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý"]
first_names = [
    "Anh", "Bình", "Cường", "Dũng", "Em", "Phương", "Giang", "Hải", "Hùng", "Khanh", "Linh", "Minh", 
    "Nam", "Oanh", "Phát", "Quân", "Sơn", "Thảo", "Tuấn", "Vinh", "Xuân", "Yến", "Trang", "Tâm", "Tùng"
]
middle_names = ["Văn", "Thị", "Minh", "Đức", "Hồng", "Ngọc", "Tuấn", "Hoàng", "Khánh", "Mai"]

phone_prefixes = ["090", "091", "098", "096", "097", "032", "035", "070", "077", "083", "085"]
domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
segments = ["B2B", "B2C"]
tour_types = ["Accommodations", "Cruises", "Domestic Tour", "Inbound Tour"]

data = []

# 2. Vòng lặp tạo 500 dòng dữ liệu
for _ in range(500):
    last = random.choice(last_names)
    first = random.choice(first_names)
    middle = random.choice(middle_names)
    
    # Kết hợp tên đầy đủ để làm email
    full_first_name = f"{middle} {first}"
    
    # Chuyển tên không dấu để tạo email chuẩn
    last_clean = unidecode.unidecode(last).lower().replace(" ", "")
    first_clean = unidecode.unidecode(first).lower().replace(" ", "")
    email = f"{last_clean}.{first_clean}{random.randint(10, 99)}@{random.choice(domains)}"
    
    phone = random.choice(phone_prefixes) + "".join([str(random.randint(0, 9)) for _ in range(7)])
    segment = random.choice(segments)
    tour = random.choice(tour_types)
    
    data.append({
        "Last Name": last,
        "First Name": full_first_name,
        "Email": email,
        "Phone": phone,
        "Phân khúc": segment,
        "Loại hình Tour": tour
    })

# 3. Tạo DataFrame và xuất file
df = pd.DataFrame(data)

# Xuất ra file Excel
df.to_excel("mock_data_tourism_500.xlsx", index=False)
print("Đã tạo thành công file 'mock_data_tourism_500.xlsx' với 500 dòng dữ liệu!")
