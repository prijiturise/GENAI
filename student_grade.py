def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# Ask how many students
try:
    number = int(input("How many students? "))

    for i in range(number):
        print("\nStudent", i + 1)

        name = input("Enter student name: ")

        try:
            mark = float(input("Enter mark: "))

            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100.")
            else:
                grade = calculate_grade(mark)

                print("Name:", name)
                print("Mark:", mark)
                print("Grade:", grade)

        except ValueError:
            print("Please enter a valid mark.")

except ValueError:
    print("Please enter a valid number of students.")
