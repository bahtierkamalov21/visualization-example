import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Визуализация Python")
        self.iconbitmap("./src/assets/favicon.ico")
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
        self['width'] = (self.winfo_screenwidth() // 2) - 180
        self['padding'] = 5
        self['borderwidth'] = 1
        self['relief'] = 'raised'
        
        # Упаковка
        self.grid(row=0, column=0)
        
        # Данные
        self.data = pd.DataFrame({"Математика": [5, 4, 4, 5, 5], "Русский язык": [4, 4, 4, 4, 4]})
        
        # Таблицы
        self.fig, self.ax = plt.subplots(figsize=(4.8, 5), layout='constrained')
        self.ax.set_title("График в виде Plot")
        self.ax.set_xlabel('Предметы')  # Add an x-label to the axes.
        self.ax.set_ylabel('Оценки')  # Add a y-label to the axes.
        self.ax.plot(["Математика", "Русский язык", "Казахский язык", "Информатика"], [[5, 5, 5, 5, 4], [4, 5, 4, 5, 5], [3, 4, 5, 5, 3], [4, 5, 4, 5, 5]]);  # Plot some data on the axes.
        canvas = FigureCanvasTkAgg(self.fig, self)
        canvas.draw()
        canvas.get_tk_widget().place(y=80, x=5) 
        
        # Компоненты
        self.label = Label(self, text="Моя статистика за неделю", bg="#333", padx=20, pady=10, font=16, fg="white", width=self.winfo_reqwidth() - 458)
        self.label.place(x=20, y=20)
        
        def OpenCanvasTableInNotebook():
            ptk.show()
        
        self.buttonCheckInNotebook = Button(self, width=self.winfo_reqwidth() - 458, padx=20, pady=10, text="Открыть график в графическом окне matplotlib", font=16, fg="white", bg="#333", command=OpenCanvasTableInNotebook)
        self.buttonCheckInNotebook.place(y=self.winfo_reqheight() - 170, x=20)
        

if __name__ == "__main__":
    root = Main()

    # Фреймы
    frame_drawer = FrameDrawer(root)

    root.mainloop()
