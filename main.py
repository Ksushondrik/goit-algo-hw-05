def caching_fibonacci():
    cache = {}                  # створення області кешу

    def fibonacci(n):
        nonlocal cache          # отримуємо доступ до списку оголошеного в зовнішній ф-ції
        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        elif n in cache:
            result = cache[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)            # використовуємо рекурсію, для обчислення послідовності Фібоначчі
            cache[n] = result
        return result

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(20))  # Виведе 610
