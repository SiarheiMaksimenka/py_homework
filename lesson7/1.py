"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.
"""

i = ()
scores = []

while i != '0':
    i = input("балл: ")
    if not i.isalpha() and "." not in i: #проверка ввода
        scores.append(i)

s = ((sum (map (int, scores)))) / (len(scores)-1)

print ("средний балл: ", round (s , 1))


