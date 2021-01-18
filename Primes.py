#Primes for week 2

nonprimes = []
primes = []
x = int(input("Enter a number: "))
primes += range(2, x+1)
for num in range(2, x+1):
	for y in range(2, x):
		if num % y == 0 and num != y:
			nonprimes.append(num)
for num in set(nonprimes):
	primes.remove(num)
print(primes)