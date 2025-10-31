def someFunction():
    a = 1
    b = 1
    yield a
    b = a + b
    yield b


print(next(someFunction()))
print(next(someFunction()))
print(next(someFunction()))

x1 = someFunction()
print(next(x1), next(x1))
x2 = someFunction()
print([p for p in x2])
