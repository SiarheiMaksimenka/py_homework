'''
Дан произвольный список из 5 элементов. 
     - Поменять местами 1ый и последний элемент
     - удалить и вывести на печать третий элемент
'''



# s = [1, 2, 3, 4, 5]  

# my_string = f"{', '.join(s)}"
# print (my_string)

l = ["1", "2", "3", "4", "5"]
s = f"{', '.join(l)}"
s = s.replace(", ", "")
print(s)
s = s.replace (s[0], s[4])
print (s)
s = s.replace (s[4], 'ff')
print (s)


# s = s2.replace(s1[0], s1[4])
# print(s)
# s = s.replace(s[4], s2[0])
# print(s)  # Выведет: яблоко, банан, груша






