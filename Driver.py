from color_function import(
    colorize,
    GREEN,
    RED,
    CYAN,
    YELLOW
)
from student_information_table import DATA_FILE , student_from_csv , student_to_csv , CSV_HEADER
from Score import PASS_SCORE
from Score import highest_score , lowest_score , average_score , grade_statistics

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
    print(" 8. Show statistics")
    print(" 9. Save statistics")
    print(" 0. Exit program")

#----------------------------------------------------------------------------


# -----------------------------choice 4-------------------------------
def delete_student(students):
    """Delete student from students list"""
    print_header("Delete Student")
    student_id = get_nonempty("Student ID of the student to delete:")
    student = search_by_id(students, student_id)
    if student is None:
        print(colorize(f"No student found with {student_id} 。", RED))
        return
    students.remove(student)
    print(colorize(f"Successfully delete {student.name}。", GREEN))


def get_nonempty(prompt):
    """Check whether the input is empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(colorize("Input cannot be empty. Please try again.", YELLOW))

#-----------------------------choice 5-------------------------------
def search_by_id(students, written_id):
    """Search student by ID"""
    for student in students:
        if student.student_id == written_id:
            return student
    return None

#-----------------------------choice 6-------------------------------
def search_students(students, query):
    """Search by name/student ID/email. Return a list of matches."""
    query = query.strip().lower()
    matches = []
    for student in students:
        if (query in student.name.lower()
                or query in student.student_id.lower()
                or query in student.email.lower()):
            matches.append(student)
    return matches

#-----------------------------choice 7-------------------------------
"""Return student by grade."""
def filter_by_grade(students, letter):
    return [student for student in students if student.grade() == letter]

"""Return student by passed or not."""
def filter_by_pass(students, passed):
    return [student for student in students if student.is_passed() == passed]

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
    if choice == "1":                              #Filter by grade.
        letter = input("please enter A/B/C/D/F: ")
        if letter not in ("A","B","C","D","F"):
            print(colorize("please enter correct letter",RED))
            return
        result = filter_by_grade(students, letter)

    elif choice == "2":                            #Filter by passed or not.
        answer = input("please enter P or F")
        if answer not in ("P","F"):
            print(colorize("please enter correct answer",RED))
            return
        result = filter_by_pass(students, answer == "p")

    elif choice == "0":                            #Exit
        return

    else:
        print(colorize("Incorrect choice", RED))
        return

    if not result:
        print("There are no students in that condition")
        return

#-----------------------------------choice 8-----------------------------------------

def show_statistics(students):
    """Show the statistics of students."""
    print_header("Show statistics")
    if not students:
        print("No students")
        return
    passed = 0
    for student in students:
        if student.score >= PASS_SCORE:
            passed += 1
    pass_rate = passed / len(students)
    highest , best = highest_score(students)
    lowest , worst = lowest_score(students)
    average = average_score(students)
    count_a , count_b , count_c , count_d , count_f = grade_statistics(students)

    print(f"Number of students{len(students)}")
    print(f"Best:{best} {highest}")
    print(f"Worst:{worst} {lowest}")
    print(f"Average score: {average}")
    print(f"A:{count_a}")
    print(f"B:{count_b}")
    print(f"C:{count_c}")
    print(f"D:{count_d}")
    print(f"F:{count_f}")
    print(f"pass rate: {pass_rate:.1%}")

#-----------------------------------choice 9-----------------------------------------
"""!!!These are generated by AI!!!"""
def load_students(filename=DATA_FILE):
    """From a CSV file, return a list of students"""
    students = []                          #Prepare an empty array to store information.
    try:
        with open(filename, "r") as file:  #"r" means read only.
            lines = file.readlines()       #Read the rows at once.
    except FileNotFoundError:
        return students

    for line in lines[1:]:                  # Skip the header of the CSV.
        student = student_from_csv(line)
        if student is not None:
            students.append(student)
    return students


def save_students(students, filename=DATA_FILE):
    """Save the list of students"""
    try:
        with open(filename, "w") as file:   #"w" means writing mode.
            file.write(CSV_HEADER + "\n")
            for student in students:
                file.write(student_to_csv(student) + "\n")   #Turn every student into CSV.
        return True
    except OSError as error:
        print(colorize(f"Save error {error}", RED))
        return False
#-----------------------------------MAIN-----------------------------------------