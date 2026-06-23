def normalize_student_names(records: list):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    print("--- CHUẨN HÓA TÊN SINH VIÊN ---")
    for student in records:
        raw_name = student["name"]
        words_list = raw_name.split()
        clean_name = " ".join(words_list)
        standard_name = clean_name.title()
        
        student["name"] = standard_name
        print(f"{student['student_id']}: {standard_name}")
        
    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")