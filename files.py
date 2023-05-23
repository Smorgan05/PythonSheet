# Load CSV
# import csv
# with open('eggs.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

# SQLite
# import sqlite3
# con = sqlite3.connect("tutorial.db")
# cur = con.cursor()
# res = cur.execute("SELECT name FROM sqlite_master")
# res.fetchone()
# res.fetchall()

# Load TXT File

# Python code to
# demonstrate readlines()
 
# L = ["Geeks\n", "for\n", "Geeks\n"]
 
# # writing to file
# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()
 
# # Using readlines()
# file1 = open('myfile.txt', 'r')
# Lines = file1.readlines()
 
# count = 0
# # Strips the newline character
# for line in Lines:
#     count += 1
#     print("Line{}: {}".format(count, line.strip()))