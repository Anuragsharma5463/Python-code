class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started :")

    @staticmethod
    def stop():
        print("car stoped ")

class toyatacar(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()


car1 =toyatacar("honda","electirc ")
print(car1.type)                       