# Create a program that takes a list of students and sstore them in file.Then read the file and display the content.

name = input("Enter the name of the student: ")
with open("students.txt", "a") as file:
    for i in range(name):
        name = input("Enter the name of the student: ")
        file.write(name + "\n")

print("\n  The list of students is:")
with open("students.txt", "r") as file:
    print(file.read())
