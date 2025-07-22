


# it is different from list

def my_generator():
    for i in range(5):
        yield i
gen=my_generator()

print(next(gen))
print(next(gen))

def my_fun():
    for i in range(5):
        yield i
generator= my_fun()
print(next(generator))
print(next(generator))