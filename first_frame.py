import tkinter as tk
from tkinter import messagebox

def open_main_frame():
    # Code to open the main frame goes here
    main_frame = tk.Toplevel(main)
    main_frame.title("Main Frame")

def sign_in():  
    fname = entry1.get()
    lname = entry2.get()
    age = entry3.get()
 
    if fname == "Quennie" and lname == "Soberano" and age == 20:
        open_main_frame()
    else:      
        messagebox.showerror("Error", "Sign-in failed. Please try again.")

def sign_up():
    fname = entry1.get()
    lname = entry2.get()
    age = entry3.get()

    if fname == "Quennie" and lname == "Soberano" and age == 20:
        open_main_frame()
    else:
        messagebox.showerror("Error", "Sign-up failed. Please try again.")

main = tk.Tk()
main.title("Sign-in/Sign-up")
main.geometry("500x500")

# Login Frame
login_frame = tk.Frame(main)
login_frame.pack()

label1 = tk.Label(login_frame, text="First Name")
label2 = tk.Label(login_frame, text="Last Name")
label3 = tk.Label(login_frame, text="Email")

entry1 = tk.Entry(login_frame, bd=10)
entry2 = tk.Entry(login_frame, bd=10)
entry3 = tk.Entry(login_frame, bd=10)

first_button = tk.Button(login_frame, text="Sign-in", command=sign_in)
second_button = tk.Button(login_frame, text="Sign-up", command=sign_up)

label1.grid(row=0, column=0, padx=20, pady=10, sticky="w")
label2.grid(row=1, column=0, padx=20, pady=10, sticky="w")
label3.grid(row=2, column=0, padx=20, pady=10, sticky="w")

entry1.grid(row=0, column=1, padx=20, pady=10)
entry2.grid(row=1, column=1, padx=20, pady=10)
entry3.grid(row=2, column=1, padx=20, pady=10)

first_button.grid(row=3, column=0, columnspan=2, pady=10)
second_button.grid(row=3, column=1, columnspan=2, pady=10)

main.mainloop()
