# Grade Checker

# Function to get a valid score from the user

def get_score():
    while True:
        try:
            # Prompt the user to enter a score
            score = int(input("Enter the score (0-100): "))
            # Check if the score is within the valid range
            if 0 <= score <= 100:
                return score # Return the valid score
            else:
                print("Score must be between 0 and 100.")  # Validation failed
        except ValueError:
            # Handle non-integer inputs
            print("Invalid input. Please enter a valid number.")

# Function to determine grade based on the score
def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Main function to run the program
def main():
    score = get_score()  # Get a valid score from the user 
    grade = determine_grade(score)  # Determine the grade using the score
    print(f"Grade: {grade}")  # Print the grade

# Entry point of the program
if __name__ == "__main__":
    main()