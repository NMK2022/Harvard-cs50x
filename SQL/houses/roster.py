# prints list of students for a given house in alphabetical order
# accept name of house as command line argument
from cs50 import SQL
from sys import argv

# check that code input is valid and set-up arguments
if len(argv) < 2:
    print("Usage error, roster.py housesort")
    exit()
# open students.db
db = SQL("sqlite:///students.db")
# execute new query to list columns you want
students_house = db.execute("SELECT * FROM students WHERE house = (?) ORDER BY last", argv[1])

# print student list in alphabetical order
for row in students_house:
    if row['middle'] != None:
        print(f"{row['first']} {row['middle']} {row['last']}, born {row['birth']}")
    else:
        print(f"{row['first']} {row['last']}, born {row['birth']}")