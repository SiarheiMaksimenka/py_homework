"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""


while True:
    a1 = input("переменная 1: ")
    a2 = input("переменная 2: ")
    a3 = input("переменная 3: ")
    a4 = input("переменная 4: ")

    if not a1.isalpha() and \
        not a2.isalpha() and \
        not a3.isalpha() and \
        not a4.isalpha() and \
        "." in a1 and \
        "." in a2 and \
        "." in a3 and \
        "." in a4:
            print (True)

    if a1.isalpha() or \
        a2.isalpha() or \
        a3.isalpha() or \
        a4.isalpha() :
            print(True)

    if (not a1.isalpha() and not a1.isalpha() and "." not in a1 and "." not in a1) or\
        (not a2.isalpha() and not a4.isalpha() and "." not in a2 and "." not in a4) or\
        (not a3.isalpha() and not a4.isalpha() and "." not in a3 and "." not in a4):
        print(True)


    