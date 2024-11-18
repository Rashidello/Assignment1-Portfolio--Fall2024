def main():
    months = {
        1 : "31",
        2 : "28",
        3 : "31",
        4 : "30",
        5 : "31", 
        6 : "30",
        7 : "31",
        8 : "31",
        9 : "30",
        10 : "31",
        11 : "30",
        12 : "31"
    }
    leapyear = input ("Is it leap year?(y/n)")
    if leapyear == 'y':
        months[2] = 29
    m_choise = int(input("choose a month (by number only): "))

    if m_choise in months:
        print(f"{m_choise} is {months[m_choise]}")
        tryagain = input("would you like to try again?(y/n)")
        if tryagain == 'y':
            main()
        else:
            print("Bye-bye!")
    else:
        print("Error! Try Again")
        main()

main()