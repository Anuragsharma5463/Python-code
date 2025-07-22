class A:
    varA = "welcome to class A "


class B:
    varB = "welcome to class B "

class c(A,B):
    varC = "welcome to clas c "

c1 =c()
print(c1.varC)
print(c1.varA)    
