from Score import validate_score


from color_function import(
    colorize,
    GREEN,
    RED,
    CYAN,
    YELLOW
)

from dataclasses import dataclass

from Driver import print_header

DATA_FILE = "students.csv"

@dataclass
class Student:
    student_id: str
    name: str
    email: str
    score: float

def student_from_csv(line):
    """
    Parse a single line of CSV string into a Student object (using split).
    Return None on failure.
    """
    parts = line.strip().split(",")
    if len(parts) != 4:
        return None
    student_id = parts[0] , name = parts[1] , email = parts[2] , score_text = parts[3]

    score, _ = validate_score(score_text)    #This line uses AI, "_" means "give up the second information.

    if score is None:
        return None
    return Student(student_id=student_id, name=name, email=email, score=score)

def student_to_csv(student):
    """Turn students into csv string"""
    return ",".join(
        [student.student_id, student.name, student.email, str(student.score)])

def search_by_id(students, written_id):
    """Search student by ID"""
    for student in students:
        if student.student_id == written_id:
            return student
    return None

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

def delete_student(students):
    """Delete student from students list"""
    print_header("Delete Student")
    student_id = get_nonempty("Student ID of the student to delete:")
    student = find_student_by_id(students, student_id)
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