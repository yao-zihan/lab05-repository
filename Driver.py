from color_function import(
    colorize,
    GREEN,
    RED,
    CYAN,
    YELLOW
)

"""To create a file that store the scores of the students which is learned from AI"""
DATA_FILE = "students.csv"
CSV_HEADER = "student_id,name,email,score"        # CSV header (AI)

"""This file is about some functions of menu."""
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

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
def search_by_id(students, written_id):
    """Search student by ID"""
    for student in students:
        if student.student_id == written_id:
            return student
    return None
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------