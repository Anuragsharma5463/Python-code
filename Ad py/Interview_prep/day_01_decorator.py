def decorator(func):
    def wrapper():
        print("Transaction started")
        func()
        print("Transaction completed")
        
    return wrapper
def hello():
    print("Executing hello function")
hello1= decorator(hello)
hello1()


def decorator(func):
    def wrapper():
        print("Transaction started")
        func()
        print("Transaction completed")
    return wrapper
def hello():
    print("Executing hello function")
hello2=decorator(hello)
hello2()

def decorator(func):
    def wrapper():
        print("Transaction started")
        func()
        print("Transaction completed")
    return wrapper
def love():
    print("Execution the all transaction executing")

jannn2=decorator(love)
jannn2()