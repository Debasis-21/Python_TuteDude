# Function to write content to a file
def write_to_file(filename, content):
    try:
        # Open the file in write mode
        with open(filename, "w") as f:
            f.write(content)  # Write the user-provided content to the file
        print(f"Content written to '{filename}' successfully.")
    except Exception as e:
        # Catch and display any error that occurs while writing
        print(f"An error occurred: {e}")

# Function to get multiline input from the user
def get_multiline_input():
    print("Enter your content (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)  # Combine all lines with newline characters

# Main program
def main():
    filename = input("Enter the filename to write to (e.g., output.txt): ").strip()
    content = get_multiline_input()   # Get content from user
    write_to_file(filename, content)  # Save content to the specified file

# Entry point of the program
if __name__ == "__main__":
    main()
