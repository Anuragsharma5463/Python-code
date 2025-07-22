class person:
    __name= "Anurag"


    def __hello(self):
        print("Hello person!")
    
    
    def welcome(self):
        self.__hello()


p1 = person()

print(p1.welcome())