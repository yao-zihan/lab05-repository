# ------------------------------------------------------------------
# Some constants
# ------------------------------------------------------------------
import unicodedata
import math
import csv
from pathlib import Path
DATA_FILE = Path(__file__).resolve().with_name("grades.csv")
CSV_HEADER = "student_id,name,email,score"        # CSV header (AI)
"""To create a file that store the scores of the students which is learned from AI"""
SCORE_MIN = 0
SCORE_MAX = 100
PASS_SCORE = 60.0

# ------------------------------------------------------------------
# Some main functions
# ------------------------------------------------------------------

def title_case_name(name):
    """Clean and format a person's name."""
    return " ".join(name.strip().split().title())
#return grade according to the score

def grade_calculation(score):
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
        return None, f"Score must be between {SCORE_MIN:.0f} to {SCORE_MAX:.0f}"
    return score, ""


def print_header(title):
    """Print a header to the screen."""
    print()
    print("=" * 42)
    print(coloriza(title, CYAN))
    print("=" * 42)

# ------------------------------------------------------------------
# Some subfunctions
# ------------------------------------------------------------------


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


def main():
    try:
        records = load_records()
    except DataError as exc:
        print(f"Startup failed: {exc}")
        print(f"Check the file: {DATA_FILE}")
        return

    if records:
        count = len(records)
        records_word = "record" if count == 1 else "records"
        print(f"Loaded {count} grade {records_word}.")

    while True:
        print_menu()
        choice = input()

        if choice == "1":
            input_score(records)
        elif choice == "2":
            grade_calculation(records)
        elif choice == "3":
            name = input("Please enter the student's name: ")

        elif choice in ("0", "q", "exit"):
            print("\nGoodbye.")
            return
        else:
            print("Invalid choice. Please enter 0, 1, or 2.")