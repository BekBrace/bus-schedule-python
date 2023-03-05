import sqlite3

# Define the database connection and cursor
conn = sqlite3.connect("bus_schedule.db")
c = conn.cursor()

# Create the bus schedule table if it does not already exist
c.execute("CREATE TABLE IF NOT EXISTS schedule (time TEXT PRIMARY KEY, route TEXT)")

# Populate the initial bus schedule in the database if it is empty
if not c.execute("SELECT * FROM schedule").fetchall():
    bus_schedule = [
        ("8:00am", "Route 1"),
        ("9:30am", "Route 2"),
        ("11:00am", "Route 3"),
        ("1:00pm", "Route 1"),
        ("2:30pm", "Route 2"),
        ("4:00pm", "Route 3"),
    ]
    c.executemany("INSERT INTO schedule (time, route) VALUES (?, ?)", bus_schedule)
    conn.commit()

# Print the heading using Figlet
heading = ("Bus Schedule")
print(heading)

# Print the current schedule from the database using Chalk
print("Current bus schedule:")
for row in c.execute("SELECT * FROM schedule"):
    print((row[0]) + ": " + (row[1]))

# Allow data entry of new bus routes and times and update the database
while True:
    user_input = input("\nEnter a new bus route and time (e.g. '5:00pm Route 4'), or press enter to quit: ")
    if user_input == "":
        break
    try:
        time, route = user_input.split(" ")
        c.execute("SELECT * FROM schedule WHERE time = ?", (time,))
        if c.fetchone() is not None:
            print("Error: There is already a bus route scheduled for that time.")
        else:
            c.execute("INSERT INTO schedule (time, route) VALUES (?, ?)", (time, route))
            conn.commit()
            print("New bus route added successfully!")
    except ValueError:
        print("Error: Invalid input. Please enter the bus route and time in the correct format.")

# Print the updated schedule from the database using Chalk
print("\nUpdated bus schedule:")
for row in c.execute("SELECT * FROM schedule"):
    print((row[0]) + ": " + (row[1]))

# Close the database connection
conn.close()