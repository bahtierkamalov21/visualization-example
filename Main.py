import tkinter as tk
import pandas as pd
from tkinter import *


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Визуализация Python")
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        w = w - 100
        h = h - 85
        self.geometry("{}x{}+42+2".format(w, h))


class FrameDrawer(tk.Frame):
    def __init__(self, master, options):
        super().__init__(master, options)
        self.grid(row=0, column=0)
        
        self.label = Label(text="Общая статистика", bg="#fff", pady=10, padx=10)
        self.label.grid(row=0, column=0)
        

if __name__ == "__main__":
    root = Main()

    # Фреймы
    frame_drawer = FrameDrawer(root, options={"width":root.winfo_screenwidth() // 2, "height":root.winfo_screenheight(), "bg":"black"})

    root.mainloop()
