def get_grade(marks):
    if 75 <= marks <= 100:
        return "A"
    elif 65 <= marks <= 74:
        return "B"
    elif 55 <= marks <= 64:
        return "C"
    elif 35 <= marks <= 54:
        return "S"
    elif 0 <= marks <= 34:
        return "F"
    else:
        return None

try:
    marks = int(input("Enter your marks (0-100): "))
    grade = get_grade(marks)

    if grade:
        print(f"Your grade is: {grade}")
    else:
        print("Invalid marks. Must be between 0 and 100.")
except ValueError:
    print("Please enter a valid number.")
