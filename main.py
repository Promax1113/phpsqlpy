import sqlite3

# Get the data from the text file
with open('textfile.txt') as f:
    data = f.readlines()

# Write the data to the CSV file
with open('output.csv', 'w') as csvfile:
    for line in data:
        # Get the line from the text file
        line = line.strip()
        
        # Write the line to the CSV file
        csvfile.write(line + '\n')

# Open a connection to the database
conn = sqlite3.connect('my_database.db')

# Create a cursor
cursor = conn.cursor()

# Read the SQL file
with open('file.sql', 'r') as f:
    sql = f.read()

# Execute the SQL commands
cursor.executescript(sql)

# Close the connection
conn.close()

