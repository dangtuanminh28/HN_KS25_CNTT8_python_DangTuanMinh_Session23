from datetime import datetime, timedelta

def predict_eta(departure_str: str, distance_km: float, speed: float = 60) -> datetime:
    """
    Chuyển chuỗi departure thành datetime, cộng thời gian di chuyển 
    dựa trên khoảng cách và vận tốc để trả về đối tượng datetime ETA.
    """
    time_format = "%Y-%m-%d %H:%M:%S"
    dep_time = datetime.strptime(departure_str, time_format)
    
    hours_needed = distance_km / speed
    
    eta_datetime = dep_time + timedelta(hours=hours_needed)
    return eta_datetime