''' Write a python code to read fron a CSV file of students marks and calculate average marks'''

import csv
total_marks = 0
count = 0
with open("students.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "marks": 85})
    writer.writerow({"name": "Bob", "marks": 90})
    writer.writerow({"name": "Charlie", "marks": 78})

with open("students.csv", "r") as file:
    reader = csv.DictReader (file)
    
    for row in reader:
        total_marks += int(row["marks"])
        count += 1

average_marks = total_marks / count
print(f"The average marks of the students is {average_marks}")