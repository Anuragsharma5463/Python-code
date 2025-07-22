class car:
    @staticmethod
    def start():
        print("car started ")

    @staticmethod
    def stop():
        print("car stoped :")

class Toyatacar(car):
    def __init__(self,brand):
        self.brand=brand 

class fortuner(Toyatacar):
    def __init__(self,type):
        self.type=type






car1 = fortuner("diesel")
# car2 = Toyatacar("prius")



print(car1.start())