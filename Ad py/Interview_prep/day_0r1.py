def show(**kwargs):
    print(kwargs)
show(name="John", age=30, city="New York")



with opne('file.txt') as f :
    content=f.read()
    print(content)