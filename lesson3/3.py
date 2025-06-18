'''
запросить цену закупки телефона и выдать следующую информацию.
	- цена продажи (+30% к цене закупке)
	- цена продажи со скидкой 5%
	- цена продажи со скидкой 10%
	- цена продажи со скидкой 15%
'''

price = float(input ('цена закупки телефона - '))
price_ceil = price * 1.3
msg_cp = 'цена продажи'
msg_cost = 'цена продажи со скидкой'

print (msg_cp, round (price_ceil, 2))
print (msg_cost, '5%  - ', round (price_ceil * 0.95, 2))
print (msg_cost,  '10%  - ', round (price_ceil * 0.9, 2))
print (msg_cost,  '15%  - ', round (price_ceil * 0.85, 2))