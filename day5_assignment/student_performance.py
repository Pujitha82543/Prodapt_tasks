# Student Performance Analyzer

students = []

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


# Function to add student
def add_student():
    name = input("Enter student name: ")

    python_marks = int(input("Enter Python marks: "))
    sql_marks = int(input("Enter SQL marks: "))
    linux_marks = int(input("Enter Linux marks: "))

    # Validate marks
    if (0 <= python_marks <= 100 and
        0 <= sql_marks <= 100 and
        0 <= linux_marks <= 100):

        marks = [python_marks, sql_marks, linux_marks]
        total = sum(marks)
        average = total / 3
        grade = calculate_grade(average)

        student = {
            "name": name,
            "marks": marks,
            "total": total,
            "average": average,
            "grade": grade
        }

        students.append(student)
        print("Student added successfully")

    else:
        print("Marks should be between 0 and 100.")


# Function to display all students
def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        for student in students:
            print("\nName:", student["name"])
            print("Marks:", student["marks"])
            print("Total:", student["total"])
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])


# Function to search student
def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Total:", student["total"])
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])
            found = True
            break

    if not found:
        print("Student not found.")


# Function to show class average
def class_average():
    if len(students) == 0:
        print("No student records available.")
    else:
        total_average = 0

        for student in students:
            total_average += student["average"]

        class_avg = total_average / len(students)
        print("Class Average:", round(class_avg, 2))


# Main Menu
while True:
    print("\nStudent Performance System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Class Average")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        class_average()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")