def fib(max):
    prev, cur = 0, 1
    count = 0
    while count < max:
        count += 1
        yield cur
        prev, cur = cur, prev + cur
print(list(fib(100)))