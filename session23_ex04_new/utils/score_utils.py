def calculate_average(scores: list) -> float:
    """Tính điểm trung bình"""
    if not scores:
        return 0.0
        
    total_score = 0.0
    valid_count = 0
    
    for score in scores:
        try:
            clean_score = float(score)
            total_score += clean_score
            valid_count += 1
        except (ValueError, TypeError):
            continue
            
    if valid_count == 0:
        return 0.0
        
    return total_score / valid_count