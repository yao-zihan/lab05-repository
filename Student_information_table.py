from project import validate_score

DATA_FILE = "students.csv"

USE_COLOR = True
RESET = "\033[0m"  #Set the color to use.
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"

import math
import csv
from dataclasses import dataclass

@dataclass
class Student:
    student_id: str
    name: str
    email: str
    score: float

def student_from_csv(line):
    """Parse a single line of CSV string into a Student object (using split). Return None on failure."""
    parts = line.strip().split(",")
    if len(parts) != 4:
        return None
    student_id, name, email, score_text = parts
    score, _ = validate_score(score_text)
    if score is None:
        return None
    return Student(student_id=student_id, name=name, email=email, score=score)

def student_to_csv(student):
    """Turn students into csv string"""
    return ",".join(
        [student.student_id, student.name, student.email, str(student.score)])

def find_student_by_id(students, student_id):
    """Find a student by exact student ID. Return None if not found."""
    for student in students:
        if student.student_id == student_id:
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

def print_header(title):
    """print a header with """
    print()
    print("=" * 42)
    print(colorize(title, CYAN))
    print("=" * 42)

def colorize(text, code):
    """colour the text with code"""
    if USE_COLOR:
        return f"{code}{text}{RESET}"
    return text

def get_nonempty(prompt):
    """Check whether the input is empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(colorize("Input cannot be empty. Please try again.", YELLOW))

