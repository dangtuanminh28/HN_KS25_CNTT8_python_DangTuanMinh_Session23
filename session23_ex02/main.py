# main.py
from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date

# Danh sách tệp tin đầu vào (Dữ liệu chuẩn hóa)
raw_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"}, # Lỗi ngày 31/6
    {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
]

def main():
    print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")
    print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... ", end="")
    
    # Khởi tạo an toàn hạ tầng thư mục lưu trữ gốc
    base_vault = "media_vault"
    safe_create_dir(base_vault)
    print("Hoàn tất.")
    print("-" * 75)
    
    success_count = 0
    total_files = len(raw_files)
    
    # Duyệt danh sách với tên biến chuẩn snake_case
    for file_info in raw_files:
        filename = file_info["filename"]
        size_bytes = file_info["size_bytes"]
        upload_at = file_info["upload_at"]
        
        print(f"[TỆP TIN: {filename}]")
        
        # 1. Kiểm tra tính hợp lệ của ngày upload thông qua module analytics
        parsed_date = parse_and_inspect_date(upload_at)
        
        if parsed_date is None:
            # Gặp lỗi ngày tháng -> Báo lỗi trực quan và không làm sập chương trình
            print(f" + Trạng thái phân loại: 🔴 THẤT BẠI (Lỗi: Định dạng ngày upload '{upload_at}' không tồn tại)")
            print()
            continue
            
        # 2. Nếu ngày tháng hợp lệ, tiến hành tính toán số lượng phân vùng block đĩa
        allocated_blocks = calculate_disk_blocks(size_bytes)
        
        # 3. Phân loại định dạng tệp tin để lưu trữ vào thư mục tương ứng
        file_extension = filename.split(".")[-1].lower()
        category_dir = "audio" if file_extension == "mp3" else "video"
        
        # Tiến hành tạo thư mục phân loại cụ thể bên trong media_vault
        target_path = f"{base_vault}/{category_dir}"
        safe_create_dir(target_path)
        
        # 4. In báo cáo thành công ra Console
        print(f" + Dung lượng thực tế: {size_bytes:,} Bytes")
        print(f" + Số khối phân vùng (4KB Block): {allocated_blocks} Blocks")
        print(f" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{category_dir}')")
        print()
        
        success_count += 1
        
    print("========================================================")
    print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{total_files} tệp tin thành công. Hệ thống ổn định.")

if __name__ == "__main__":
    main()