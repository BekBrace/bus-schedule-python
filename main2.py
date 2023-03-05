# Define the initial bus schedule as a dictionary
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

# Print the initial schedule using Chalk
for time, route in bus_schedule.items():
    print((time) + ": " + (route))

# Allow data entry of new bus routes and times
while True:
    user_input = input("\nEnter a new bus route and time (e.g. '5:00pm Route 4'), or press enter to quit: ")
    if user_input == "":
        break
    try:
        time, route = user_input.split(" ")
        if time in bus_schedule:
            print("Error: There is already a bus route scheduled for that time.")
        else:
            bus_schedule[time] = route
            print("New bus route added successfully!")
    except ValueError:
        print("Error: Invalid input. Please enter the bus route and time in the correct format.")

# Print the updated schedule using Chalk
print("\nUpdated bus schedule:")
for time, route in bus_schedule.items():
    print((time) + ": " + (route))
