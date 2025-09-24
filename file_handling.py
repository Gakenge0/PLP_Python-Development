def modify_file():
    input_file = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")

    try:
        with open(input_file, "r") as infile:
            content = infile.read()

        # Example modification: convert text to uppercase
        modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"File '{input_file}' was modified and saved as '{output_file}'.\n")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")


def read_user_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as f:
            print("\n--- File Content ---")
            print(f.read())
            print("---------------------\n")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.\n")
    except PermissionError:
        print(f"Error: You don’t have permission to read '{filename}'.\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")


def main():
    while True:
        print("File Handling & Exception Handling Menu")
        print("1. Modify a file and save to new file")
        print("2. Read a file")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            modify_file()
        elif choice == "2":
            read_user_file()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


# Run the program
if __name__ == "__main__":
    main()
