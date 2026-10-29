import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.pack()

box = canvas.create_rectangle(0, 50, 100, 150, fill="red")

x = 0

def move_box():
    global x
    x += 5
    canvas.coords(box, x, 50, x + 100, 150)

    if x < 500:
        root.after(50, move_box)

move_box()

root.mainloop()