# ------------------------------------------------------------------
#The following lines are the result of AI
#To make the window colorful
# ------------------------------------------------------------------

"""Using Octal to define the colors."""
USE_COLOR = True    #To start the using of color
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"

def colorize(text, code):
    """To make the window colorful"""
    if USE_COLOR:
        return f"{code}{text}{RESET}"
    return text