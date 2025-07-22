class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"my name is {self.name}.i am {self.age} years old.")

d=person("Anurag",20)
d.info()        