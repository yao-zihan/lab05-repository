from color_function import(
    colorize,
    GREEN,
    RED,
    CYAN,
    YELLOW
)
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
    print(" 7. Filter student")
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
"""Return student by grade."""
def filter_by_grade(students, letter):
    return [student for student in students if student.grade() == letter]

"""Return student by passed or not."""
def filter_by_pass(students, passed):
    return [student for student in students if student.passOrnot() == passed]

"""Mix the two functions above."""
def filter_student(students):
    print_header("Filter student")
    if not students:
        print("No students")
        return
    print("1.Filter by grade A/B/C/D/F")
    print("2.Filter by PASS or not")
    print("0.Return")
    choice = input("please enter your choice: ")
    if choice == "1":
        letter = input("please enter A/B/C/D/F: ")
        if letter not in ("A","B","C","D","F"):
            print(colorize("please enter correct letter",RED))
            return
        result = filter_by_grade(students, letter)

    elif choice == "2":
        answer = input("please enter P or F")
        if answer not in ("P","F"):
            print(colorize("please enter correct answer",RED))
            return
        result = filter_by_pass(students, answer == "p")

    elif choice == "0":
        return

    else:
        print(colorize("Incorrect choice", RED))
        return

    if not result:
        print("There are no students in that condition")
        return



#----------------------------------------------------------------------------