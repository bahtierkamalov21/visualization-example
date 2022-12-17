import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Визуализация Python | Камалов Бахтиёр")
        self.iconbitmap("./src/assets/favicon.ico")
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        w = w - 100
        h = h - 85
        self.geometry("{}x{}+42+2".format(w, h))
        

class FrameDrawer(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
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
        
        # Компоненты
        self.label = Label(self, text="Моя статистика за неделю", bg="#333", padx=20, pady=10, font=16, fg="white", width=self.winfo_reqwidth() - 458)
        self.label.place(x=20, y=20)
        
        self.buttonCheckInNotebook = Button(self, width=self.winfo_reqwidth() - 458, padx=20, pady=10, text="Открыть график в графическом окне matplotlib", font=16, fg="white", bg="#4f46e5", command=self.graph)
        self.buttonCheckInNotebook.place(y=self.winfo_reqheight() - 170, x=20)
    
    # Метод открытия и рендеринга графика
    def graph(self, open=False):
        self.open = open
        self.fig, self.ax = plt.subplots(figsize=(4.8, 5), layout='constrained')
        self.ax.set_title("График в виде Plot")
        # Первый аргумент предмет, второй оценка
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        self.ax.plot(days, [5, 5, 4, 5, 0], label='Математика')
        self.ax.plot(days, [4, 4, 4, 4, 0], label='Русский язык')
        self.ax.plot(days, [4, 5, 4, 5, 0], label='Казахский язык')
        self.ax.plot(days, [5, 5, 5, 4, 5], label='Информатика')
        self.ax.set_xlabel('Дни недели')
        self.ax.set_ylabel('Оценки')
        self.ax.legend()
        if not self.open:
            plt.show()
        else:
            canvas = FigureCanvasTkAgg(self.fig, self)
            canvas.draw()
            canvas.get_tk_widget().place(y=80, x=5)
            
    def get_req_width(self):
        return self.winfo_reqwidth()
            

class FrameRightTop(ttk.Frame):
    def __init__(self, master, reqwidth):
        super().__init__(master)
         # Стили
        style = ttk.Style()
        style.configure("RightTop.TFrame", background="#293548")
        
        # Описание фрейма
        self['width'] = self.winfo_screenwidth() - reqwidth
        self['height'] = self.winfo_screenheight() // 2
        self['borderwidth'] = 1
        self['relief'] = 'raised'
        self['style'] = "RightTop.TFrame"
        
        # Упаковка
        self.place(x=reqwidth)
        
        
class FrameRightBottom(ttk.Frame):
    def __init__(self, master, reqwidth):
        super().__init__(master)
         # Стили
        style = ttk.Style()
        style.configure("RightBottom.TFrame", background="#1e293b")
        
        # Описание фрейма
        self['width'] = self.winfo_screenwidth() - reqwidth
        self['height'] = self.winfo_screenheight() // 2
        self['borderwidth'] = 1
        self['relief'] = 'groove'
        self['style'] = "RightBottom.TFrame"
        
        # Упаковка
        self.place(x=reqwidth, y=self.winfo_screenheight() // 2)
        

if __name__ == "__main__":
    root = Main()

    # Фреймы
    frame_drawer = FrameDrawer(root)
    reqwidth_frame_drawer = frame_drawer.get_req_width()
    frame_right_top = FrameRightTop(root, reqwidth_frame_drawer)
    frame_right_bottom = FrameRightBottom(root, reqwidth_frame_drawer)
    # Вызов графика
    frame_drawer.graph(open=True)

    root.mainloop()
