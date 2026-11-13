"""This file is used to define the student data file"""
def title_name(name):
    """Clean and format a student's name."""
    return " ".join(name.strip().split().title())      #Using" "to split the names.

def clean_email(email):
    """Clean and format a student's email."""
    cleaned_email = email.strip().lower()
    if "@" not in cleaned_email:
        return None,"Missing @ symbol"
    if "."not in cleaned_email:
        return None,"Missing a DOT"
    return cleaned_email,"Valid"


