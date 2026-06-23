import math

def calculate_disk_blocks(size_bytes: int, block_size: int = 4096) -> int:
    """Dùng hàm math.ceil để làm tròn chính xác số """
    if size_bytes == 0:
        return 0
    return math.ceil(size_bytes / block_size)