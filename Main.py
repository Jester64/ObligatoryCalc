import tkinter as tk
import math
import re

# Custom context with math functions
complex_math_dict = {
    "log": math.log,           # natural log (base e)
    "ln": math.log,            # alias for natural log
    "log10": math.log10,       # base-10 log
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "pi": math.pi,
    "e": math.e
}

root = tk.Tk() # Create a window object
bgColour = "#26292a" # Define the background color
root.configure(bg=bgColour) # Set the background color to black

root.title("Obligatory Calculator")
root.geometry("400x600")

value = "0" # Initialize the value to be displayed

# Create a single-line entry widget with right-aligned text
MainEntry = tk.Entry(root, justify='left', font=("Arial", 25), bg="white", fg="black", width=20)
MainEntry.pack(pady=10)

# Insert the initial value
MainEntry.insert(0, str(value))

def preprocess_expr(expr):
    """
    Converts logN(x) → log(x, N)
    For example: log2(8) → log(8, 2)
    """
    # Matches things like log2(3), log12(144), etc.
    pattern = r"log(\d+(?:\.\d+)?)(\s*)\(([^()]+)\)"
    
    def replacer(match):
        base = match.group(1)
        spacing = match.group(2)
        value = match.group(3)
        return f"log({value},{spacing}{base})"
    
    return re.sub(pattern, replacer, expr)

def update_entry(newChar):
    """Update the entry with the given value."""
    
    value = MainEntry.get()  # Get the current value from the entry

    if MainEntry.get() == "0":
        MainEntry.delete(0, tk.END)  # Clear the entry if it is "0"
        MainEntry.insert(0, str(newChar))  # Insert the new value
    else:
        value += str(newChar)
        MainEntry.delete(0, tk.END)  # Clear the entry if it is "0"
        MainEntry.insert(0, str(value))  # Insert the new value

def solve():
    """Evaluate the expression in the entry."""

    proccessed_expr = preprocess_expr(MainEntry.get())  # Preprocess the expression

    try:
        result = eval(proccessed_expr, {"__builtins__": None}, complex_math_dict)  # Evaluate the expression
        MainEntry.delete(0, tk.END)  # Clear the entry
        MainEntry.insert(0, str(result))  # Insert the result
    except Exception as e:
        MainEntry.delete(0, tk.END)  # Clear the entry if there's an error
        MainEntry.insert(0, "Error")  # Show error message

def clear_entry():
    """Clear the entry."""
    MainEntry.delete(0, tk.END)  # Clear the entry
    MainEntry.insert(0, "0")  # Reset to initial value

# Frame for the calculator operations
operationButtonFrame = tk.Frame(root, bg=bgColour)
operationButtonFrame.pack(pady=10)

# Frame for the calculator buttons
numberButtonFrame = tk.Frame(root, bg=bgColour)
numberButtonFrame.pack(pady=10)

# Buttons for the calculator
# Number Buttons
buttonOne = tk.Button(numberButtonFrame, text="1", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("1"))
buttonOne.grid(row=2, column=0, padx=5, pady=5)

buttonTwo = tk.Button(numberButtonFrame, text="2", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("2"))
buttonTwo.grid(row=2, column=1, padx=5, pady=5)

buttonThree = tk.Button(numberButtonFrame, text="3", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("3"))
buttonThree.grid(row=2, column=2, padx=5, pady=5)

buttonFour = tk.Button(numberButtonFrame, text="4", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("4"))
buttonFour.grid(row=1, column=0, padx=5, pady=5)

buttonFive = tk.Button(numberButtonFrame, text="5", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("5"))
buttonFive.grid(row=1, column=1, padx=5, pady=5)

buttonSix = tk.Button(numberButtonFrame, text="6", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("6"))
buttonSix.grid(row=1, column=2, padx=5, pady=5)

buttonSeven = tk.Button(numberButtonFrame, text="7", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("7"))
buttonSeven.grid(row=0, column=0, padx=5, pady=5)

buttonEight = tk.Button(numberButtonFrame, text="8", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("8"))
buttonEight.grid(row=0, column=1, padx=5, pady=5)

ButtonNine = tk.Button(numberButtonFrame, text="9", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("9"))
ButtonNine.grid(row=0, column=2, padx=5, pady=5)

buttonZero = tk.Button(numberButtonFrame, text="0", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("0"))
buttonZero.grid(row=3, column=0, padx=5, pady=5)

buttonDecimel = tk.Button(numberButtonFrame, text=".", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("."))
buttonDecimel.grid(row=3, column=1, padx=5, pady=5)

buttonSum = tk.Button(numberButtonFrame, text="=", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=solve)
buttonSum.grid(row=3, column=2, padx=5, pady=5)

#Operation Buttons
buttonAdd = tk.Button(numberButtonFrame, text="+", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("+"))
buttonAdd.grid(row=0, column=3, padx=5, pady=5)

buttonSubtract = tk.Button(numberButtonFrame, text="-", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("-"))
buttonSubtract.grid(row=1, column=3, padx=5, pady=5)

buttonMultiply = tk.Button(numberButtonFrame, text="*", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("*"))
buttonMultiply.grid(row=2, column=3, padx=5, pady=5)

buttonDivide = tk.Button(numberButtonFrame, text="/", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("/"))
buttonDivide.grid(row=3, column=3, padx=5, pady=5)

#helper buttons
clearButton = tk.Button(operationButtonFrame, text="C", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=clear_entry)
clearButton.grid(row=0, column=0, padx=5, pady=5)

openBracketButton = tk.Button(operationButtonFrame, text="(", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("("))
openBracketButton.grid(row=0, column=1, padx=5, pady=5)

closeBracketButton = tk.Button(operationButtonFrame, text=")", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry(")"))
closeBracketButton.grid(row=0, column=2, padx=5, pady=5)

logButton = tk.Button(operationButtonFrame, text="log", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("log"))
logButton.grid(row=0, column=3, padx=5, pady=5)

natLogButton = tk.Button(operationButtonFrame, text="ln", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("ln("))
natLogButton.grid(row=0, column=4, padx=5, pady=5)

commaButton = tk.Button(operationButtonFrame, text=",", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry(","))
commaButton.grid(row=0, column=5, padx=5, pady=5)

eButton = tk.Button(operationButtonFrame, text="e", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("e"))
eButton.grid(row=1, column=0, padx=5, pady=5)

sinButton = tk.Button(operationButtonFrame, text="sin", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("sin(")) 
sinButton.grid(row=1, column=1, padx=5, pady=5)

cosButton = tk.Button(operationButtonFrame, text="cos", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("cos("))
cosButton.grid(row=1, column=2, padx=5, pady=5)

tanButton = tk.Button(operationButtonFrame, text="tan", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("tan(")) 
tanButton.grid(row=1, column=3, padx=5, pady=5)

piButton = tk.Button(operationButtonFrame, text="π", bg="white", fg="black", font=("Arial", 20), width=3, height=1, command=lambda: update_entry("pi"))
piButton.grid(row=1, column=4, padx=5, pady=5)

root.resizable(False, False) # Prevent the window from being resized unless your enviroment is big silly.
root.mainloop() # Start the main loop to run the application