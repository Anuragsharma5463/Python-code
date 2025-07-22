try:
    a = int(input("enter the number of a :"))
    c = 1/a
    print(c)

except ValueError as e:
    print("please enter a valid value :")
    print(e)    
except ZeroDivisionError as e :
    print("please enter number greater than 0:")
    print(e)


print("Thnks for using this code :")