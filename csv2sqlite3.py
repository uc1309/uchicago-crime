# Import necessary libraries
import sqlite3
import csv

# Connecting/creating database
conn = sqlite3.connect('test.db')
c = conn.cursor()

# Initialize ID list
id = 0

# Create crimes table
c.execute('''CREATE TABLE crimes ( id INT, Incident TEXT, Location TEXT, Reported TEXT, Occured TEXT, Comments TEXT, Disposition TEXT, UCPDI TEXT )''')

# Insert data from CSV file into SQLite3 database
with open('crime.csv', newline = '') as csvfile:
    next(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for row in spamreader:
        id += 1
        c.execute('INSERT INTO crimes VALUES (?,?,?,?,?,?,?,?)', [id] + row)

# Save changes
conn.commit()

# Close connection
conn.close()

