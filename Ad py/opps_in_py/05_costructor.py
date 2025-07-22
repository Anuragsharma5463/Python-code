class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks= marks
        print("Adding new student in database:")


        #we can a method in our code 

    def welcome(self):
        print("miss you  my love")    
    def get_marks(self):
        return self.marks
   # name = "Anurag Sharma"

s1 = Student("Anuarg sharma",90)
print(s1.name)
print(s1.marks)
s1.welcome()
print(s1.get_marks())

s2 = Student("Harsh sinha",98)
print(s2.name)
print(s2.marks)
