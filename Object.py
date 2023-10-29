from tkinter import ttk
from abc import ABC
import Calculation


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
        firstRule = ttk.Label(text="Первое правило")
        secondRule = ttk.Label(text="Второе правило")
        labels = [maxCU, minCU, firstCU, secondCU, firstRule, secondRule]
        ParametrsLabel(labels)
        maxCU.place(x=25, y=25)
        minCU.place(x=25, y=70)
        firstCU.place(x=25, y=115)
        secondCU.place(x=25, y=160)
        firstRule.place(x=25, y=205)
        secondRule.place(x=25, y=250)


class Entry(Figure):
    def __init__(self, maxCU, minCU, firstCU, secondCU, firstRule, secondRule):
        self.maxCU = maxCU
        self.minCU = minCU
        self.firstCU = firstCU
        self.secondCU = secondCU
        self.firstRule = firstRule
        self.secondRule = secondRule

    def Sozdanie(self, window):
        maxCU = ttk.Entry(width=20, textvariable=self.maxCU)
        minCU = ttk.Entry(width=20, textvariable=self.minCU)
        firstCU = ttk.Entry(width=20, textvariable=self.firstCU)
        secondCU = ttk.Entry(width=20, textvariable=self.secondCU)
        firstRule = ttk.Entry(width=38, textvariable=self.firstRule, state="readonly")
        secondRule = ttk.Entry(width=38, textvariable=self.secondRule, state="readonly")
        maxCU.place(x=220, y=25)
        minCU.place(x=220, y=70)
        firstCU.place(x=220, y=115)
        secondCU.place(x=220, y=160)
        firstRule.place(x=220, y=205)
        secondRule.place(x=220, y=250)


