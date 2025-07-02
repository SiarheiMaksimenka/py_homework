"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""
import os

os.system('cls')

d = {'names':[],'reviews':[]}
name = review = ()

while True:
    name  = input('name: ')
    if name == 'stop':
        break
    d['names'].append(name)

    review  = input('review: ')
    if review == 'stop':
        break
    d['reviews'].append(review)

os.system('cls')

print("количество отзывов: ", len(d['reviews']), "\n")

print("имена:")
for i in range (0,len(d['names'])):
    print("-",d['names'][i])

print( "\n", "отзывы:")
for i in range (0,len(d['reviews'])):
    print("-",d['reviews'][i])
