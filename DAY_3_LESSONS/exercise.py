# ===============================
# Student Management System
# With Functions + Loop + Quit
# ===============================

# -------- Enroll Function --------
def enroll():

    # global ka matlab hai ye variables function ke bahar bhi use honge
    global name, fname, cnic, location, classroom, course

    print("\n===== Student Enrollment =====")

    name = input("Enter student name: ")
    fname = input("Enter student father name: ")
    cnic = input("Enter student CNIC: ")
    location = input("Enter student address: ")
    classroom = input("Enter class name: ")
    course = input("Enter enrolled course: ")

    print(f"\n{name} enrolled successfully.\n")


# -------- Check Function --------
def check():

    # Agar pehle enroll nahi hua to error na aaye
    try:

        if name == "sufyan" and cnic == "1620199050921":
            print(f"\n{name} is our student.\n")
        else:
            print("\nNo, this is not our student.\n")

    except NameError:
        print("\nFirst enroll a student.\n")


# -------- Show Function --------
def showStudent():

    try:

        print("\n====== Student Record ======")
        print("Student Name      :", name)
        print("Father Name       :", fname)
        print("CNIC              :", cnic)
        print("Address           :", location)
        print("Class             :", classroom)
        print("Course            :", course)

    except NameError:
        print("\nNo student data found.\n")


# ===============================
# Main Program Loop
# ===============================

while True:

    print("\n========= MENU =========")
    print("1. Enroll")
    print("2. Check")
    print("3. Show Student")
    print("4. Quit")

    choice = input("Enter your choice: ")

    # Agar user 1 likhe
    if choice == "1":
        enroll()

    # Agar user 2 likhe
    elif choice == "2":
        check()

    # Agar user 3 likhe
    elif choice == "3":
        showStudent()

    # Agar user 4 likhe
    elif choice == "4":

        print("\nSystem Closed Successfully.")
        break      # Loop yahin khatam ho jayegi

    # Agar koi aur input de
    else:
        print("\nInvalid Choice. Try Again.")