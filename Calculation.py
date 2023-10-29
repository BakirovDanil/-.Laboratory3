from tkinter.messagebox import showerror, showinfo


def Raschet(firstCu, secondCu, maxCu, minCu):
    if Proverka(firstCu, secondCu, maxCu, minCu):
        firstCu1 = float(firstCu.get())
        secondCu2 = float(secondCu.get())
        result = firstCu1 + (1 - firstCu1 * secondCu2)
        if result > maxCu.get():
            showinfo(title="Вывод", message="Вывод: прибыль растет. Полученный КУ: " + result)
        elif result > minCu.get():
            showinfo(title="Вывод", message="Вывод: прибыль падает")
        elif minCu < result < maxCu:
            showinfo(title="Вывод", message="Вывод: система не может сделать вывод, т.к. значение находится между граничными КУ")
    else:
        showerror(title="Ошибка", message="Введенные данные некорректны")
        firstCu.set(0.0)
        secondCu.set(0.0)


# !!!!ЮЗАТЬ В ХОДЕ ВЫПОЛНЕНИЯ КУРСОВОГО ПРОЕКТА ДОЛБЕНЬ!!!!
def Proverka(firstCu, secondCu, maxCu, minCu):
    try:
        firstCu = float(firstCu.get())
        secondCu = float(secondCu.get())
        maxCu = float(maxCu.get())
        minCu = float(minCu.get())
        if firstCu < 1 and secondCu < 1 and maxCu < 1 and minCu < 1:
            return True
    except Exception as e:
        return False
