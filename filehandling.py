# Step 1: Create and write to input.txt
with open("input.txt", "w") as input_file:
    input_file.write("am humble.\n")
    input_file.write("am honest.\n")
    input_file.write("i love team work.\n")
    input_file.write("coding is fun.\n")
    input_file.write("Finally, i want to become an expert in software engineering.\n")

# Step 2: Read the contents of input.txt
with open("input.txt", "r") as input_file:
    content = input_file.read()

# Step 3: Process the content
word_count = len(content.split())  # Count the number of words
uppercase_content = content.upper()  # Convert text to uppercase

# Step 4: Write the processed content and word count to output.txt
with open("output.txt", "w") as output_file:
    output_file.write(uppercase_content)
    output_file.write(f"\n\nWord Count: {word_count}")

# Step 5: Print success message
print("The file 'output.txt' has been created successfully!")