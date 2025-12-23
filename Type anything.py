# --- Imports --- #
import tkinter as tk
import time

# --- Window Managment --- #
window = tk.Tk()
window.title("Type anythingType")
window.geometry("300x200")

# --- Create the input box --- #
entry = tk.Entry(
    window,
    font=("Arial", 24)
)
entry.pack()
print("Input box created")

# --- Adds the text from the input box to the screen --- #
def get_text():
    textAdded = entry.get()
    window,
    label = tk.Label(
    text=textAdded,
    font=("Arial", 24)
)
    label.pack()

# --- Create button --- #
button = tk.Button(
window,
text="Enter", 
command=get_text
)
button.pack()
print("Button created")

window.mainloop()
print("Window closed, closing in 3 seconds")
time.sleep(3)
