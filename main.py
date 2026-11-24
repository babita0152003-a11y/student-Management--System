students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        course = input("Enter course: ")

        student = {
            "name": name,
            "roll": roll,
            "course": course
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print("\nName:", student["name"])
                print("Roll:", student["roll"])
                print("Course:", student["course"])

    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                print("Student Found!")
                print("Name:", student["name"])
                print("Course:", student["course"])
                found = True

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
                    
                    