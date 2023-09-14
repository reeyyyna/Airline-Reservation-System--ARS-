import tkinter as tk
from tkinter import messagebox

def open_main_frame():
    # Code to open the main frame goes here
    main_frame = tk.Toplevel(main)
    main_frame.title("Main Frame")

def sign_in():
    # Add your sign-in logic here
    if sign_in_successful:  # Replace with your sign-in validation
        open_main_frame()
    else:
        messagebox.showerror("Error", "Sign-in failed. Please try again.")

def sign_up():
    # Add your sign-up logic here
    if sign_up_successful:  # Replace with your sign-up validation
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

label1.place(x=20, y=20)
label2.place(x=20, y=50)
label3.place(x=20, y=80)

entry1.place(x=120, y=20)
entry2.place(x=120, y=50)
entry3.place(x=120, y=80)

first_button.place(x=20, y=120)
second_button.place(x=120, y=120)

main.mainloop()
