from color_function import(
    colorize,
    GREEN,
    RED,
    CYAN,
    YELLOW
)

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

#----------------------------------------------------------------------------

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

#-----------------------------------choice 8-----------------------------------------

def show_statistics(students):
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

def load_students(filename=DATA_FILE):
    """从 CSV 文件读取学生记录；文件不存在时返回空列表（副作用：读文件）。"""
    students = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return students

    for line in lines[1:]:                  # 跳过表头（第一行）
        student = student_from_csv(line)
        if student is not None:
            students.append(student)
    return students


def save_students(students, filename=DATA_FILE):
    """把学生记录保存到 CSV 文件；返回是否成功（副作用：写文件）。"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(CSV_HEADER + "\n")
            for student in students:
                file.write(student_to_csv(student) + "\n")
        return True
    except OSError as error:
        print(colorize(f"保存失败：{error}", RED))
        return False