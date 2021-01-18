#MySort for week 2

list = [2, 4, 1, 5, 3, 9, 5]
#example

for i in range(len(list)):

	minIndex = i

	for j in range(i + 1, len(list)):
		if list[j] < list[minIndex]:
			minIndex = j

	if minIndex != i:
		list[minIndex], list[i] = list[i], list[minIndex]

print(list)