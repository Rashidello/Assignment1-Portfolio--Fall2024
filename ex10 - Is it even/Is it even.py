def main():
    usernumber = int(input("enter desired number: "))

    j = usernumber % 2

    if j == 0:
        again = in10
        put("it's even\nWanna try again?(y/n) ")
        if again == "y":
            main()
        else:
            exit()   
    else:
        oddagain = input("It's odd\nWanna try again?(y/n) ")
        if oddagain == 'y':
            main()
        else:
            exit()
main()