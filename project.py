# ------------------------------------------------------------------
#The following lines are the result of AI
#To make the window colorful
# ------------------------------------------------------------------

USE_COLOR = True
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"

def colorize(text, code):
    """To make the window colorful"""
    if USE_COLOR:
        return f"{code}{text}{RESET}"
    return text

# ------------------------------------------------------------------
# Some constants
# ------------------------------------------------------------------

DATA_FILE = "students.csv"                        # To create a csv form to store the information
CSV_HEADER = "student_id,name,email,score"        # CSV header (AI)
"""Add some basic scores"""
SCORE_MIN = 0
SCORE_MAX = 100
PASS_SCORE = 60.0

# ------------------------------------------------------------------
# Some main functions
# ------------------------------------------------------------------

def title_name(name):
    """Clean and format a student's name."""
    return " ".join(name.strip().split().title())

def student_into_csv(student):
    """Turn a student's information into string."""
    return ",".join(
        [student.student_id, student.name, student.email, str(student.score)]       #Array
    )


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
    """Calculate average score。"""
    if not students:
        return None          #If there's no student,return none.
    total = 0
    for student in students:
        total += student.score
    return total / len(students)

def highest_score(students):
    """Return the highest score."""
    if not students:
        return None
    best = students[0]     #Let the first student be the example
    for student in students:
        if student.score > best.score:
            best = student
    return best


def lowest_score(students):
    """Return the lowest score."""
    if not students:
        return None
    worst = students[0]      #Same as "best"
    for student in students:
        if student.score < worst.score:
            worst = student
    return worst

def clean_and_validate_email(email):
    """Clean and validate an email address."""
    cleaned = email.strip().lower()
    if "@" not in cleaned:
        return None, "Missing @ symbol"
    if "." not in cleaned:
        return None, "Missing dot"
    return cleaned, "Valid"

def validate_score(score_text):
    """Turn score into float and correct its range.Return score and error message."""
    try:
        score = float(score_text)
    except ValueError:
        return None, "Score must be a float"
    if not (SCORE_MIN <= score <= SCORE_MAX):
        return None, f"Score must be between {SCORE_MIN:.0f} to {SCORE_MAX:.0f}"    #keep the number being integer
    return score, ""        # Using "" as a success symbol

def grade_distribution(students):
    """Count the number of students in each grade."""
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_f = 0
    """ Count the number of students in each grade."""
    for student in students:
        grade = grade_calculation(student.score)
        if grade == "A":
            count_a += 1
        elif grade == "B":
            count_b += 1
        elif grade == "C":
            count_c += 1
        elif grade == "D":
            count_d += 1
        else:
            count_f += 1
    return {"A": count_a, "B": count_b, "C": count_c, "D": count_d, "F": count_f}

def search_student_by_id(students, student_id):
    """Search student by ID."""
    for student in students:
        if student.student_id == student_id:
            return student
    return None


def format_student(student):
    """Show student details."""
    grade = grade_calculation(student.score)
    if student.score >= PASS_SCORE:
        status = "PASS"
    else: "FAIL"
    return (f"ID {student.student_id} | Name {student.name} | "
            f"Email {student.email} | Score {student.score:.1f} | "
            f"Grade {grade} | {status}")


# ------------------------------------------------------------------
# Some subfunctions
# ------------------------------------------------------------------

def print_header(title):
    """Print a header to the screen."""
    print()
    print("=" * 42)
    print(colorize(title, CYAN))
    print("=" * 42)

def print_menu():
    """display the menu options"""
    print_header("Students' scores management system")
    print(" 1. Display all students")
    print(" 2. Add new student")
    print(" 3. Edit student")
    print(" 4. Delete student")
    print(" 5. Search student according to ID")
    print(" 6. Search (Name / ID / Email)")
    print(" 7. Score statistics")
    print(" 8. Save statistics")
    print(" 0. Exit program")


