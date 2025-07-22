# A clas method is bound to the class & receive the class as an  implicit first argumet
# static method cant access or meodify class state and generally for utility


class person:
    name = "siya"


    @classmethod
    def changename(cls,name):
        cls.name=name

p=person()
p.changename("siya sharma") 
print(p.name)
print(person.name)          