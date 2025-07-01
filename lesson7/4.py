'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******



* - елочка со снегом
'''

import random
import os
import time

def snow(s:int):
   for i in range (0,s):
      a = random.randint(0, 20)
      if a == 1:
         print(".",end = "")
      else:
         print(" ", end = "")

h = int(input("высота елочки: "))

while True:
   os.system('cls')

   n_emp = h 
   n_stars = 1

   for i in range(0,h):
      snow(n_emp)
      print("*"*n_stars,end = "")
      snow(n_emp)
      print('')
      n_stars += 2
      n_emp -= 1
      
   time.sleep(0.5)