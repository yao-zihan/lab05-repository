from Score import grade_calculation


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
CSV_HEADER = "student_id,name,email,score"

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

    score, _ = grade_calculation(score_text)    #This line uses AI, "_" means "give up the second information.

    if score is None:
        return None
    return Student(student_id=student_id, name=name, email=email, score=score)

def student_to_csv(student):
    """Turn students into csv string"""
    return ",".join(
        [student.student_id, student.name, student.email, str(student.score)])

