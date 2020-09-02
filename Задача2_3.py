# Задача 3 через списки
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

month = int (input ('Пожалуйста, введите номер месяца '))

if month in winter:
    print ("зима *")
elif month in spring:
    print('весна')
elif month in summer:
    print ('лето')
elif month in autumn:
    print ('осень')
else:
    print ('Некорректный ввод')


# Задача 3 через словари

keys1 = {1: "зима",
         2: "зима",
         3: "весна",
         4: "весна",
         5: "весна",
         6: "лето",
         7: "лето",
         8: "лето",
         9: "осень",
         10: "осень",
         11: "осень",
         12: "зима"}

month = int (input ('Пожалуйста, введите номер месяца '))

print (keys1[month])






