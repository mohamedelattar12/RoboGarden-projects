import os
from datetime import datetime

def write_entry(file_name):
    try:
        entry = input("Write your diary entry: ")

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        full_entry = f"{timestamp}\n{entry}\n\n"

        with open(file_name, 'a') as file:
            file.write(full_entry)
        print("Your diary entry has been saved.")
    except PermissionError:
        print("Permission denied. You do not have permission to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_entries(file_name):
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                entries = file.read()
                if entries:
                    print("\nPrevious Diary Entries:\n")
                    print(entries)
                else:
                    print("No entries found.")
        else:
            print("Diary file does not exist.")
    except PermissionError:
        print("Permission denied. You do not have permission to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    diary_file = 'personal_diary.txt'

    while True:
        print("\nPersonal Diary Application")
        print("1. Write a new entry")
        print("2. View previous entries")
        print("3. Exit")
        choice = input("Please choose an option (1/2/3): ")
        if choice == '1':
            write_entry(diary_file)
        elif choice == '2':
            view_entries(diary_file)
        elif choice == '3':
            print("Thank you for using the Personal Diary Application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


main()
