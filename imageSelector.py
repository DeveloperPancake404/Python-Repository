import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, Tk, Label
from PIL import Image, ImageTk # type: ignore

root = Tk()
root.geometry("500x500")
root.title("Image Loader")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")

label = Label(root)
label.pack()

def load_image_tabone():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg")
        ]
    )
    if not file_path:
        return
    img = Image.open(file_path)
    img = img.resize((400, 400))
    photo = ImageTk.PhotoImage(img)
    image_label = Label(tab1, image=photo)
    image_label.image = photo
    image_label.pack()

def load_image_tabtwo():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg")
        ]
    )
    if not file_path:
        return
    img = Image.open(file_path)
    img = img.resize((400, 400))
    photo = ImageTk.PhotoImage(img)
    image_label = Label(tab2, image=photo)
    image_label.image = photo
    image_label.pack()

def load_image_tabthree():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg")
        ]
    )
    if not file_path:
        return
    img = Image.open(file_path)
    img = img.resize((400, 400))
    photo = ImageTk.PhotoImage(img)
    image_label = Label(tab3, image=photo)
    image_label.image = photo
    image_label.pack()

button = tk.Button(tab1, text="Load image", command=load_image_tabone).pack()
button = tk.Button(tab2, text="Load image", command=load_image_tabtwo).pack()
button = tk.Button(tab3, text="Load image", command=load_image_tabthree).pack()

root.mainloop()
