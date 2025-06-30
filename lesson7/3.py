'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''
import string

number = '812678126487614871268471'
number_new = ("")

for  i in range (len(number)):
        number_new = number_new + chr(int(number[i]) + 96)
number = number_new        
print (number)


  