# Import necessary libraries
import csv
import sqlite3

# Open connection, create cursor
conn = sqlite3.connect('test.db')
c = conn.cursor()

# In case of error, uncomment to erase faulty table
# c.execute('''DROP TABLE times''')
# c.execute('''DROP TABLE incidents''')

# Create incidents and times tables to filter results by incident type and time in SQLite3 queries
c.execute('''CREATE TABLE incidents ( id INT, type TEXT )''')
c.execute('''CREATE TABLE times (id INT, month INT, day INT, year INT, hour INT, minute INT )''')

# Initialize ID list
id = 0

# Insert incident data from CSV into database
with open('crime.csv', newline = '') as csvfile:
    next(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for row in spamreader:
        id += 1
        labels = row[0].split(' / ')
        for label in labels:
            iterable = [id, label.strip().lower()]
            #c.execute('INSERT INTO incidents VALUES (?,?)', iterable)

# Initialize ID list   
id = 0        
  
# Insert time data from CSV into database          
with open('crime.csv', newline = '') as csvfile:
    next(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for row in spamreader:
        id += 1
        date = row[2].split(' ')[0].strip().split('/')
        time = row[2].split(' ')[1].strip().split(':')
        if len(time) < 2:
            time = row[2].split(' ')[1].strip().split(';')
        c.execute('INSERT INTO times VALUES (?,?,?,?,?,?)', [id] + date + time)
        holder = [id] + date + time
        
# Save changes and close connection
conn.commit()
conn.close()