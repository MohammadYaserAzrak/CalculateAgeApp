# Calculate your age desktop app with Tkinter to make it a GUI

from tkinter import *
from tkinter import messagebox

# Create the main app window
ageApp = Tk()

# Change app text
ageApp.title("MYA Calculate Age App")

# Set dimensions
ageApp.geometry("400x200")

# Write age label
text = Label(ageApp, text="Write your age", height=2, font=("Arial", 20))
text.pack()  # Place the text into the main window

# age variable
age = StringVar()

# Set default value for age
age.set("00")

# Create the input for age
ageInput = Entry(
    ageApp, width=2, font=("Arial", 30), textvariable=age
)  # width is the # of allowed char
ageInput.pack()  # Place the input into the main window


def calc():
    ageValue = age.get()

    # Calculate time units
    months = int(ageValue) * 12
    weeks = 4 * months
    days = int(ageValue) * 365

    lineOne = f"Your age in months is: {months}"
    lineTwo = f"Your age in weeks is: {weeks}"
    lineThree = f"Your age in days is: {days}"

    allLines = [lineOne, lineTwo, lineThree]
    messagebox.showinfo("Your age details:", "\n".join(allLines))


# Create the calculate button
btn = Button(
    ageApp,
    text="Calculate age",
    width=20,
    height=2,
    bg="#e91e63",
    fg="white",
    borderwidth=0,
    command=calc,
)
btn.pack()  # Place button in the main window


# Run app infinitely
ageApp.mainloop()

# pyinstaller.exe --onefile CalculateAgeWithTkinter.py -> To make an exe file
