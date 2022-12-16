import tkinter as tk
from tkinter import Label

# Импорт компонентов


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        # Создания title приложения
        self.title("Визуализация Python")
        self.add_frames()

    def add_frames(self):
        self.drawer = Drawer(self)


class Drawer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.drawer = Label(text="cascacasc")
        self.drawer.pack()


if __name__ == "__main__":
    main = Main()
    main.mainloop()
