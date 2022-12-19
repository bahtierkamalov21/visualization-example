from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")


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
        self.call_components()

    def call_components(self):
        # Фреймы
        self.frame_drawer = FrameDrawer(self)
        self.reqwidth_frame_drawer = self.frame_drawer.get_req_width()
        self.frame_right_top = FrameRightTop(self, self.reqwidth_frame_drawer)
        self.frame_right_bottom = FrameRightBottom(
            self, self.reqwidth_frame_drawer)
        
        # Вызов графика
        self.frame_drawer.graph(open=True)
        self.frame_right_top.graph(open=True)
        self.frame_right_bottom.graph(open=True)


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
        self.label = Label(self, text="Моя статистика за неделю", bg="#333", padx=20,
                           pady=10, font="Montserrat 12", fg="white", width=self.winfo_reqwidth() - 458)
        self.label.place(x=20, y=20)

        self.buttonCheckInNotebook = Button(
            self, width=self.winfo_reqwidth() - 458,
            padx=20, pady=10, text="Открыть график в графическом окне matplotlib",
            font=16, fg="white", bg="#4f46e5",
            activebackground="#333", activeforeground="#fff",
            relief="groove",  command=self.graph
        )
        self.buttonCheckInNotebook.place(y=self.winfo_reqheight() - 140, x=20)

    # Метод открытия и рендеринга графика
    def graph(self, open=False):
        self.open = open
        
        # Данные
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"] # Первый аргумент предмет, второй оценка
        
        fig, ax = plt.subplots(
            figsize=(4.8, 5.2), layout='constrained')
        ax.set_title("График в виде Plot")
        ax.plot(days, [5, 5, 4, 5, 0], label='Математика')
        ax.plot(days, [4, 4, 4, 4, 0], label='Русский язык')
        ax.plot(days, [4, 5, 4, 5, 0], label='Казахский язык')
        ax.plot(days, [5, 5, 5, 4, 5], label='Информатика')
        ax.set_xlabel('Дни недели')
        ax.set_ylabel('Оценки')
        ax.legend()
        
        if not self.open:
            fig.show()
        else:
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.draw()
            canvas.get_tk_widget().place(y=85, x=5)

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
        self['padding'] = 5
        self['style'] = "RightTop.TFrame"
        
        # Данные
        self.days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        self.students = [20, 23, 27, 16, 18]

        # Упаковка
        self.place(x=reqwidth)
        
        # Компоненты
        self.buttonCheckInNotebook = Button(
            self, width=50,
            padx=20, pady=10, text="Открыть график в графическом окне matplotlib",
            font=16, fg="white", bg="#4f46e5",
            activebackground="#333", activeforeground="#fff",
            relief="groove",  command=self.graph
        )
        self.buttonCheckInNotebook.place(y=312, x=10)
        
    def graph(self, open=False):
        self.open = open
        
        fig, ax = plt.subplots(figsize=(6, 2.8), layout='constrained')
        ax.set_title("Колличество учеников посещавших колледж | Bar")
        ax.set_xlabel("Ученики")
        ax.set_ylabel("Дни недели")
        ax.bar(self.days, self.students)
        
        if not self.open:
            fig.show()
        else:
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=20)


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
        self['padding'] = 5
        self['style'] = "RightBottom.TFrame"
        
        # Данные
        self.days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        self.students = [20, 23, 27, 16, 18]
        map(float(), self.students) # Преобразование данных массива в float

        # Упаковка
        self.place(x=reqwidth, y=self.winfo_screenheight() // 2)
        
    def graph(self, open=False):
        self.open = open
        
        fig, ax = plt.subplots(figsize=(5, 2.8), layout='constrained')
        ax.set_title("Колличество учеников посещавших колледж | Pie")
        ax.pie(self.students, labels=self.days)
        
        if not self.open:
            fig.show()
        else:
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=15)


if __name__ == "__main__":
    root = Main()
    root.mainloop()
