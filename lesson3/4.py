'''
запросить число и вывести на экран сколько номиналов в этом числе:
	 - тысячи
	 - сотни
	 - десятки
	 - единицы

пример: # знак >>> значит что ввели что-то через input
    >>>21234 
    тысяч - 21
    сотни - 2
    десятки - 3
    единицы - 4
'''

num = float(input ('число - '))

print (
f'''число {num} содержит 
{int( (num //1000) )} тысяч 
{int( ( (num%1000) // 100) )} сотен 
{int( ( (num%100) // 10) )} десятков 
{int( ((num%10) // 1) )} единиц'''
)
 
