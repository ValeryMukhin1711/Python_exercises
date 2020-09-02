#Задача 4

words = input("Введите слова, разделенные пробелами ")
list_words = words.split()

counter = 0
length = len (list_words)
while counter < length:
    current_word = list_words[counter][0:10]
    print ((counter + 1), current_word)
    counter = counter + 1

