import random
import csv


def num_check(question):
    valid = False
    while not valid:
        response = input(question)

        if response.lower() == "xxx":
            return response.lower()
        else:
            try:
                response = int(response)
                return response
            except ValueError:
                print("Please enter a valid number")


def ask_question(first, second, who):
    question = input("What is {} x {}... <press enter> ".format(first, second))
    if question == "xxx":
        return "xxx"
    ask = num_check("{}: ".format(who))
    answer = first * second

    if ask == answer:
        fdbck = random.choice(well_done)
        outcome = "right"
    else:
        fdbck = "oops - {} x {} = {}".format(first, second, answer)
        outcome = "wrong"

    print(fdbck)
    return outcome

# Get names from txt file and add to list

# *** Generate student names list *****
# open file
student_names = open('9KVS_names.csv')

# Read data into a list
csv_students = csv.reader(student_names)

# Puts names into list called 'all students'
all_students = []
for item in csv_students:
    item = "".join(item)
    all_students.append(item)

# Initialises lists
tables = []
well_done = ["great job", "well done", "ka pai", "awesome", "fantastic"]

table = ""
while table != "xxx":
    table = num_check("Choose a times table (or 'xxx' to start playing)\n  For all tables, type 0 (zero): ")

    if len(tables) <= 0 and table == "xxx":
        print("You must choose at least one table")
        table = ""
    elif table == 0:
        for item in range(2, 13):
            tables.append(item)
            table = "xxx"
    elif table != "xxx":
        tables.append(table)

do_it = ""
while do_it != "xxx":

    # Generate question and answer
    num_1 = random.choice(tables)
    num_2 = random.randint(2,12)

    # Call a student
    call_on = random.choice(all_students)

    do_it = "wrong"
    while do_it == "wrong":
        do_it = ask_question(num_1, num_2, call_on)

        if do_it == "xxx":
            break

