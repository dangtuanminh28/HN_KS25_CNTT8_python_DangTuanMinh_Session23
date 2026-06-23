import os

def create_log_dir(dir_name: str):
    """
    Kiểm tra an toàn sự tồn tại của thư mục trước khi tạo.
    Tránh tuyệt đối lỗi FileExistsError khiến ứng dụng bị sập.
    """
    if not os.path.exists(dir_name):
        print(f"[SYSTEM] Thư mục '{dir_name}' chưa tồn tại. Đang khởi tạo...")
        os.mkdir(dir_name)
        print("[SYSTEM] Tạo thư mục log thành công!")
    else:
        print(f"[SYSTEM] Thư mục '{dir_name}' đã tồn tại. Bỏ qua bước khởi tạo.")