# Get names from txt file and add to list

import csv
import random

# *** Generate student names list *****
# open file
student_names = open('9KVS_names.csv')

# Read data into a list
csv_students = csv.reader(student_names)

all_students = []
for item in csv_students:
    item = "".join(item)
    all_students.append(item)

print(all_students)
