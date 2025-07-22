class car:
    def __init__(self):
        self.acc=False
        self.brl=False
        self.cult=False

    def start(self):
        self.acc=True
        self.brl=True
        self.cult=True
        print("now your car has been started :")

car1=car()
car1.start()        