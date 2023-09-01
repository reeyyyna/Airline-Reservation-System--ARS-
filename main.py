import random, csv

# Main Program
try: 
	while True:
		print("\n\n\t\t\t==== AIRLINE RESERVATION SYSTEM ====\n\n")
		print("\t\t\t1. Display Seat Map")
		print("\t\t\t2. Reserve a Seat")
		print("\t\t\t3. Cancel Reservation")
		print("\t\t\t4. Display Available Seats")
		print("\t\t\t5. Display Flight Information")
		print("\t\t\t6. Refresh System and CSV Data")
		print("\t\t\t7. Exit")

		choice = input("\nEnter your choice: ")

except:
	print("\nThe system execution is done.")