# Задача 5 (рейтинг)
list1 = [7, 9, 0, -8] #Начальный список
element = ""
# element = input ('Введите, пожалуйста, элемент для составления рейтинга или нажмите Q для выхода ')
while element != "Q":
    element = input('Введите, пожалуйста, элемент для составления рейтинга или нажмите Q для выхода ')
    try:
        element1 = int(element)
        list1.append(element1)
        list1.sort()
        list1.reverse()
        print("Рейтинг: ", end='')
        print(list1)

    except:
        element = input('Некорректный ввод. Введите, пожалуйста, число или Q для выхода ')








