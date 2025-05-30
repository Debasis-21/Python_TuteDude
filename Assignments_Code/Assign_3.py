# Write to a File

# Open a file in write mode ('w' will create the file if it doesn't exist)

file = open("example.txt", "w")

# Write content to the file
file.write("Hello, this is a sample file.\n")
file.write("You can write multiple lines.\n")
file.write("This is the third line.\n")

# Close the file to save changes
file.close()

print("Content written to 'example.txt' successfully")
