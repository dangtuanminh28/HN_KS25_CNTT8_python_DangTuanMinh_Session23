from datetime import datetime, timedelta

def valid_daytime(datetime_str: str) -> bool:
    """Kiểm tra chuỗi nhập vào có đúng định dạng YYYY-MM-DD HH:MM:SS"""
    try:
        datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False

def show_flight_eta(flights_list: list):
    print("----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")
    search_id = input("Nhập mã chuyến bay cần tính: ").strip().upper()
    
    for fly in flights_list:
        if fly['flight_id'] == search_id:
            time_format = "%Y-%m-%d %H:%M:%S"
            depart_dt = datetime.strptime(fly['depart_time'], time_format)
            eta_dt = depart_dt + timedelta(minutes=fly['duration_min'])
            eta_str = eta_dt.strftime(time_format)
            
            print(f"-> Chuyến bay {fly['flight_id']} cất cánh lúc: {fly['depart_time']}")
            print(f"-> Thời gian hạ cánh dự kiến (ETA): {eta_str}")
            break
    else:
        print(f"Không tìm thấy chuyến bay có mã {search_id}!")