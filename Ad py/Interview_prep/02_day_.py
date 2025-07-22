
def sqr(n):
    for i in range(1,n+1):
        yield i*i
a=sqr(3)

print("The squre are :")
print(next(a))
print(next(a))
print(next(a))


# for i in range(10):
#     if i==7:
#         break
#     print(i,end='')
    

