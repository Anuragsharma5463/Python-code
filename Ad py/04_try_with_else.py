try:
    i = int(input("Enter the number: "))
    c = 1 / i
except Exception as r:
    print(r)
else:
    print("We were successful :")
