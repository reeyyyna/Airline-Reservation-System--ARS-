import random, csv
import tkinter
from tkinter import messagebox

main = Tk()

login_frame = Frame()

main_frame = Frame()


button1 = Button(main, text="Seat Map")
button2 = Button(main, text="Reserve Seat")
button3 = Button(main, text="Cancel Reservation")
button4 = Button(main, text="Flight Information")
button5 = Button(main, text="Refresh System")  # hidden to the users


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