import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

box = canvas.create_rectangle(50, 50, 150, 150, fill="red")

def delete_box(event):
    canvas.delete(box)

canvas.bind("<Button-1>", delete_box)

root.mainloop()