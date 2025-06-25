'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

a  = [float (input ("число1: ")), float (input ("число2: ")), float (input ("число3: "))]
t = "наибольшее число: "
if a[1]<a[0] and a[0]>a[2]:
    print (t, a[0])
elif a[0]<a[1] and a[1]>a[2]:
    print (t, a[1])
else:
    print (t, a[2])
       