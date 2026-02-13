# grades.py
class Grade:
    def __init__(self, category, score, weight):
        self.category = category
        self.score = score
        self.weight = weight
    
    def get_weighted_score(self):
        return (self.score * self.weight) / 100

def calc_final_grade(grades_list, weights_list):
    if not grades_list:
        return 0
    
    total_weighted_score = 0
    total_weight_applied = 0
    
    # Group grades by category
    categories = {}
    for grade in grades_list:
        if grade.category not in categories:
            categories[grade.category] = []
        categories[grade.category].append(grade.score)
    
    # Calculate weighted contribution
    mark_types = ["assignment", "quiz", "test", "midterm", "exam", "project"]
    
    for i, category in enumerate(mark_types):
        if weights_list[i] > 0 and category in categories:
            category_avg = sum(categories[category]) / len(categories[category])
            weighted_contribution = (category_avg * weights_list[i]) / 100
            total_weighted_score += weighted_contribution
            total_weight_applied += weights_list[i]
    
    # Adjust if weights don't total 100%
    if total_weight_applied < 100 and total_weight_applied > 0:
        total_weighted_score = (total_weighted_score * 100) / total_weight_applied
    
    return round(total_weighted_score, 2)