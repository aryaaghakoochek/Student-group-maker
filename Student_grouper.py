# Imports list and shuffles it (happens later on)
from random import shuffle

import good as good

n = 0

# Asks for number of students from user
num_of_students: float = float(input("How many students are in this class? Please keep it an even number (1-30):"))
# If any of these statements are true it will ask restart and ask you to input code again
while num_of_students < 1 or num_of_students > 30 or num_of_students % 2 != 0:
    num_of_students = float(input("How many students are in this class? Please keep it an even number (1-30):"))

# Tells user to input x number of names
student_names = str(input("Please enter " + str(int(num_of_students)) + " student names separated by commas and spaces:").upper())
student_names: str = student_names.replace(" ", "")


# Splits the string of student names at the commas and returns a list containing the names
students = student_names.split(',')

# will only accept names if it is the same number as you inputted at the beginning
while len(students) != num_of_students:
    # Will tell you to enter less names if you have entered more then stated
    if len(students) > num_of_students:
        print("You have entered too many names, please make sure student names are separated by commas and spaces:")
        student_names = str(input("Please enter " + str(int(num_of_students)) + " student names separated by commas:"))
        student_names = student_names.replace(" ", "")
        students = student_names.split(',')
    # Will tell you to enter more names if you have entered more then stated
    else:
        print('You have not entered enough names, please make sure student names are separated by commas and spaces:')
        student_names = str(input("Please enter " + str(int(num_of_students)) + " student names separated by commas:"))
        student_names = student_names.replace(" ", "")
        students = student_names.split(',')

# Randomizes the names you have put in
shuffle(students)

# This while loop iterates through the list containing all the student names and prints out two student names at a time
# i gets increased by 2 because we are printing out two students at a time
i = 0
print("Here are your groups of 2:")
while i < len(students):
    print(str(students[i]) + " and " + str(students[i + 1] + " are together"))
    i = i + 2

print("Thank you for using the Arya.Group.Generator.3000!")


