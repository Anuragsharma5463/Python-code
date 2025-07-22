class A:
    def display(self):
        print("this is displaying the a ")

class B(A):
    def show(self):
        print("this is showing the b")

D= B()
D.display()
D.show()                