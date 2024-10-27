import os 

# Function to create a file
def create_file(filename):
    try: 
        with open(filename, 'x') as f:  # Fixed quotes around filename
            print(f"File '{filename}' created successfully")
    except FileExistsError:
        print(f"File '{filename}' already exists")
    except Exception as e:  # Fixed typo in exception variable
        print(f"An error occurred: {e}")

# Function to view all files in the current directory
def view_files():
    files = os.listdir()
    if not files:
        print("No files found in the current directory")  # Fixed function name to 'print'
    else:
        print('Files in directory:')
        for file in files:  # Fixed variable shadowing and misused variable name
            print(file)

# Function to delete a file
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' successfully removed from directory")
    except FileNotFoundError:
        print(f"File '{filename}' not found in directory")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to read a file
def read_file(filename):
    try:
        with open(filename, 'r') as f:  # Fixed hard-coded file name
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to edit a file
def edit_file(filename):
    try:
        with open(filename, 'a') as f:  # Fixed hard-coded file name
            content = input('Enter the data you want to add: ')
            f.write(content + "\n")
            print(f"Updated successfully to '{filename}'")
    except FileNotFoundError:
        print(f"File '{filename}' does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function for menu-driven interface
def main():
    while True:
        print("\nFile Management App")
        print("1: Create file")
        print("2: View all files")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter the file name you want to create: ")
            create_file(filename)  # Corrected function call
        elif choice == '2':
            view_files()  # Corrected function call
        elif choice == '3':
            filename = input("Enter the file name you want to delete: ")
            delete_file(filename)  # Corrected function call
        elif choice == '4':
            filename = input("Enter the file name you want to read: ")
            read_file(filename)  # Corrected function call
        elif choice == '5':
            filename = input("Enter the file name you want to edit: ")
            edit_file(filename)  # Corrected function call
        elif choice == '6':
            print("App is closing")
            break
        else:
            print("Invalid input, please choose a valid option")

# Run main function
if __name__ == "__main__":
    main()






