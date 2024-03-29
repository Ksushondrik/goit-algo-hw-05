def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        nonlocal cache
        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        elif n in cache:
            result = cache[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
        return result

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))
