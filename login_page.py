import tkinter as tk

# Function to check login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the provided username and password are correct (you can replace this with your own authentication logic)
    if username == "admin" and password == "password":
        message_label.config(text="Login successful")
        # Add code to open the admin panel here
    else:
        message_label.config(text="Login failed. Try again.")

# Create the main window
root = tk.Tk()
root.title("Admin Panel")

# Create and configure widgets
username_label = tk.Label(root, text="Username")
password_label = tk.Label(root, text="Password")
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")  # Passwords are hidden
login_button = tk.Button(root, text="Login", command=login)
message_label = tk.Label(root, text="")

# Grid layout for widgets
username_label.grid(row=0, column=0)
password_label.grid(row=1, column=0)
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
login_button.grid(row=2, column=1)
message_label.grid(row=3, column=0, columnspan=2)

# Start the GUI main loop
root.mainloop()
