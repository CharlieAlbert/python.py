""" Fibonacci series upto n """


def fib(n):
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)  # result = result + [a]
        a, b = b, a + b

    return result


fib(1000)
