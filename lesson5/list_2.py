'''
Запросить по очереди у пользователя 5 имен. Добавить все в список. 
Отсортировать. 
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
'''


# name_1 = input("Введите имя 1: ")
# name_2 = input("Введите имя 2: ")
# name_3 = input("Введите имя 3: ")
# name_4 = input("Введите имя 4: ")
# name_5 = input("Введите имя 5: ")
name_1 = "Вася"
name_2 = "Василий"
name_3 = "Васек"
name_4 = "Васян"
name_5 = "Василиск"
names = [name_1, name_2, name_3, name_4, name_5]
names.sort()
print (names)
print("вася" in list(map(str.lower, names)))