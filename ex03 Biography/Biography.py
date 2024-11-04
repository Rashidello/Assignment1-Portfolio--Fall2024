def Main():
    Fname = input("write your name: ")
    Lname = input("Write your last name: ")
    Name = Fname + " "+ Lname
    Age = int(input("Enter your age(numbers only!!): "))
    
    Hometown = input("your hometown: ")

    confirmation = input("Do you sure?(y/n): ")
    if confirmation == 'n':
        Main()
    Bio = {"Name" : Name, "Age" : Age, "Hometown" : Hometown}
    print(f"Name : {Bio["Name"]}")
    print(f"Age :  {Bio["Age"]}")
    print(f"Hometown : {Bio["Hometown"]}")




Main()
