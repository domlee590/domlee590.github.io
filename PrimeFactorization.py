#Prime Factorization for week 2
import math

output = ""
number = int(input("Enter a number: "))
i = 2 #start division at 2
while i <= math.sqrt(number):
	if number % i == 0:
		number = number / i
		print(i)
		#found factor
	else:
		i+=1

if number > 2:
	print(number)