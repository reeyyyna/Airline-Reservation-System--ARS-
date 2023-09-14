import random, csv
from tkinter import *
from tkinter import messagebox
from first_frame import *

main = Tk()
main.title("Airline Reservation System")
main.geometry("1000x500")


canvas = Canvas(main, width=300)
canvas.pack(fill=BOTH, expand=True)

# Main Frame
main_frame = Frame(canvas)
canvas.create_window((0,0), window=main_frame, anchor=NW)

# Horizontal Scrollbar
xscrollbar = Scrollbar(main, orient=HORIZONTAL, command=canvas.xview)
xscrollbar.pack(side=BOTTOM, fill=X)
canvas.configure(xscrollcommand=xscrollbar.set)

# Vertical Scrollbar
yscrollbar = Scrollbar(main, orient=VERTICAL, command=canvas.yview)
yscrollbar.pack(side=LEFT, fill=Y)
canvas.configure(yscrollcommand=yscrollbar.set)


button1 = Button(main, text="Seat Map", relief="raise", activeforeground="white", activebackground="red", justify="center")
button2 = Button(main, text="Reserve Seat", relief="raise", activeforeground="white", activebackground="red", justify="center")
button3 = Button(main, text="Cancel Reservation", relief="raise", activeforeground="white", activebackground="red", justify="center")
button4 = Button(main, text="Flight Information", relief="raise", activeforeground="white", activebackground="red", justify="center")
button5 = Button(main, text="Refresh System", relief="raise", activeforeground="white", activebackground="red", justify="center")  # hidden to the users


button1.place(x=80, y=50)
button2.place(x=180, y=50)  
button3.place(x=320, y=50)  
button4.place(x=520, y=50)  
button5.place(x=720, y=50)  

# Update the canvas scrolling region
main_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

main.mainloop()

