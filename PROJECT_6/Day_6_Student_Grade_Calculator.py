def calculate_percentage(total_marks, num_subjects):
    return total_marks / num_subjects


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    print("=" * 40)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 40)

    num_subjects = int(input("Enter number of subjects: "))

    total_marks = 0

    for i in range(1, num_subjects + 1):
        while True:
            marks = float(input(f"Enter marks for Subject {i} (0-100): "))
            if 0 <= marks <= 100:
                total_marks += marks
                break
            else:
                print("Invalid input! Marks should be between 0 and 100.")

    percentage = calculate_percentage(total_marks, num_subjects)
    grade = calculate_grade(percentage)

    print("\n" + "=" * 40)
    print("RESULT")
    print("=" * 40)
    print(f"Total Marks : {total_marks:.2f}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")


if __name__ == "__main__":
    main()