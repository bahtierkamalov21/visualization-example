import tkinter as tk
from tkinter import Label


class Drawer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.drawer = Label(text="cascacasc")
        self.drawer.pack()
