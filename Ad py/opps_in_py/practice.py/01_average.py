class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks


    def get_avg(self):
        sum= 0
        for val in self.marks:
                sum+=val
        print("Hiii",self.name,"your avg score si :",sum/3) 


s= Student("Anurag sharma",[87,98,97])
s.get_avg() 

s.name="siya"
s.get_avg()