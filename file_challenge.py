# File Read & Write Challenge with Error Handling

def process_file(filename):
    try:
        # Try opening the file for reading
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open("modified_" + filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Success! Modified file created: modified_{filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read/write this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Ask the user for a filename
filename = input("Enter the filename to process: ")
process_file(filename)
