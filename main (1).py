"""A small command-line Student Registration System for an OOP assignment."""


class Student:
    """Stores one student's basic details and registered courses."""

    def __init__(self, student_id, name, courses=None):
        self.student_id = str(student_id).strip()
        self.name = str(name).strip()
        self.courses = list(courses) if courses else []

    @classmethod
    def from_record(cls, record):
        """Create a Student object from a dictionary record (class method)."""
        return cls(
            record["student_id"],
            record["name"],
            record.get("courses", []),
        )

    def register_course(self, course_name):
        """Add a course to this student's list (instance method)."""
        course_name = course_name.strip()
        if not course_name:
            return False
        if course_name.lower() in [course.lower() for course in self.courses]:
            return False
        self.courses.append(course_name)
        return True

    def display_info(self):
        """Return a readable summary of this student."""
        course_list = ", ".join(self.courses) if self.courses else "No courses registered"
        return f"ID: {self.student_id} | Name: {self.name} | Courses: {course_list}"


class RegistrationSystem:
    """Manages students using a dictionary keyed by student ID."""

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        """Add a Student object; return False if the ID already exists."""
        if student.student_id in self.students:
            return False
        self.students[student.student_id] = student
        return True

    def find_student(self, student_id):
        """Find and return a student, or None if no matching ID exists."""
        return self.students.get(str(student_id).strip())

    def register_course(self, student_id, course_name):
        """Register a student for a course; return a status message."""
        student = self.find_student(student_id)
        if student is None:
            return "Student ID was not found."
        if student.register_course(course_name):
            return f"{course_name.strip()} registered for {student.name}."
        return "Course name is empty or the student is already registered for it."

    def display_students(self):
        """Display all students currently stored in the system."""
        if not self.students:
            print("No students have been added yet.")
            return
        print("\n--- Student Records ---")
        for student in self.students.values():
            print(student.display_info())

    @classmethod
    def with_sample_data(cls):
        """Build a system with fictional sample records (class method)."""
        system = cls()
        sample_records = [
            {"student_id": "ST001", "name": "Aminata Kamara", "courses": ["OOP 1"]},
            {"student_id": "ST002", "name": "Joseph Conteh", "courses": ["Database Systems"]},
        ]
        for record in sample_records:
            system.add_student(Student.from_record(record))
        return system


def main():
    """Run the interactive command-line menu."""
    system = RegistrationSystem.with_sample_data()
    print("Welcome to the Student Registration System")

    while True:
        print("\n1. Add a student")
        print("2. Register a student for a course")
        print("3. Display all students")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            if not student_id or not name:
                print("Student ID and name cannot be empty.")
            elif system.add_student(Student(student_id, name)):
                print("Student added successfully.")
            else:
                print("That student ID already exists.")

        elif choice == "2":
            student_id = input("Enter student ID: ").strip()
            course_name = input("Enter course name: ").strip()
            print(system.register_course(student_id, course_name))

        elif choice == "3":
            system.display_students()

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
