from math import ceil
from utils.time_helper import valid_daytime

def check_duplicate_id(flight_id: str, flight_list: list) -> bool:
    """Hàm trợ giúp bẫy lỗi và chuẩn hóa mã chuyến bay"""
    clean_id = flight_id.strip().upper()
    
    if clean_id == '':
        print("Vui lòng không để trống!")
        return False
    for fly in flight_list:
        if clean_id == fly['flight_id']:
            print("Mã tồn tại!")
            return False
    return True

def show_flight(flights):
    if not flights:
        print("Danh sách trống!")
    else:
        print("----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
        for i, fly in enumerate(flights, start=1):
            total_water = fly['passengers'] / 10
            print(f"{i}. Mã: {fly['flight_id']:<5} | Khởi hành: {fly['depart_time']:<20} | Số khách: {fly['passengers']:<5} | Dự phòng: {ceil(total_water)} thùng nước")

def add_flight(flights):
    print("----- TIẾP NHẬN CHUYẾN BAY MỚI -----")
    while True:
        raw_id = input("Nhập mã chuyến bay: ")
        
        if check_duplicate_id(raw_id, flights):
            add_fly_id = raw_id.strip().upper()
            break
            
    while True:
        add_fly_num = input("Nhập số lượng hành khách: ").strip()
        if add_fly_num == '':
            print("Vui lòng không để trống!")
        elif not add_fly_num.isdigit():
            print("Số lượng hành khách phải là số!")
        else:
            add_fly_num = int(add_fly_num)
            break

    while True:
        add_depart_time = input("Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ").strip()
        if add_depart_time == '':
            print("Vui lòng không để trống!")
        elif not valid_daytime(add_depart_time):
            print("Sai định dạng thời gian! Vui lòng nhập đúng chuẩn YYYY-MM-DD HH:MM:SS")
        else:
            break

    while True:
        add_duration_min = input("Nhập số phút bay: ").strip()
        if add_duration_min == '':
            print("Vui lòng không để trống!")
        elif not add_duration_min.isdigit():
            print("Số phút bay phải là số!")
        else:
            add_duration_min = int(add_duration_min)
            break

    new_flight = {
        "flight_id": add_fly_id,
        "passengers": add_fly_num,
        "depart_time": add_depart_time,
        "duration_min": add_duration_min
    }
    flights.append(new_flight)
    print(f">> Thêm chuyến bay {add_fly_id} thành công!")