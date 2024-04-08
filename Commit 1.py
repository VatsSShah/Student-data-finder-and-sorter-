print("-----Program for Student Information-----")

D = dict()

n = int(input('How many student records do you want to store? '))

# Add student information to the dictionary
for i in range(0, n):
    name = tuple(input("Enter the complete name (First and last name) of the student: ").split())
    contact = input("Enter contact number: ")
    marks = input('Enter Marks: ')
    D[name] = (contact, marks)

# Define a function for sorting names based on the first name
def sort():
    ls = sorted(D.keys(), key=lambda x: x[0])
    for i in ls:
        print(i[0], i[1])
    return

# Define a function for finding the minimum marks in stored data
def minmarks():
    marks_list = [int(details[1]) for details in D.values()]
    print("Minimum marks:", min(marks_list))
    return

# Define a function for searching student contact number
def searchdetail(fname):
    for name, details in D.items():
        if name[0] == fname:
            print(details[0])
            return
    print("No student found with the given first name.")
    return

# Define a function for asking the options
def option():
    while True:
        choice = int(input('Enter the operation detail: \n \
        1: Sorting using first name \n \
        2: Finding Minimum marks \n \
        3: Search contact number using first name \n \
        4: Exit\n \
        Option: '))

        if choice == 1:
            sort()
        elif choice == 2:
            minmarks()
        elif choice == 3:
            first_name = input('Enter first name of student: ')
            searchdetail(first_name)
        elif choice == 4:
            print('Thanks for executing me!!!!')
            break
        else:
            print('Invalid option. Please try again.')

        inp = input('Want to perform some other operation? Y or N: ')
        if inp != 'Y':
            print('Thanks for executing me!!!!')
            break

option()
