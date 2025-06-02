import json   # For file-based JSON storage
import os     # To check file existence

# JSON file name where grades will be stored
FILENAME = "grades.json"

# Load student grades from file (if exists), otherwise return empty dictionary
def load_grades():
    if os.path.exists(FILENAME):  # Check if file exists
        try:
            with open(FILENAME, "r") as f:
                return json.load(f)  # Load and return data from JSON
        except json.JSONDecodeError:
            # If the file is corrupted or unreadable, start fresh
            print("Error reading grade data. Starting with an empty record.")
            return {}
    return {}  # File doesn't exist; start with empty grades

# Save the student grades dictionary to the JSON file
def save_grades(grades):
    with open(FILENAME, "w") as f:
        json.dump(grades, f)  # Convert dictionary to JSON and save

# Add a new student and grade
def add_student(grades):
    name = input("Enter student name: ").strip()
    if name in grades:
        print(f"{name} already exists.")
    else:
        grade = input("Enter grade: ").strip().upper()
        grades[name] = grade
        print(f"Added {name} with grade {grade}.")

# Update an existing student's grade
def update_grade(grades):
    name = input("Enter student name to update: ").strip()
    if name in grades:
        grade = input("Enter new grade: ").strip().upper()
        grades[name] = grade
        print(f"Updated {name}'s grade to {grade}.")
    else:
        print(f"{name} does not exist.")

# Display all students and their grades
def print_grades(grades):
    if grades:
        print("\nAll Student Grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade}")
    else:
        print("No student records found.")

# Menu system to interact with the user
def menu():
    grades = load_grades()  # Load existing data

    while True:
        print("\n1. Add Student")
        print("2. Update Grade")
        print("3. View Grades")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_student(grades)
        elif choice == "2":
            update_grade(grades)
        elif choice == "3":
            print_grades(grades)
        elif choice == "4":
            save_grades(grades)  # Save data before exiting
            print("Grades saved. Exiting.")
            break
        else:
            print("Invalid choice.")

# Entry point of the program
if __name__ == "__main__":
    menu()
