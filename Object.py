from tkinter import ttk
from abc import ABC


def ParametrsLabel(labels):
    for i in labels:
        i['foreground'] = 'blue'
        i['font'] = ('TimesNewRoman', 11)
        i['foreground'] = 'navy'
class Figure(ABC):
    def Sozdanie(self, window):
        pass


class Label(Figure):
    def Sozdanie(self, window):
        maxCU = ttk.Label(text="Максимальный граничный\nКУ")
        minCU = ttk.Label(text="Минимальный граничный\nКУ")
        firstCU = ttk.Label(text="КУ первого правила")
        secondCU = ttk.Label(text="КУ второго правила")
        labels = [maxCU, minCU, firstCU, secondCU]
        ParametrsLabel(labels)
        maxCU.place(x=25, y=25)
        minCU.place(x=25, y=80)
        firstCU.place(x=25, y=125)
        secondCU.place(x=25, y=170)

