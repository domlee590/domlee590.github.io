#Unscramble for week 2

letters = input("Enter letters: ")
fileIn = open("wordlist.txt", "r")
words = fileIn.read().split('\n')
output = []

for word in words:
	valid = True
	for char in letters:
		if char not in word:
			valid = False
	if valid == True:
		output.append(word)

print(output)