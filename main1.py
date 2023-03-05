# Define the bus schedule as a dictionary
bus_schedule = {
    "8:00am": "Route 1",
    "9:30am": "Route 2",
    "11:00am": "Route 3",
    "1:00pm": "Route 1",
    "2:30pm": "Route 2",
    "4:00pm": "Route 3",
}

# Print the heading using Figlet
heading = ("Bus Schedule")
print(heading)

# Print the schedule using Chalk
for time, route in bus_schedule.items():
    print((time) + ": " + (route))
