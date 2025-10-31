def someFunction():
    x = 1007
    y = 70
    z = 50
    y += yield
    yield y + z


x1 = someFunction()
print(next(x1))
print(x1.send(100))
