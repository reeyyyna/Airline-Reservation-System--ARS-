import tkinter as tk
from tkinter import messagebox
import mysql.connector

# storage_info = "user_info.txt"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iamquennie16??",
    database="sys",
    auth_plugin="mysql_native_password")


mycursor = mydb.cursor()

# Create the users table if it doesn't exist
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        province VARCHAR(255),
        municipality VARCHAR(255),
        brgy VARCHAR(255),
        street_address VARCHAR(255)
    )
""")


def open_main_frame():
    main.deiconify()


def sign_in():  
    fname = entry1.get().strip()
    lname = entry2.get().strip()
    age = entry3.get().strip()

    # Query the database for the user
    sql = "SELECT * FROM users WHERE first_name = %s AND last_name = %s AND age = %s"
    val = (fname, lname, age)

    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        open_main_frame()
    else:
        messagebox.showerror("Error", "Sign-in failed. Please try again.")

   

def sign_up():

    main.withdraw()

    sub = tk.Toplevel()
    sub.title("Sign-up")
    sub.geometry("500x500")

    sign_up_info = tk.Frame(sub)
    sign_up_info.pack()


    def proceed():
        fname = fname_entry.get()
        lname = lname_entry.get()
        age = age_entry.get()
        province = province_entry.get()
        municipality = municipality_entry.get()
        brgy = brgy_entry.get()
        street = street_entry.get()
        

        # Insert the user information into the database
        sql = "INSERT INTO users (first_name, last_name, age, province, municipality, brgy, street_address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (fname, lname, age, province, municipality, brgy, street)

        mycursor.execute(sql, val)
        mydb.commit()  # Commit the changes to the database

        messagebox.showinfo("Success", "Sign-up Successfully!")
        sub.destroy()
        open_main_frame() 

    def cancel():
        response = messagebox.askyesno("Cancel Sign-up", "Are you sure to exit?")
        if response:
            sub.destroy()
            open_main_frame()

    # Labels
    fname_label = tk.Label(sign_up_info, text="First Name")
    lname_label = tk.Label(sign_up_info, text="Last Name")
    age_label = tk.Label(sign_up_info, text="Age")
    province_label = tk.Label(sign_up_info, text="Province")
    municipality_label = tk.Label(sign_up_info, text="Municipality")
    brgy_label = tk.Label(sign_up_info, text="Barangay")
    street_label = tk.Label(sign_up_info, text="Street Address")

    # Entries
    fname_entry = tk.Entry(sign_up_info, bd=10)
    lname_entry = tk.Entry(sign_up_info, bd=10)
    age_entry = tk.Entry(sign_up_info, bd=10)
    province_entry = tk.Entry(sign_up_info, bd=10)
    municipality_entry = tk.Entry(sign_up_info, bd=10)
    brgy_entry = tk.Entry(sign_up_info, bd=10)
    street_entry = tk.Entry(sign_up_info, bd=10)

    # Button
    proceed = tk.Button(sign_up_info, text="Proceed", command=proceed)
    cancel = tk.Button(sign_up_info, text="Cancel", command=cancel)

    # Layout
    row_num = 0
    fname_label.grid(row=row_num, column=0, padx=10, pady=5, sticky="e")
    fname_entry.grid(row=row_num, column=1, padx=10, pady=5)

    row_num += 1
    lname_label.grid(row=row_num, column=0, padx=10, pady=5, sticky="e")
    lname_entry.grid(row=row_num, column=1, padx=10, pady=5)

    row_num += 1
    age_label.grid(row=row_num, column=0, padx=10, pady=5, sticky="e")
    age_entry.grid(row=row_num, column=1, padx=10, pady=5)

    row_num += 1
    province_label.grid(row=row_num, column=0, padx=10, pady=5, sticky="e")
    province_entry.grid(row=row_num, column=1, padx=10, pady=5)

    row_num += 1
    municipality_label.grid(row=row_num, column=0, padx=10, pady=5, sticky="e")
    municipality_entry.grid(row=row_num, column=1, padx=10, pady=5)

    row_num += 1
    brgy_label.grid(row=row_num, column=0, padx=10, pady=5, sticky="e")
    brgy_entry.grid(row=row_num, column=1, padx=10, pady=5)

    row_num += 1
    street_label.grid(row=row_num, column=0, padx=10, pady=5, sticky="e")
    street_entry.grid(row=row_num, column=1, padx=10, pady=5)

    row_num += 1
    proceed.grid(row=row_num, column=0, columnspan=2, padx=10, pady=10)
    cancel.grid(row=row_num, column=1, columnspan=2, padx=10, pady=10)

    sub.protocol("WM_DELETE_WINDOW", open_main_frame)



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
