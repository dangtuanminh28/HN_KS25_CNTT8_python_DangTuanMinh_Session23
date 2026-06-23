from datetime import datetime
from utils.score_utils import calculate_average

def display_student_scores(records: list):
    """Chức năng 1: Xem danh sách sinh viên"""
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    print("--- DANH SÁCH ĐIỂM SINH VIÊN ---")    
    for i, student in enumerate(records, start=1):
        avg_score = calculate_average(student['scores'])
        
        if avg_score >= 8.0:
            rank = "Giỏi"
        elif avg_score >= 6.5:
            rank = "Khá"
        elif avg_score >= 5.0:
            rank = "Trung bình"
        else:
            rank = "Yếu"
            
        scores_str = ""
        for score in student['scores']:
            scores_str += str(score) + ", "
        scores_str = scores_str[:-2] if scores_str else ""
        
        print(f"{i}. [{student['student_id']}] {student['name']:<15} | Điểm: [{scores_str}] | ĐTB: {avg_score:.2f} - {rank}")
    print("-------------------------------------------------------------------")

def export_learning_report(records: list):
    """Chức năng 4: Xuất báo cáo"""
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    print("--- XUẤT BÁO CÁO HỌC TẬP ---")
    total_students = len(records)
    passed_count = 0
    failed_count = 0
    
    for student in records:
        avg_score = calculate_average(student["scores"])
        if avg_score >= 5.0:
            passed_count += 1
        else:
            failed_count += 1
            
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số sinh viên đạt yêu cầu: {passed_count}")
    print(f"Số sinh viên cần cải thiện: {failed_count}")
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("learning_report.txt", "w", encoding="utf-8") as file:
        file.write("===== BÁO CÁO KẾT QUẢ HỌC TẬP =====\n")
        file.write(f"Thời gian khởi tạo: {current_time}\n")
        file.write(f"Tổng số sinh viên: {total_students}\n")
        file.write(f"Số sinh viên đạt yêu cầu: {passed_count}\n")
        file.write(f"Số sinh viên cần cải thiện: {failed_count}\n")
        
    print(">> Đã xuất báo cáo ra file learning_report.txt")