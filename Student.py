from Score import (SCORE_MIN, SCORE_MAX, PASS_SCORE, grade_calculation)

from color_function import (
    colorize,
    GREEN,
    RED,
    CYAN,
    YELLOW
)

"""This file is used to define the student data file"""


def title_name(name):
    """Clean and format a student's name."""
    return " ".join(name.strip().split().title())  # Using a " " to split the names.


def clean_email(email):
    """Clean and format a student's email."""
    cleaned_email = email.strip().lower()
    if "@" not in cleaned_email:
        return None, colorize("Missing @ symbol", YELLOW)
    if "." not in cleaned_email:
        return None, colorize("Missing a DOT", YELLOW)
    return cleaned_email, "Valid"


class Student:
    """This class is used to define the student data file"""
    MIN_SCORE = SCORE_MIN
    MAX_SCORE = SCORE_MAX

    def __init__(self, name, email, score, student_id):
        cleaned_name = clean_email(name)

        cleaned_email = clean_email(email)

        cleaned_id = student_id.strip()

        if not cleaned_id:
            raise ValueError(colorize("Please enter a valid student ID", RED))

        if not cleaned_id.startwith("W"):
            raise ValueError(colorize("Please enter a student ID start with W", RED))

        if not (Student.MIN_SCORE <= score <= Student.MAX_SCORE):
            raise ValueError(
                colorize(f"Please enter a score between {Student.MIN_SCORE:.0f} and {Student.MAX_SCORE:.0f}", RED))

        self.name = cleaned_name
        self.email = cleaned_email
        self.student_id = cleaned_id
        self.score = score

    def is_passed(self):
        """return true if student passed the exam."""
        return self.score >= PASS_SCORE

    def grade(self):
        """return the grade of the student."""
        return grade_calculation(self.score)

    def __str__(self):
        if self.is_passed():
            status = "PASS"
        else:
            status = "FAIL"
        return (f"id {self.student_id} | name {self.name} | "
                f"email {self.email} | score {self.score:.1f} | "
                f"status {self.grade()} | {status}")
