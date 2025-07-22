
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name}. I am {self.age} years old.")

c = Person("Anurag", 23)
c.info()