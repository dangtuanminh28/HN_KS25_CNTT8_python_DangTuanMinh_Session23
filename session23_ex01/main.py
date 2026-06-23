from datetime import datetime
from utils.file_helper import create_log_dir
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta

shipments = [
    {
        "id": "TRK-001", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 10.8231, "to_lon": 106.6297, 
        "depart": "2026-06-10 08:00:00", "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 16.0544, "to_lon": 108.2022, 
        "depart": "2026-06-10 09:30:00", "deadline": "2026-06-10 15:00:00"
    },
]

def main():
    print("===== HỆ THỐNG GIÁM SÁT VẬN TẢI LÀM SẠCH =====")
    
    create_log_dir("logs")
    print("---------------------------------------------------------------------------")

    time_format = "%Y-%m-%d %H:%M:%S"
    
    for s in shipments:
        distance = calculate_distance(s["from_lat"], s["from_lon"], s["to_lat"], s["to_lon"])
        
        eta_obj = predict_eta(s["depart"], distance, speed=60)
        eta_str = eta_obj.strftime(time_format)
        
        deadline_obj = datetime.strptime(s["deadline"], time_format)
        
        print(f"Mã xe: {s['id']} | Quãng đường: {distance:.2f} km")
        print(f"  + Xuất phát: {s['depart']}")
        print(f"  + ETA dự kiến: {eta_str}")
        print(f"  + Hạn cuối (Deadline): {s['deadline']}")
        
        if eta_obj > deadline_obj:
            trang_thai = f"CẢNH BÁO: Xe {s['id']} TRỄ HẸN! (Vượt quá {eta_obj - deadline_obj})"
        else:
            trang_thai = f"AN TOÀN: Xe {s['id']} bảo đảm tiến độ giao hàng."
            
        print(f"  -> Trạng thái: {trang_thai}")
        print("========================================================")

if __name__ == "__main__":
    main()