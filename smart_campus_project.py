# SMART CAMPUS INFORMATION SYSTEM
# Mini Project Integration (Lab 1 to Lab 8)
import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = {}

# === FUNCTION : CALCULATE GRADE ===

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

# FUNCTION : REGISTER STUDENT ---


def register_student():
    usn = input("Enter Student USN: ")

    if usn in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    semester = input("Enter Semester: ")

    marks = []

    print("\nEnter marks for 5 subjects:")

    for i in range(5):
        mark = int(input(f"Subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)

    students[usn] = {
        "Name": name,
        "Department": dept,
        "Semester": semester,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade,
        "Courses": []
    }

    print("\nStudent Registered Successfully!")

# FUNCTION : DISPLAY STUDENTS
# ============================================

def display_students():

    if not students:
        print("No student records found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for usn, details in students.items():

        print("\nUSN:", usn)
        print("Name:", details["Name"])
        print("Department:", details["Department"])
        print("Semester:", details["Semester"])
        print("Marks:", details["Marks"])
        print("Total:", details["Total"])
        print("Average:", round(details["Average"], 2))
        print("Grade:", details["Grade"])
        print("Courses:", details["Courses"])

# FUNCTION : COURSE ENROLLMENT
# ============================================

def enroll_course():

    courses = [
        "Python Programming",
        "Data Structures",
        "Artificial Intelligence",
        "Machine Learning",
        "Cyber Security"
    ]

    usn = input("Enter Student USN: ")

    if usn not in students:
        print("Student not found!")
        return

    print("\nAvailable Courses:")

    for i, course in enumerate(courses, start=1):
        print(i, ".", course)

    choice = int(input("Select Course Number: "))

    if choice < 1 or choice > len(courses):
        print("Invalid Choice!")
        return

    selected_course = courses[choice - 1]

    if selected_course in students[usn]["Courses"]:
        print("Course already enrolled!")
    else:
        students[usn]["Courses"].append(selected_course)
        print("Course Enrolled Successfully!")

# FUNCTION : SEARCH STUDENT---

def search_student():

    usn = input("Enter USN to Search: ")

    if usn in students:
        details = students[usn]

        print("\nStudent Found!")
        print("Name:", details["Name"])
        print("Department:", details["Department"])
        print("Grade:", details["Grade"])

    else:
        print("Student not found!")

# FUNCTION : SORT STUDENTS ====

def sort_students():

    if not students:
        print("No records available.")
        return

    sorted_data = sorted(
        students.items(),
        key=lambda x: x[1]["Average"],
        reverse=True
    )

    print("\n===== STUDENTS SORTED BY AVERAGE =====")

    for usn, details in sorted_data:
        print(usn, "-", details["Name"],
              "-", round(details["Average"], 2))

# FUNCTION : FEE CALCULATION===

def calculate_fee():

    course_fee = float(input("Enter Course Fee: "))
    scholarship = float(input("Enter Scholarship Amount: "))

    final_fee = course_fee - scholarship

    if final_fee < 0:
        final_fee = 0

    print("Final Fee to Pay =", final_fee)


# FUNCTION : SAVE RECORDS TO FILE

def save_to_file():

    with open("student_records.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "USN",
            "Name",
            "Department",
            "Semester",
            "Average",
            "Grade"
        ])

        for usn, details in students.items():

            writer.writerow([
                usn,
                details["Name"],
                details["Department"],
                details["Semester"],
                details["Average"],
                details["Grade"]
            ])

    print("Records saved successfully!")


# FUNCTION : LOAD FILE===

def load_file():

    try:
        with open("student_records.csv", "r") as file:
            print("\n===== FILE CONTENT =====")

            reader = csv.reader(file)

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("File not found!")

# FUNCTION : DIRECTORY SCANNING---

def scan_directory():

    path = "."

    try:
        files = os.listdir(path)

        print("\n===== DIRECTORY FILES =====")

        for file in files:
            print(file)

    except Exception as e:
        print("Error:", e)


# FUNCTION : PERFORMANCE ANALYTICS---

def performance_analytics():

    if not students:
        print("No student data available.")
        return

    names = []
    averages = []

    for usn, details in students.items():
        names.append(details["Name"])
        averages.append(details["Average"])

    # NUMPY ANALYSIS
    avg_marks = np.mean(averages)
    highest = np.max(averages)
    lowest = np.min(averages)

    print("\n===== PERFORMANCE ANALYTICS =====")

    print("Class Average =", round(avg_marks, 2))
    print("Highest Average =", highest)
    print("Lowest Average =", lowest)

    # PANDAS DATAFRAME
    df = pd.DataFrame({
        "Students": names,
        "Average Marks": averages
    })

    print("\nData Analysis Table:")
    print(df)

    # MATPLOTLIB GRAPH
    plt.bar(names, averages)

    plt.title("Student Performance Analysis")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")

    plt.show()

# MAIN MENU
# ==========

while True:

    print("\n================================")
    print(" SMART CAMPUS INFORMATION SYSTEM ")
    print("================================")

    print("1. Register Student")
    print("2. Display Students")
    print("3. Enroll Course")
    print("4. Search Student")
    print("5. Sort Students")
    print("6. Fee Calculation")
    print("7. Save Records to File")
    print("8. Load File Records")
    print("9. Directory Scanning")
    print("10. Performance Analytics")
    print("11. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        enroll_course()

    elif choice == "4":
        search_student()

    elif choice == "5":
        sort_students()

    elif choice == "6":
        calculate_fee()

    elif choice == "7":
        save_to_file()

    elif choice == "8":
        load_file()

    elif choice == "9":
        scan_directory()

    elif choice == "10":
        performance_analytics()

    elif choice == "11":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")
        