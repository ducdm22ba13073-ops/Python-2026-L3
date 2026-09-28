# Practical work 1: Student Mark Management

# Global data storage
students = []  # List of tuples: (id, name, dob)
courses = []   # List of tuples: (id, name)
marks = {}     # Dictionary mapping course_id -> { student_id: mark }


# --- Input Functions ---

def input_number_of_students():
    count = int(input("Enter number of students in the class: "))
    return count

def input_student_information(num_students):
    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Student Name: ").strip()
        dob = input("Enter Date of Birth (DoB): ").strip()
        students.append((student_id, name, dob))

def input_number_of_courses():
    count = int(input("\nEnter number of courses: "))
    return count

def input_course_information(num_courses):
    for i in range(num_courses):
        print(f"\n--- Course {i + 1} ---")
        course_id = input("Enter Course ID: ").strip()
        course_name = input("Enter Course Name: ").strip()
        courses.append((course_id, course_name))
        marks[course_id] = {}

def input_marks_for_course():
    if not courses:
        print("No courses available. Please add courses first.")
        return
    if not students:
        print("No students available. Please add students first.")
        return

    list_courses()
    course_id = input("\nSelect a course ID to enter marks for: ").strip()

    # Check if course exists
    course_exists = any(c[0] == course_id for c in courses)
    if not course_exists:
        print("Course ID not found!")
        return

    print(f"\n--- Enter Marks for Course: {course_id} ---")
    for student_id, name, _ in students:
        mark = float(input(f"Enter mark for {name} (ID: {student_id}): "))
        marks[course_id][student_id] = mark


# --- Listing Functions ---

def list_courses():
    print("\n================ LIST OF COURSES ================")
    if not courses:
        print("No courses available.")
        return
    for course_id, name in courses:
        print(f"ID: {course_id:<10} Name: {name}")

def list_students():
    print("\n================ LIST OF STUDENTS ===============")
    if not students:
        print("No students available.")
        return
    for student_id, name, dob in students:
        print(f"ID: {student_id:<10} Name: {name:<20} DoB: {dob}")

def show_student_marks_for_course():
    if not courses:
        print("No courses available.")
        return

    list_courses()
    course_id = input("\nEnter Course ID to view marks: ").strip()

    if course_id not in marks or not marks[course_id]:
        print("No marks recorded for this course.")
        return

    print(f"\n=========== MARKS FOR COURSE: {course_id} ===========")
    for student_id, mark in marks[course_id].items():
        # Find student name from students list
        student_name = next((s[1] for s in students if s[0] == student_id), "Unknown")
        print(f"Student ID: {student_id:<10} Name: {student_name:<20} Mark: {mark}")


# --- Main Menu System ---

def main():
    # Step 1: Initialize class structure
    num_students = input_number_of_students()
    input_student_information(num_students)

    num_courses = input_number_of_courses()
    input_course_information(num_courses)

    # Step 2: Interactive Menu
    while True:
        print("\n" + "="*40)
        print("      STUDENT MARK MANAGEMENT MENU      ")
        print("="*40)
        print("1. List Courses")
        print("2. List Students")
        print("3. Enter Marks for a Course")
        print("4. Show Student Marks for a Course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            list_courses()
        elif choice == '2':
            list_students()
        elif choice == '3':
            input_marks_for_course()
        elif choice == '4':
            show_student_marks_for_course()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-5.")

if __name__ == "__main__":
    main()