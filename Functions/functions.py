import random, csv

ROWS = 10
COLS = 6
SEAT_PLAN = [['_' for _ in range(COLS)] for _ in range(ROWS)]

# Function to display the seat map
def seat_map():
	print("\nCurrent Seat Plan:\n")
	print("  A B C D E F")
	for rows in range(ROWS):
		print(rows + 1, ends=" ") 
		for cols in range(COLS):
			print(SEAT_PLAN[rows][cols], ends=" ")
		print()

# Function to display or save the passengers' details
def seat_passenger_details():
	pass 

# Function to determine the availability of a seat
def seat_availability(rows, cols):
	return SEAT_PLAN[rows][cols] == '_' 

# Function to determine the reserve seat
def seat_reservation(rows, cols):
	return SEAT_PLAN[rows][cols] == 'X'

# Function that deals with the cancellation of reservation
def seat_cancellation():
	pass 

# Function to post the allotted time 
def seat_time_date():
	time_date_choices = { 1: "Tue 05 September 2023 8:00 AM", 2: "Wed 06 September 2023 10:00 AM", 
	3: "Thu 07 September 2023 13:00 PM"}

	print("\nTime and Date of Flight choices: ")
	for key, value in time_date_choices.items():
		print(f"[{key}] {value}")

	choices = int(input("\nEnter the choice for the time and date: "))

	return choices

# Function to determine the seat type
def seat_type():
	seat_choices = {1: "Economy", 2: "Premium Economy", 3: "Business", 4: "First Class"} 

	print("\nType of Seat choices: ")
	for key, value in seat_choices.items():
		print(f"[{key}] {value}")

	choices = int(input("\nEnter the choice for the seat type: "))

	return choices 

# Function to determine the flight type
def flight_type():
	flight_choices = {1: "Direct", 2: "Connecting", 3: "Charter"}

	print("\nFlight Type choices: ")
	for key, value in flight_choices.items():
		print(f"[{key}] {value}")

	choices = int(input("\nEnter the choice for the flight type: "))

	return choices

# Function to search the information of the passengers
def search_seat():
	pass 

# Function to refresh the data in the csv file
def refresh_file():
	pass
