"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""

d = {'one':11, 'two':22, 'hello':'python', True:False}

print ("дан словарь: ", d)

print (f"введите номер удаляемого элемента (число от 1 до {len(d)-1}): ", end="")

element = int(input())

s = list(d.keys())

del d[s[element - 1]]

print("новый словарь: ", d)


