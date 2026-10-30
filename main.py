students = {}

def add_student():
    sid = input("Enter Student ID: ")

    if sid in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students[sid] = {
        "name": name,
        "age": age,
        "course": course
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found!")
        return

    for sid, details in students.items():
        print("\nStudent ID:", sid)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Course:", details["course"])


def search_student():
    sid = input("Enter Student ID to search: ")

    if sid in students:
        print("Student Details:", students[sid])
    else:
        print("Student not found!")


def update_student():
    sid = input("Enter Student ID to update: ")

    if sid in students:
        students[sid]["name"] = input("Enter new name: ")
        students[sid]["age"] = input("Enter new age: ")
        students[sid]["course"] = input("Enter new course: ")
        print("Student updated successfully!")
    else:
        print("Student not found!")


def delete_student():
    sid = input("Enter Student ID to delete: ")

    if sid in students:
        del students[sid]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")