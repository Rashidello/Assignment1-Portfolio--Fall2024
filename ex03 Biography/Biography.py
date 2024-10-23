def Main():
    Name = input("write your name: ")
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