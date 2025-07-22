num_int=10
print("type of num_int is:",type(num_int))
num_float=float(num_int)
print("type of num_float is:",type(num_float))


challange='thirty_day_of_my_python'
print(challange.endswith('on'))

# alphanumerc checking
challange2='Thirtydayspythob'
print(challange2.isalnum())

challenge3='Thirty days of python'
print(challenge3.isalpha())

data='Python_is_a_programming_language'
output=data[-15:]
print(output)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)