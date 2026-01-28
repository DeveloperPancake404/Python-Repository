import tkinter as tk
import random

# Use set_cell(row, col, value) to set the value of a cell in the grid

rows = 5 # Rows in the grid
cols = 8 # Columns in the grid
cell_width = 50 # Width of each cell
cell_height = 30 # Height of each cell
canvas_height = rows * cell_height # Height of the canvas
canvas_width = cols * cell_width # Width of the canvas

# Create the main window
root = tk.Tk()
root.geometry("400x400")
root.title("Grid Layout Example")
text = tk.StringVar()
# Create a canvas
canvas = tk.Canvas(
    root,
    width=canvas_width,
    height=canvas_height,
    bg="white"
)
canvas.pack()

rects = {}
texts = {}

def set_cell(row, col, value):
    canvas.itemconfig(texts[(row, col)], text=str(value))
    canvas.itemconfig(rects[(row, col)], fill="white")

# Draw the grid
for r in range(rows):
    for c in range(cols):
        x1 = c * cell_width
        y1 = r * cell_height
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        rect_id = canvas.create_rectangle(x1, y1, x2, y2, outline="black")
        text_id = canvas.create_text(
            (x1 + x2) // 2,
            (y1 + y2) // 2,
            text="" # Default text of the cells
        )
        rects[(r, c)] = rect_id
        texts[(r, c)] = text_id
tk.Entry(root, textvariable=text).pack()

def edit_square_one():
    ranY = random.randint(0, rows)
    ranX = random.randint(0, cols)
    set_cell(ranY, ranX, text.get())
    
tk.Button(root, text="Edit random square", command=edit_square_one).pack()
root.mainloop()
