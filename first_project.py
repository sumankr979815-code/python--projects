print("\n***** WELCOME TO STUDENT MANAGEMENT SYSTEM *****\n")

# student list
l = ["shanti", "sonam", "ashish"]

# view student list
def view_list():
    if len(l) == 0:
        print("No record found.")
    else:
        for i in range(len(l)):
            print(l[i])

# add new student
def add_data():
    x = input("Enter the name: ")
    l.append(x)
    print("Name added successfully...")

# remove student
def remove_data():
    name = input("Enter the name to remove: ")
    if name in l:
        l.remove(name)
        print("Record deleted successfully...")
    else:
        print("Name not found...")

# search student
def search_data():
    name = input("Enter the name to search: ")
    if name in l:
        print("Record found:", name)
    else:
        print("Record not found...")

# main program
while True:
    print("\nPlease choose any one options:")
    print("1. To view student list")
    print("2. To add new list")
    print("3. To remove the data")
    print("4. To search data")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        view_list()

    elif choice == 2:
        add_data()

    elif choice == 3:
        remove_data()

    elif choice == 4:
        search_data()

    elif choice == 5:
        print("Thank you for using Student Management System")
        break

    else:
        print("Invalid choice...")

    ch = input("\nDo U Continue this (y/n): ")
    if ch.lower() != 'y':
        break
