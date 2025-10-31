def function1():
    a = 1
    for i in range(10):
        a += i
        yield a


print([x for x in function1()])
