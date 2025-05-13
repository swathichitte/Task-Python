def fibonacci_count(limit):
    a, b = 0, 1
    count = 0
    while a <= limit:
        count += 1
        a, b = b, a + b
    return count

limit = 500
result = fibonacci_count(limit)
print(f"The count of Fibonacci numbers between 0 and {limit} is {result}")
