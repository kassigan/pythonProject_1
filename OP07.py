import tkinter as tk

def say_hello():
    name = entry.get()
    label.config (text=f"Hallo, {name}!")

# window of the program with title
root = tk.Tk()
root.title("Welcome Screen")

# description what we expect from the user
label = tk.Label(root, text="Please write your name")
label.pack()

# field to enter user information
entry = tk.Entry(root) # create input field
entry.pack() #display entry field

button = tk.Button(root, text="Enter", command=say_hello)
button.pack()


root.mainloop() # display window for decent amount of time