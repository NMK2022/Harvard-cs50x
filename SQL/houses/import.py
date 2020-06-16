# imports data from csv spreadsheet
# accept name of csv as command line argument

from cs50 import SQL
from sys import argv
import csv

# open database
db = SQL("sqlite:///students.db")

# check that code input is valid and set-up arguments
if len(argv) < 2:
    print("Usage error, import.py characters.csv")
    exit(1)

# import csv file & account for incorrect input
with open(argv[1], "r") as students:
    reader = csv.DictReader(students)
    # parse names in each row
    for row in reader:
    # if first name, middle, and last
        name_check = row["name"].split(' ')
        # check and account for whether there is a middle name
        if len(name_check) == 3:
            # insert each student name, house, and birth into students table of students.db
            # execute values where there is a middle name into students table of students.db
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       name_check[0], name_check[1], name_check[2], row["house"], row["birth"])
        elif len(name_check) == 2:
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       name_check[0], None, name_check[1], row["house"], row["birth"])
        else:
            print("No names found")
            exit(2)
