import os

def safe_create_dir(path: str):
    """Khởi tạo thư mục một cách an toàne"""
    os.makedirs(path, exist_ok=True)