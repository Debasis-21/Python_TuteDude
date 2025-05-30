# Student Grades Manager

# Initialize an empty dictionary
student_grades = {}

while True:
    print("\nChoose an option:")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        name = input("Enter student name: ")
        if name in student_grades:
            print(f"{name} already exists.")
        else:
            grade = input("Enter grade: ")
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}")
    
    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input(f"Enter new grade for {name}: ")
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"{name} does not exit.")
    
    elif choice == '3':
        if student_grades:
            print("\nAll Student Grades:")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")
        else:
            print("No student records found.")
    
    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
