from tkinter import *
from tkinter import ttk

import Object
import Calculation

Frame = Tk()

maxCu = DoubleVar()
minCu = DoubleVar()
firstCu = DoubleVar()
secondCu = DoubleVar()


def Maths():
    Calculation.Raschet(firstCu, secondCu)


def Finish():
    Frame.destroy()
    print("Приложение закрыто")


def MainForm(window):
    window.title("Бакиров Данил, Валеев Марат. Задача с коэффициентом уверенности")
    window.geometry("600x300+400+200")
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", Finish)
    Label1 = Object.Label()
    Label1.Sozdanie(window)
    Entry1 = Object.Entry(maxCu, minCu, firstCu, secondCu)
    Entry1.Sozdanie(window)
    window.mainloop()


button = ttk.Button(text="Произвести расчет", command=Maths)
button.place(x=400, y=25)

MainForm(Frame)
