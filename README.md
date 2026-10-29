
## Project Documentation

**Project type:** Python command-line application  
**Programming language:** Python 3  
**Programming approach:** Object-oriented programming (OOP)  
**Data storage:** In-memory Python data structures  
**Interface:** Interactive command-line menu

> **Documentation note:** This README is based on the implementation visible in the supplied code screenshots. The application stores records in memory; persistent database or file storage is not demonstrated in the supplied evidence.

## 1. Introduction

The Student Registration System is a menu-driven Python application designed to manage basic student records and course registrations. It allows a user to add a student, register an existing student for a course, display the students currently held by the application, and exit the program.

The project demonstrates how object-oriented programming can be used to organise related data and operations into classes and methods. It also demonstrates input handling, conditional logic, iteration, validation, and the use of a class method to construct an instance containing sample records.

## 2. Aim and Objectives

### Aim
To develop a simple, interactive student registration application that organises student information and supports basic course-registration operations.

### Objectives
- Create and manage student objects.
- Add students to a central registration system.
- locate a student using a student ID.
- Register a course for a valid student.
- Prevent duplicate student IDs and repeated or empty course registrations where the underlying methods enforce these checks.
- Display the student records currently stored in the system.
- Provide a clear command-line menu for user interaction.
- Demonstrate object-oriented programming concepts in Python.

## 3. Main Features

| Menu option | Function |
|---|---|
| 1. Add a student | Collects student information and attempts to add the student to the system. |
| 2. Register a student for a course | Requests a student ID and course name, then displays the registration status. |
| 3. Display all students | Lists the student records currently stored in the system. |
| 4. Exit | Displays a goodbye message and terminates the menu loop. |

## 4. Technologies and Concepts

- **Python 3:** Implements the program logic.
- **Classes and objects:** Represent students and the registration system.
- **Methods:** Group operations such as adding, finding, registering, and displaying students.
- **Dictionary/data collections:** The system accesses student records through `self.students.values()` and uses student IDs to locate records.
- **Lists and dictionaries:** Sample records are represented as dictionaries in a list.
- **Conditionals:** `if`/`elif` statements select menu actions and handle validation outcomes.
- **Loops:** A menu loop keeps the application running until the user selects Exit; a `for` loop displays stored records.
- **Input processing:** `.strip()` removes leading and trailing whitespace from entered values.
- **Class method:** `with_sample_data(cls)` creates a system instance and populates it with fictional records.

## 5. Program Structure

### 5.1 Student class

The screenshots show calls to `Student.from_record(record)`, `student.register_course(course_name)`, and `student.display_info()`. These indicate that the `Student` class is responsible for representing an individual student and providing operations related to that student's information.

The visible sample records contain:
- `student_id`
- `name`
- `courses`

The `from_record` method is used to construct a student object from a dictionary. The `register_course` method attempts to add a course to that student's course list, while `display_info` provides a formatted representation of the student's details.

### 5.2 RegistrationSystem class

The `RegistrationSystem` class manages the collection of student objects. The visible implementation includes the following methods:

| Method | Responsibility |
|---|---|
| `find_student(self, student_id)` | Searches for a student using the supplied ID. |
| `register_course(self, student_id, course_name)` | Finds the student, delegates course registration to the student object, and returns a status message. |
| `display_students(self)` | Displays all stored student records, or an informative message if none exist. |
| `with_sample_data(cls)` | A class method that creates a system and adds fictional sample records. |

The `register_course` method first calls `find_student`. If no matching student is found, it returns **“Student ID was not found.”** If a student is found and the student's `register_course` method succeeds, it returns a confirmation containing the course name and student name. Otherwise, it returns a message explaining that the course name is empty or the student is already registered for it.

### 5.3 `main()` function

The visible `main()` function runs the interactive command-line menu. The menu presents four choices and uses conditional branches to execute the selected operation.

For course registration, the program requests a student ID and course name, removes surrounding whitespace using `.strip()`, and calls `system.register_course(student_id, course_name)`. Selecting option 3 calls `system.display_students()`. Selecting option 4 prints a goodbye message and uses `break` to leave the menu loop.

## 6. How the System Works

