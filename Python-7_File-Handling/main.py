# Step 1: Read contents from a file
try:
    # Try to open 'sample.txt' in read mode
    with open('sample.txt', 'r') as file:
        contents = file.read()  # the purpose of this line is to read the whole file
        print("Contents of the file:")
        print(contents)
except FileNotFoundError:
    # incase the file not found, show this message:
    print("The file 'sample.txt' was not found.")

# Step 2: Write to a new file
# 'w' to create new file, or if there is an exisitng file, we will overwrite
with open('newfile.txt', 'w') as file:
    file.write("This is a new file, like New Year New Me XD. Zoo wee mama, live, laugh, love coding!! <33\n")
    print("\nNew file created with content:")

# Step 3: Verify content in the new file by reading it ('r')
with open('newfile.txt', 'r') as file:
    newfile_contents = file.read()
    print(newfile_contents)