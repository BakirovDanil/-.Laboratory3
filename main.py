from tkinter import *
from tkinter import ttk

import Object

Frame = Tk()


def Finish():
    Frame.destroy()
    print("Приложение закрыто")


def MainForm(window):
    window.title("Бакиров Данил, Валеев Марат. Задача с коэффициентом уверенности")
    window.geometry("600x700+400+200")
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", Finish)
    Label1 = Object.Label()
    Label1.Sozdanie(window)
    window.mainloop()


MainForm(Frame)
