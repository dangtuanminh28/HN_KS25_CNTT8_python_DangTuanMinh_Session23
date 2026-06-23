from core.manager import show_flight, add_flight
from utils.time_helper import show_flight_eta
from utils.file_helper import check_log

flights = [
    {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120}, # Hà Nội - TP.HCM
    {"flight_id": "RA002", "passengers": 85,  "depart_time": "2026-06-15 13:30:00", "duration_min": 45}   # Hà Nội - Vinh
]

while True:
    print("""
===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====
1. Hiển thị lịch trình và Thống kê hậu cần
2. Tiếp nhận chuyến bay mới
3. Tính thời gian hạ cánh dự kiến (ETA)
4. Khởi tạo thư mục lưu trữ log hệ thống
5. Thoát chương trình
==================================================
""")
    choice = input("Nhập lựa chọn của bạn: ").strip()
    
    if choice == '1':
        show_flight(flights)
    elif choice == '2':
        add_flight(flights)
    elif choice == '3':
        show_flight_eta(flights)
    elif choice == '4':
        check_log()
    elif choice == '5':
        print("Cảm ơn kỹ sư đã sử dụng hệ thống!")
        break
    else:
        print("Vui lòng nhập (1-5)!")