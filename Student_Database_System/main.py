class Student:
    def __init__(self, name, age, grades):
        """
        Initialize a new Student object.
        
        :param name: The name of the student
        :param age: The age of the student
        :param grades: A list of grades (e.g., [90, 85, 88])
        """
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        """
        Display student information.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average_grade(self):
        """
        Calculate the average grade of the student.
        :return: The average grade
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


class StudentDatabase:
    def __init__(self):
        """
        Initialize the student database.
        """
        self.students = []

    def add_student(self, name, age, grades):
        """
        Add a new student to the database.
        
        :param name: The name of the student
        :param age: The age of the student
        :param grades: A list of grades
        """
        student = Student(name, age, grades)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def display_all_students(self):
        """
        Display information for all students in the database.
        """
        if not self.students:
            print("No students in the database.")
            return

        print("\nStudent Information:")
        for idx, student in enumerate(self.students, start=1):
            print(f"\nStudent {idx}:")
            student.display_info()
            print(f"Average Grade: {student.calculate_average_grade():.2f}")


def main():
    database = StudentDatabase()
    database.add_student("Alice", 20, [85, 90, 88])
    database.add_student("Bob", 22, [78, 74, 80])
    database.add_student("Charlie", 19, [92, 88, 95])
    database.display_all_students()
    print("\nAdding a new student interactively...")
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grades = list(map(int, input("Enter the student's grades (separated by spaces): ").split()))
    database.add_student(name, age, grades)
    database.display_all_students()



main()
