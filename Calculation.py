from tkinter.messagebox import showerror


def Raschet(firstCu, secondCu):
    if Proverka(firstCu, secondCu):
        firstCu1 = float(firstCu.get())
        secondCu2 = float(secondCu.get())
        result = firstCu1 + (1 - firstCu1 * secondCu2)
        print(result)
    else:
        showerror(title="Ошибка", message="Введенные данные некорректны")
        firstCu.set(0)
        secondCu.set(0)

#!!!!ЮЗАТЬ В ХОДЕ ВЫПОЛНЕНИЯ КУРСОВОГО ПРОЕКТА ДОЛБЕНЬ!!!!
def Proverka(firstCu, secondCu):
    try:
        firstCu=float(firstCu.get())
        secondCu=float(secondCu.get())
        return True
    except Exception as e:
        return False
