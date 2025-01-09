import os

def input_grades(file_name):
    try:
        with open(file_name, 'a') as file:
            while True:
                subject = input("Enter subject name (or type 'done' to finish): ").strip()
                if subject.lower() == 'done':
                    break
                grade = input(f"Enter grade for {subject}: ").strip()
                try:
                    grade = float(grade)
                    file.write(f"{subject}:{grade}\n")
                    print(f"Grade for {subject} saved.")
                except ValueError:
                    print("Invalid grade. Please enter a numeric value.")
    except PermissionError:
        print("Permission denied. Cannot write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def calculate_average(file_name):
    try:
        with open(file_name, 'r') as file:
            grades = []
            for line in file:
                try:
                    subject, grade = line.strip().split(':')
                    grades.append(float(grade))
                except ValueError:
                    print(f"Skipping invalid entry: {line.strip()}")
            if grades:
                average = sum(grades) / len(grades)
                print(f"Your average grade is: {average:.2f}")
            else:
                print("No valid grades found to calculate the average.")
    except FileNotFoundError:
        print("Grades file not found. Please input grades first.")
    except PermissionError:
        print("Permission denied. Cannot read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    file_name = "grades.txt"
    while True:
        print("\nStudent Grade Tracker")
        print("1. Input grades")
        print("2. Calculate average grade")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            input_grades(file_name)
        elif choice == '2':
            calculate_average(file_name)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


main()
