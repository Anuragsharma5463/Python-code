while(True):
    print("press q for exit :")
    a = input("Enter the value of a :")

    if a=="q":
        break
    try:
        a = int(a)
        if a > 6 :
            print("you entered a nubmer greater than 6 :")
    except Exception as e:
        print(f"your input resulted in an error :{e}")        



print("Thanks for playing this game :")        