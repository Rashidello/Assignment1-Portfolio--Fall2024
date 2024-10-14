def main():
    quiz0 = input("What is capital of France ")
    if quiz0.lower() in {'paris'}:
        print("The answer is correct")
    else:
        print("The answer is Wrong")
        main()
    quiz1 = input("What is capital of Germany ")
    if quiz1.lower() in {'berlin'}:
        print("The answer is correct")
    else:
        print("The answer is Wrong")
        main()
    quiz2 = input("What is capital of Estonia ")
    if quiz2.lower() in {'tallin'}:
        print("The answer is correct")
    else:
        print("The answer is Wrong")
        main()
    quiz3 = input("What is capital of Belguim ")
    if quiz3.lower() in {"brussels"}:
        print("The answer is correct")
    else:
        print("The answer is Wrong")
        main()
    quiz4 = input("What is capital of Finland ")
    if quiz4.lower() in {"helsinki"}:
        print("The answer is correct")
    else:
        print("The answer is Wrong")
        main()
    quiz5 = input("What is capital of Denmark ")
    if quiz5.lower() in {"copenhagen"}:
        print("The answer is correct")
    else:
        print("The answer is Wrong")
        main()
    quiz6 = input("What is capital of Hungary ")
    if quiz6.lower() in {"budapest"}:
        print("Answer is correct")
    else:
        print("The answer is Wrong")
        main()
    quiz7 = input("What is capital of Croatia ")
    if quiz7.lower() in {"zagreb"}:
        print("Answer is correct")
    else:
        print("The answer is Wrong")
        main()

    quiz8 = input("What is capital of Austria ")
    if quiz8.lower() in {"vienna"}:
        print("Answer is correct")
    else:
        print("The answer is Wrong")
        main()

    quiz9 = input("What is capital of Cyprus ")
    if quiz9.lower() in {"nicosia"}:
        print("The answer is correct")
    else:
        print("The answer is Wrong")
        main()

    quiz10 = input("What is capital of Poland ")
    if quiz10.lower() in {"warsaw"}:
        print("The answer is correct")
    else:
        print("The answer is Wrong")
        main()


print("Wellcome to the quiz")
main()

