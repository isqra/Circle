import tkinter as tk
import math

buttons = 10
distance = 5

root = tk.Tk()
root.geometry("404x404")

i = 0
while i < buttons:
    angle = 2 * math.pi * i / buttons - math.pi / 2
    tk.Button(root, width=5, height=2).place(
        x=202 + 150 * math.cos(angle), y=202 + 150 * math.sin(angle), anchor="center")
    i += 1

root.mainloop()
