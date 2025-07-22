#methods that do not use the self parameter work at class level
# here decorator is used 


#Decorators allow us to wrap another function in order to extend the behaviour of 
# wrapped function.without permanently modifiying it


class Student:
    @staticmethod

    def college():
        print("Hello sir")


s =Student
s.college()