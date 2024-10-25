def calculation(number):
    number = number % 2

    if number == 0:
       return "it's even"
       
    else:
        return "it's odd"
       
def main():
    number = int(input("enter desired number: "))
    print(f"{calculation(number)}")
    again = input("\nWanna try again?(y/n)")
    if again == 'y':
        main()
    else:
        exit()
    
main()
