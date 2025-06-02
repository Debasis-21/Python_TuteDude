# Function to read and display content from a file
def read_from_file(filename):
    try:
        # Open the file in read mode
        with open(filename, "r") as f:
            content = f.read()  # Read all content from the file
        print("\nFile Content:")
        print(content)  # Print the read content
    except FileNotFoundError:
        # If the file does not exist
        print(f"File '{filename}' not found.")
    except Exception as e:
        # Catch and display any other error that occurs
        print(f"An error occurred: {e}")

# Main function to handle user interaction
def main():
    filename = input("Enter the filename to read from: ").strip()  # Ask user for filename
    read_from_file(filename)  # Call function to read the file

# Entry point of the program
if __name__ == "__main__":
    main()
