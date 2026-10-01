import tkinter as tk

from operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulus,
    square_root
)


# ==========================================
# Calculator state
# ==========================================

first_number = None
current_operator = None


# ==========================================
# Number button
# ==========================================

def number_click(number):

    current = display.get()

    # Prevent multiple decimal points
    if number == "." and "." in current:
        return

    display.insert(tk.END, number)


# ==========================================
# Operator button
# ==========================================

def operator_click(operator):

    global first_number
    global current_operator

    try:

        first_number = float(display.get())

        current_operator = operator

        display.delete(0, tk.END)

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Error")


# ==========================================
# Calculate
# ==========================================

def calculate():

    global first_number
    global current_operator

    try:

        second_number = float(display.get())

        if current_operator == "+":

            result = add(first_number, second_number)

        elif current_operator == "-":

            result = subtract(first_number, second_number)

        elif current_operator == "*":

            result = multiply(first_number, second_number)

        elif current_operator == "/":

            result = divide(first_number, second_number)

        elif current_operator == "^":

            result = power(first_number, second_number)

        elif current_operator == "%":

            result = modulus(first_number, second_number)

        else:

            return

        # Remove unnecessary .0
        if result == int(result):
            result = int(result)

        display.delete(0, tk.END)

        display.insert(0, str(result))

        first_number = None
        current_operator = None

    except (ValueError, TypeError, OverflowError) as error:

        display.delete(0, tk.END)

        display.insert(0, "Error")

        print("Error:", error)


# ==========================================
# Square root
# ==========================================

def calculate_square_root():

    try:

        number = float(display.get())

        result = square_root(number)

        if result == int(result):
            result = int(result)

        display.delete(0, tk.END)

        display.insert(0, str(result))

    except (ValueError, TypeError):

        display.delete(0, tk.END)

        display.insert(0, "Error")


# ==========================================
# Clear
# ==========================================

def clear():

    global first_number
    global current_operator

    first_number = None
    current_operator = None

    display.delete(0, tk.END)


# ==========================================
# Backspace
# ==========================================

def backspace():

    current = display.get()

    display.delete(0, tk.END)

    display.insert(0, current[:-1])


# ==========================================
# Main Window
# ==========================================

window = tk.Tk()

window.title("Professional Calculator")

window.geometry("420x650")

window.minsize(350, 550)


# ==========================================
# Display
# ==========================================

display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    bd=5
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=15,
    pady=20,
    sticky="nsew"
)


# ==========================================
# Buttons
# ==========================================

buttons = [

    # text, row, column
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),

    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),

    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),

    ("0", 4, 0),
    (".", 4, 1),
    ("%", 4, 2),
    ("+", 4, 3),

    ("^", 5, 0),
    ("√", 5, 1),
    ("⌫", 5, 2),
    ("=", 5, 3),
]


# ==========================================
# Create buttons
# ==========================================

for text, row, column in buttons:

    if text in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:

        command = lambda value=text: number_click(value)

    elif text in ["+", "-", "*", "/", "^", "%"]:

        command = lambda value=text: operator_click(value)

    elif text == "=":

        command = calculate

    elif text == "√":

        command = calculate_square_root

    elif text == "⌫":

        command = backspace

    else:

        command = None

    button = tk.Button(
        window,
        text=text,
        font=("Arial", 20),
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        sticky="nsew"
    )


# ==========================================
# Clear button
# ==========================================

clear_button = tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 18),
    command=clear
)

clear_button.grid(
    row=6,
    column=0,
    columnspan=4,
    padx=5,
    pady=15,
    sticky="nsew"
)


# ==========================================
# Responsive layout
# ==========================================

for column in range(4):

    window.columnconfigure(
        column,
        weight=1
    )


for row in range(7):

    window.rowconfigure(
        row,
        weight=1
    )


# ==========================================
# Start calculator
# ==========================================

window.mainloop()