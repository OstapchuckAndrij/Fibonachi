def fibonacci(n):
    fib_numbers = [0, 1]

    for i in range(2, n):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])

    return fib_numbers

# Введіть бажану кількість чисел Фібоначчі
n = int(input("Введіть кількість чисел Фібоначчі: "))

result = fibonacci(n)
print(f"Перші {n} чисел Фібоначчі: {result}")