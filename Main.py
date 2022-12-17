import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Визуализация Python")
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        w = w - 100
        h = h - 85
        self.geometry("{}x{}+42+2".format(w, h))
        

class FrameDrawer(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Класс объекта
        print(self.winfo_class())
        
        # Стили
        style = ttk.Style()
        style.configure("TFrame", background="#fafafa")
        
        # Описание фрейма
        self['height'] = self.winfo_screenheight()
        self['width'] = (self.winfo_screenwidth() // 2) - 200
        self['padding'] = 5
        self['borderwidth'] = 1
        self['relief'] = 'raised'
        
        # Упаковка
        self.grid(row=0, column=0)
        
        # Данные для графиков
        self.list = [[5, 4, 5, 5, 5], [4, 5, 3, 3, 3], [3, 5, 2, 2, 2], [5, 5, 5, 5, 5], [2, 5, 4, 4, 4]]
        self.index = ["Математика", "Казахски", "Английский", "Русский", "Физика"]
        self.columns = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        table = pd.DataFrame(self.list, index=self.index, columns=self.columns)
        
        # Графики
        fig, ax = plt.subplots()
        
        title = plt.title("Линейный график")
        line = ax.plot(table)
        
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(y=100)
        
        self.label = Label(self, text="Моя статистика за неделю", bg="#333", padx=20, pady=10, font=16, fg="white", width=self.winfo_reqwidth() - 440)
        self.label.place(x=20, y=20)
        

if __name__ == "__main__":
    root = Main()

    # Фреймы
    frame_drawer = FrameDrawer(root)

    root.mainloop()
