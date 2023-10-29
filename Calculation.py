from tkinter.messagebox import showerror, showinfo


def Raschet(firstCu, secondCu, maxCu, minCu):
    if Proverka(firstCu, secondCu, maxCu, minCu):
        firstCu1 = float(firstCu.get())
        secondCu2 = float(secondCu.get())
        result = ((1 - firstCu1)*secondCu2 + firstCu1)
        if result > maxCu.get():
            showinfo("Вывод", "Вывод: прибыль растет. Полученный КУ: " + str(result))
        elif result > minCu.get():
            showinfo("Вывод", "Вывод: прибыль падает. Полученный КУ: " + str(result))
        elif minCu < result < maxCu:
            showinfo("Вывод", "Вывод: система не может сделать вывод, т.к. значение находится между граничными КУ. Полученный КУ: " + str(result))
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
