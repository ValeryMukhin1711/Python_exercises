#Задача_2
test_list1 = [1, 2, 3, 4, 5]
list1 = input ('Введите, пожалуйста, данные через пробел ').split()
length = len (list1)
if length == 0:
    list1 = test_list1
    print ('Данных не было введено, будет обработан список по умолчанию, 1, 2, 3, 4, 5')
    length = len(list1)
counter = 0
while counter < length - 1:
    list1[counter], list1[counter + 1] = list1[counter + 1], list1[counter]
    counter += 2
print (list1)