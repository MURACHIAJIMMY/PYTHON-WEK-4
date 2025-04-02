# File Read & Write Challenge with Error Handling

def process_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Step 1: Attempt to open and read the file
        with open(input_filename, "r") as input_file:
            content = input_file.read()

        # Step 2: Process the content
        modified_content = content.upper()  # Convert text to uppercase

        # Step 3: Write the modified content to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)

        # Step 4: Print success message
        print(f"The modified file has been created successfully as '{output_filename}'!")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file could not be read or written. Please check file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
process_file()