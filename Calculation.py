from tkinter.messagebox import showerror, showinfo


def on_key_press(event):
    if event.char.lower() not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\x08']:
        return "break"
    elif event.char == '.' in event.widget.get():
        return "break"



def Raschet(firstCu, secondCu, maxCu, minCu):
    if Proverka(firstCu, secondCu, maxCu, minCu):
        firstCu1 = float(firstCu.get())
        secondCu2 = float(secondCu.get())
        result = ((1 - firstCu1)*secondCu2 + firstCu1)
        if result > maxCu.get():
            showinfo("Вывод", "Вывод: прибыль растет. Полученный КУ: " + str(result))
        elif result < minCu.get():
            showinfo("Вывод", "Вывод: прибыль падает. Полученный КУ: " + str(result))
        elif minCu.get() < result < maxCu.get():
            showinfo("Вывод", "Вывод: система не может сделать вывод, т.к. значение находится между граничными КУ. Полученный КУ: " + str(result))
    else:
        showerror(title="Ошибка", message="Введенные данные некорректны. Либо они равны нулю, либо равны единице")
        firstCu.set(0.0)
        secondCu.set(0.0)
        maxCu.set(0.0)
        minCu.set(0.0)


# !!!!ЮЗАТЬ В ХОДЕ ВЫПОЛНЕНИЯ КУРСОВОГО ПРОЕКТА ДОЛБЕНЬ!!!!
def Proverka(firstCu, secondCu, maxCu, minCu):
    try:
        firstCu = float(firstCu.get())
        secondCu = float(secondCu.get())
        maxCu = float(maxCu.get())
        minCu = float(minCu.get())
        if firstCu < 1 and secondCu < 1 and maxCu < 1 and minCu < 1 and firstCu > 0 and secondCu > 0 and maxCu > 0 and minCu > 0:
            return True
    except Exception as e:
        return False
