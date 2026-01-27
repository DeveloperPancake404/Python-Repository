import tkinter as tk
from tkinter import filedialog, Tk, Label
from PIL import Image, ImageTk # type: ignore

root = Tk()

label = Label(root)
label.pack()

def load_image():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg")
        ]
    )
    if not file_path:
        return
    img = Image.open(file_path)
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

button = tk.Button(text="Load image", command=load_image)
button.pack()

root.mainloop()
