def fib(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib(10000))