"""
Запросить любое число не менее 10. 
Вывести на экран сумму квадратов каждой цифры составляющей это число. 
Например: дано 236 => 2*2 + 3*3 + 6*6 = 49 

"""

number = '123456'
squares_sum = 0

for i in range(0,len(number)):
    squares_sum += (int(number[i]) * int(number[i]))
print(squares_sum)
