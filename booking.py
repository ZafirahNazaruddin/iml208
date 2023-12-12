import tkinter as tk
import datetime
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import timedelta, datetime, date

root = tk.Tk()
root.title('Pet Hotel Booking System')
root.configure(bg='#000000')

registrations = []

def register():
    pet_name = pet_name_entry.get()
    room_num = room_num_entry.get()
    check_in_date = check_in_date_entry.get()
    check_out_date = check_out_date_entry.get()

    date_format = "%Y-%m-%d"
    a = datetime.strptime(check_in_date, date_format)
    b = datetime.strptime(check_out_date, date_format)

    delta = b - a
    diff_date = delta.days
    price_value = diff_date * 50

    if not pet_name or not room_num or not check_in_date or not check_out_date:
        messagebox.showerror("Error", "Please fill in the required fields.")
    else:
        registration = {
            "pet_name": pet_name,
            "room_num": room_num,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date,
            "price": price_value
        }
        registrations.append(registration)
        update_registration_list()
        clear_fields()
        messagebox.showinfo("Booking Successful", "Thank you for booking with us!")

def clear_fields():
    pet_name_entry.delete(0, tk.END)
    room_num_entry.delete(0, tk.END)

def update_registration_list():
    registration_list.delete(0, tk.END)
    for i, registration in enumerate(registrations, start=1):
        registration_list.insert(tk.END, f"Booking {i}: "
            f"Name: {registration['pet_name']}  |  Room Number: {registration['room_num']}  |  "
            f"Check In: {registration['check_in_date']}  |  Check Out: {registration['check_out_date']} | Price: RM {registration['price']}")

def delete_registration():
    selected_index = registration_list.curselection()
    if selected_index:
        index = selected_index[0]
        registrations.pop(index)
        update_registration_list()

def edit_registration():
    selected_index = registration_list.curselection()
    if selected_index:
        index = selected_index[0]
        registration = registrations[index]
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Registration")
        edit_window.configure(bg='#000000')
        
        pet_name_label = tk.Label(edit_window, text="Pet Name:", font=("Arial", 16), bg='#000000', fg='#F0ECE5')
        pet_name_label.grid(row=1, column=1, columnspan=1, padx=5, pady=5)
        
        pet_name_edit = tk.Entry(edit_window, font=("Arial", 16))
        pet_name_edit.insert(0, registration["pet_name"])
        pet_name_edit.grid(row=1, column=2, columnspan=1, padx=5, pady=5)
        
        room_num_label = tk.Label(edit_window, text="Room Number:", font=("Arial", 16), bg='#000000', fg='#F0ECE5')
        room_num_label.grid(row=2, column=1, padx=5, pady=5)
        
        room_num_edit = tk.Entry(edit_window, font=("Arial", 16))
        room_num_edit.insert(0, registration["room_num"])
        room_num_edit.grid(row=2, column=2, padx=5, pady=5)
        
        check_in_date_label = tk.Label(edit_window, text="Check In:", font=("Arial", 16), bg='#000000', fg='#F0ECE5')
        check_in_date_label.grid(row=3, column=1, padx=5, pady=5)
        
        check_in_date_edit = tk.Entry(edit_window, font=("Arial", 16))
        check_in_date_edit.insert(0, registration["check_in_date"])
        check_in_date_edit.grid(row=3, column=2, padx=5, pady=5)
        
        check_out_date_label = tk.Label(edit_window, text="Check Out:", font=("Arial", 16), bg='#000000', fg='#F0ECE5')
        check_out_date_label.grid(row=4, column=1, padx=5, pady=5)
        
        check_out_date_edit = tk.Entry(edit_window, font=("Arial", 16))
        check_out_date_edit.insert(0, registration["check_out_date"])
        check_out_date_edit.grid(row=4, column=2, padx=5, pady=5)

        def save_changes():
            registration["pet_name"] = pet_name_edit.get()
            registration["room_num"] = room_num_edit.get()
            registration["check_in_date"] = check_in_date_edit.get()
            registration["check_out_date"] = check_out_date_edit.get()

            date_format = "%Y-%m-%d"
            a = datetime.strptime(registration["check_in_date"], date_format)
            b = datetime.strptime(registration["check_out_date"], date_format)

            delta = b - a
            diff_date_edit = delta.days
            price_value_edit = diff_date_edit * 50

            registration["price"] = price_value_edit
            edit_window.destroy()
            update_registration_list()
        
        save_button = tk.Button(edit_window, text="Save Changes", command=save_changes, font=("Arial", 15), bg="#FDB0C0", fg="#000000")
        save_button.grid(row=5, column=1, columnspan=2, padx=10,  pady=10,  ipadx=5)

frame = tk.Frame(bg='#30D5C8')

#Title
title_label = tk.Label(root, text="Pet Hotel Booking System", bg='#000000', fg='#B6BBC4', font=('Arial', 30))
title_label.grid(row=0, column=0, columnspan=10, padx=20, pady=20)

#Label
pet_name_label = tk.Label(root, text="Pet Name:", bg='#000000', fg='#F0ECE5', font=('Arial', 16))
pet_name_label.grid(row=1, column=0, padx=10, pady=10)

room_num_label = tk.Label(root, text="Room Number:", bg='#000000', fg='#F0ECE5', font=('Arial', 16))
room_num_label.grid(row=2, column=0, padx=10, pady=10)

check_in_date_label = tk.Label(root, text="Check In:", bg='#000000', fg='#F0ECE5', font=('Arial', 16))
check_in_date_label.grid(row=3, column=0, padx=10, pady=10)

check_out_date_label = tk.Label(root, text="Check Out:", bg='#000000', fg='#F0ECE5', font=('Arial', 16))
check_out_date_label.grid(row=4, column=0, padx=10, pady=10)

#Entry
pet_name_entry = tk.Entry(root, font=("Arial", 16), width=22)
pet_name_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

room_num_entry = tk.Spinbox(root, font=("Arial", 16), from_=1, to=5, width=20)
room_num_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

check_in_date_entry = DateEntry(root, font=("Arial", 16), width=20, date_pattern = 'yyyy-mm-dd')
check_in_date_entry.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

check_out_date_entry = DateEntry(root, font=("Arial", 16), width=20, date_pattern = 'yyyy-mm-dd')
check_out_date_entry.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

#Button
register_button = tk.Button(root, text="Enter", bg="#FDB0C0", fg="#000000", font=("Arial", 16), width=8, command=register)
register_button.grid(row=5, column=0, columnspan=1, padx=5,  pady=5,  ipadx=10, sticky = 'e')

edit_button = tk.Button(root, text="Edit", bg="#FDB0C0", fg="#000000", font=("Arial", 16), width=8, command=edit_registration)
edit_button.grid(row=5, column=1, columnspan=1, padx=5,  pady=5,  ipadx=10)

delete_button = tk.Button(root, text="Delete", bg="#FDB0C0", fg="#000000", font=("Arial", 16), width=8, command=delete_registration)
delete_button.grid(row=5, column=2, columnspan=1, padx=5,  pady=5,  ipadx=10)

#List
registration_list = tk.Listbox(root, selectmode=tk.SINGLE, font=("Arial", 12), bg='#FDB0C0', fg='#000000', width=90, height=14)
registration_list.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

update_registration_list()

root.mainloop()