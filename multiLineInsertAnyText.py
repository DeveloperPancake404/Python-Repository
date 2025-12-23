# --- Imports --- #
import tkinter as tk
import time
# --- Window Managment --- #
window = tk.Tk()
window.title("Hello")
window.geometry("300x200")
# --- Create the input box --- #
entry = tk.Entry(window)
entry.pack()

# --- Adds the text from the input box to the screen --- #
def get_text():
    text = entry.get()
    label = tk.Label(window, text=text)
    label.pack()

# --- Create button --- #
button = tk.Button(window, text="Enter", command=get_text)
button.pack()

window.mainloop()
print("Window closed, closing in 3 seconds")
time.sleep(3)