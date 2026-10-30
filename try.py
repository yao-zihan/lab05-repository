def get_integer(prompt, minimum=None, maximum=None):
    """Prompt user until they enter a valid integer in range."""
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Please enter at least {minimum}")
                continue
            if maximum is not None and value > maximum:
                print(f"Please enter at most {maximum}")
                continue
            return value
        except ValueError:
            print("Please enter a whole number")

age = get_integer("Age: ", 0, 120)
score = get_integer("Score (0-100): ", 0, 100)