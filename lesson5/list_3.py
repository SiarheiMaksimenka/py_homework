'''
Дан произвольный список из 5 элементов. 
     - Поменять местами 1ый и последний элемент
     - удалить и вывести на печать третий элемент
'''



my_list = [1, 2, 3, 4, 5]  

my_list[0], my_list[-1] = my_list[-1], my_list[0]

third_element = my_list.pop(2) 
print("Удаленный третий элемент:", third_element)

print("Измененный список:", my_list)