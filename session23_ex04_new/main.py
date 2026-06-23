from reports.report_generator import display_student_scores, export_learning_report
from utils.string_utils import normalize_student_names
from utils.random_utils import generate_assignment_code

student_records = [
	{
    	"student_id": "SV001",
    	"name": "Nguyễn Văn A",
    	"scores": [8.5, 7.0, 9.0]
	},	
	{
    	"student_id": "SV002",
    	"name": "Trần Thị B",
    	"scores": [4.0, 5.5, 5.0]
	},
	{
    	"student_id": "SV003",
    	"name": "Lê Văn C",
    	"scores": [9.5, 9.0, 8.5]
	}
]
def main():
	while True :
		print("""
===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====
1. Xem danh sách sinh viên và điểm trung bình
2. Chuẩn hóa tên sinh viên
3. Sinh mã bài tập ngẫu nhiên
4. Xuất báo cáo học tập
5. Thoát chương trình
====================================================	
	""")
		choice = input("Chọn chức năng (1-5): ").strip()
		if choice == '1':
			display_student_scores(student_records)
		elif choice == '2':
			normalize_student_names(student_records)
		elif choice == '3':
			generate_assignment_code()
		elif choice == '4':
			export_learning_report(student_records)
		elif choice == '5':
			print("Cảm ơn bạn đã sử dụng hệ thống!")
			break
		else :
			print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()