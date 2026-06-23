from datetime import datetime

def parse_and_inspect_date(date_str: str) -> datetime | None:
    """ Kiểm tra dữ liệu ngày tháng bằng try-except ValueError"""
    try:
        valid_date = datetime.strptime(date_str, "%Y-%m-%d")
        return valid_date
    except ValueError:
        return None