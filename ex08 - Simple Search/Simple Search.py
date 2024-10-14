people = ("Jake", "Zac", "Ian", "Ron", "Sam", "Dave")

q1 = input("would you like to see list of people?(y/n) ")
if q1 == "y":
    print(people)
search = input ("pick a name(capital!) ")

if search in people:
    print(f"{search} is found")
else:
    print("Not found")