1. The program starts and displays the Student Registration System menu.
2. The user enters a menu choice from 1 to 4.
3. The relevant branch in `main()` handles the selection.
4. For student creation, the program collects student details and attempts to add the student. The visible code indicates that it reports whether the student was added or whether the ID already exists.
5. For course registration, the program obtains the student ID and course name, searches for the student, and attempts to register the course.
6. For displaying records, the system checks whether any students exist. If records are present, it iterates through them and prints each student's information.
7. The menu continues until the user selects option 4.

## 7. Validation and Status Messages

The visible code demonstrates several checks and user-facing messages:

- **Student not found:** The registration system checks whether `find_student` returns `None`.
- **Empty or repeated course:** The course-registration operation returns a failure message if the course name is empty or the student is already registered for it, subject to the validation implemented in `Student.register_course`.
- **Duplicate student ID:** The add-student branch displays a message when the ID already exists.
- **No records:** `display_students` prints a message and returns when the student collection is empty.
- **Whitespace handling:** `.strip()` is applied to the student ID and course name entered for course registration.

These checks improve usability by giving the user feedback instead of silently ignoring an unsuccessful operation.

## 8. Sample Data

The class method `with_sample_data(cls)` creates two fictional student records:

| Student ID | Name | Course |
|---|---|---|
| ST001 | Aminata Kamara | OOP 1 |
| ST002 | Joseph Conteh | Database Systems |

The method converts each dictionary into a `Student` object by calling `Student.from_record(record)`, then adds that object to the registration system. These are demonstration records, not evidence of real student information.

## 9. Running the Application

1. Install Python 3 on the computer.
2. Save the project source code in a Python file, for example `student_registration.py`.
3. Open a terminal in the directory containing the file.
4. Run:

```bash
python student_registration.py
```

On systems where Python is invoked as `python3`, use:

```bash
python3 student_registration.py
```

5. Follow the displayed menu and enter the option number.
6. Select option 4 to exit.

**Note:** The exact filename depends on the name used when saving the source file.

## 10. Screenshots and Implementation Evidence

The following screenshots document the code structure and the running interface.

### Figure 1. Course-registration logic
The code locates a student by ID, checks whether the student exists, attempts to register the requested course, and returns a success or failure message.

### Figure 2. Registration-system methods and sample-data class method
The screenshot shows the `register_course` and `display_students` methods, together with the `with_sample_data` class method and its two fictional records.

### Figure 3. Main command-line menu
The running application displays the four available actions: add a student, register a student for a course, display all students, and exit.

### Figure 4. Menu selection handling
The code shows how the application processes course registration, displays student records, and exits when option 4 is selected.

## 11. Limitations

Based on the supplied screenshots, the following limitations should be considered:

- **No demonstrated permanent storage:** Student data appears to be held in memory. Records may be lost when the program closes unless persistence is implemented elsewhere in the source code.
- **Command-line interface only:** The screenshots show a text-based menu rather than a graphical or web interface.
- **Basic scope:** The demonstrated menu focuses on adding students, registering courses, viewing records, and exiting.
- **Limited evidence of testing:** The screenshots show code and the menu, but do not provide a complete test report covering every success and failure case.

## 12. Recommended Future Improvements

- Add persistent storage using SQLite or another database.
- Provide update and delete operations for student records.
- Add stronger validation for student IDs, names, and course names.
- Add automated unit tests for successful and unsuccessful operations.
- Improve the interface with a graphical or web-based front end.
- Add search and filtering for students and courses.
- Provide reports such as course enrolment lists.

## 13. Conclusion

The Student Registration System demonstrates a practical application of Python object-oriented programming. It organises student information into objects, centralises student management in a registration-system class, and provides a simple menu through which users can add students, register courses, and view records. The project also demonstrates validation, control flow, iteration, and reusable methods. With persistent storage, expanded record-management features, and a broader testing strategy, the application could be developed into a more complete student administration tool.

---

**Academic submission note:** Add your name, student ID, course/module title, lecturer's name, institution, and submission date to the cover page if required by your department. Verify that the final source code matches the descriptions in this document before submission.
E_Student_Registration_System.md…]()
