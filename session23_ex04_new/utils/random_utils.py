import random
import string

def generate_assignment_code():
    print("--- SINH MÃ BÀI TẬP ---")
    pool = string.ascii_uppercase + string.digits
    
    random_part = ""
    for i in range(4):
        random_part += random.choice(pool)
        
    final_code = "PY-" + random_part
    print(f"Mã bài tập của bạn là: {final_code}")