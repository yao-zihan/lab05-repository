"""This file is used to define the student data file"""
def title_name(name):
    """Clean and format a student's name."""
    return " ".join(name.strip().split().title())      #Using" "to split the names.

def clean_email(email):
    """Clean and format a student's email."""
    cleaned_email = email.strip().lower()
    if "@" not in cleaned_email:
        return None,"Missing @ symbol"
    if "."not in cleaned_email:
        return None,"Missing a DOT"
    return cleaned_email,"Valid"

def grade_calculation(score):
    """Calculate a grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def average_score(students):
    """Calculate a average score."""
    if not students:
        return None,
    total_score = 0
    for student in students:
        total_score += student.score
    return total_score/len(students)

def highest_score(students):
    """Calculate a highest score."""
    if not students:
        return None
    highest = students[0].score
    best = students[0]
    for student in students:

        if student.score > highest :
            highest = student.score
            best = student
    return highest,best

def lowest_score(students):
    """Calculate a lowest score."""
    if not students:
        return None
    lowest = students[0].score
    worst = students[0]
    for student in students:

        if student.score < lowest :
            lowest = student.score
            worst = student
    return lowest,worst
