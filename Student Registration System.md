# Student Registration System

A simple command-line project written in Python to demonstrate Object-Oriented Programming (OOP). It stores fictional student records in a dictionary and allows users to add students, register them for courses, and display all records.

## Requirements

- Python 3
- No external packages are required.

## Run the program

From this folder, run:

```bash
python3 main.py
```

The program starts with two fictional sample students. Choose an option from the menu to add a student, register a course, display records, or exit.

## Example interaction

```text
Welcome to the Student Registration System

1. Add a student
2. Register a student for a course
3. Display all students
4. Exit
Choose an option (1-4): 3

--- Student Records ---
ID: ST001 | Name: Aminata Kamara | Courses: OOP 1
ID: ST002 | Name: Joseph Conteh | Courses: Database Systems
```

## OOP concepts demonstrated

- `Student` and `RegistrationSystem` are classes.
- Each `Student` object has attributes: `student_id`, `name`, and `courses`.
- `register_course`, `display_info`, `add_student`, and `display_students` are instance methods.
- `Student.from_record` and `RegistrationSystem.with_sample_data` are class methods, marked with `@classmethod`.
- `RegistrationSystem.students` is a dictionary that stores multiple `Student` objects, using each student ID as the key.
- The `main` function creates and uses objects from both classes.

## Digital Public Goods (DPG) alignment

- **Open source:** The project uses plain Python and can be shared in a public GitHub repository. A license such as MIT may be added when publishing.
- **Privacy:** The included names and IDs are fictional. Do not enter real sensitive or confidential personal information.
- **Modular and reusable:** Student data and registration behavior are separated into classes, so the classes can be reused in other small programs.
- **Accessible design:** The program has a text-based menu and requires no paid software or third-party packages.

## Files

- `main.py` — program source code.
- `README.md` — project explanation and usage instructions.
