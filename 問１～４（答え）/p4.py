import tkinter as tk

root = tk.Tk()
root.title("練習問題4 - 10/29/2026")
canvas = tk.Canvas(
    root,
    width=800,
    height=600,
    bg="#ffffff"
)
canvas.pack()
box = canvas.create_rectangle(
    100, 100, 200, 200,
    fill="#ff0000"
)
def delete_box(event):
    canvas.delete(box)
canvas.tag_bind(box, "<Button-1>", delete_box)

def move_box():
    canvas.move(box, 5, 0)
    root.after(30, move_box)
    
move_box()
root.mainloop()