from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Vehicle.db")
root = Tk()
root.title("Vehicles Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

regno = StringVar()
name = StringVar()
account = StringVar()
deviceid = StringVar()
email = StringVar()
contact = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Vehicles Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lblRegno = Label(entries_frame, text="Regno", font=("Calibri", 16), bg="#535c68", fg="white")
lblRegno.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtRegno = Entry(entries_frame, textvariable=regno, font=("Calibri", 16), width=30)
txtRegno.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblAccount = Label(entries_frame, text="Account", font=("Calibri", 16), bg="#535c68", fg="white")
lblAccount.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtAccount = Entry(entries_frame, textvariable=account, font=("Calibri", 16), width=30)
txtAccount.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblDeviceid = Label(entries_frame, text="Deviceid", font=("Calibri", 16), bg="#535c68", fg="white")
lblDeviceid.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txtDeviceid = Entry(entries_frame, textvariable=deviceid, font=("Calibri", 16), width=30)
txtDeviceid.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    regno.set(row[1])
    name.set(row[2])
    account.set(row[3])
    email.set(row[4])
    deviceid.set(row[5])
    contact.set(row[6])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_employee():
    if txtRegno.get() == "" or txtName.get() == "" or txtAccount.get() == "" or txtEmail.get() == "" or txtDeviceid.get() == "" or txtContact.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtRegno.get(),txtName.get(), txtAccount.get() , txtEmail.get() ,txtDeviceid.get(), txtContact.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()



def update_employee():
    if txtRegno.get() == "" or txtName.get() == "" or txtAccount.get() == "" or txtEmail.get() == "" or txtDeviceid.get() == "" or txtContact.get() == "" :
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtRegno.get(), txtName.get(), txtAccount.get(), txtEmail.get(), txtDeviceid.get(), txtContact.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    regno.set("")
    name.set("")
    account.set("")
    deviceid.set("")
    email.set("")
    contact.set("")


btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Regno")
tv.heading("3", text="Name")
tv.column("3", width=5)
tv.heading("4", text="Account")
tv.column("4", width=10)
tv.heading("5", text="Email")
tv.heading("6", text="Deviceid")
tv.column("6", width=10)
tv.heading("7", text="Contact")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
