DATA_FILE = "students.csv"
SCORE_MIN = 0
SCORE_MAX = 100
PASS_SCORE = 60.0

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
