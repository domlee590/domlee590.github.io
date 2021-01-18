#Adventure Game Demo for week 2

print("Welcome to Adventure Game Demo!")
print("You wake up in a field with only a lighter and clothes. \nYou see a bucket and a spear. You pick up the [1]Bucket or [2]Spear")

def makeChoice():
	choice = int(input("Choice: "))
	while choice != 1 and choice != 2:
		choice = int(input("Choice: "))
	return choice

if makeChoice() == 1:
	print("You pick up the bucket. You go to a nearby pond and\nfill the bucket with water, sealing the top tightly.\nYou're hungry; should you [1]Look for food or [2]Look for shelter?")
	if makeChoice() == 1:
		print("You go forth looking for food, but your bucket is heavy and you can't move quickly.\nYou need to take a rest.")
	else:
		print("The field seems empty. After many hours of searching, you find \na small grove with a lone tree providing shade. You rest here.")
else:
	print("You pick up the spear. Shortly after, you hear a noise behind you—it seems a deer is\ninjured and cannot flee. You realize how hungry you are; should you\n[1]Kill the deer or [2]Spare it?")
	if makeChoice() == 1:
		print("You kill the deer with your spear, and use your lighter \nto start a small fire. After cooking and eating your meal, it \nis dark and you must rest.")
	else:
		print("You spare the deer, but you know you must find food soon. \nYou go forth looking and come upon a small pond. You can \n[1]Spear the fish or [2]Continue looking")
		if makeChoice() == 1:
			print("You spear the fish, and start a small fire with your lighter. After your meal, \nit is dark and you must rest.")
		else:
			print("You go on looking, but find nothing. You're extremely tired, and you sit \ndown catch your breath, but fall asleep instread")

print("You wake up. [END OF DEMO. CHECK OTHER CHOICES IF YOU LIKE]")