
class A:
    def abc(self):
        print("A")
class B(A):
    def abc(self):
        print("B") 
class C(B):
    def abc(self):
        print("C")
class D(B,C):
    pass
d=D()
d.abc()   


# initializing an empty list tuple and dict and set
empty_list = []
empty_tuple = ()
empty_Dict={}
empty_set=set()