password = 12345
limit = 5
attempts = 0

userinput = int(input("Enter a password: "))
while password != userinput and limit > attempts:

    attempts += 1
    print(attempts, "failed attempts!")
    userinput = int(input("try again: "))
if userinput == password:
    print("The correct password is entered!!")
