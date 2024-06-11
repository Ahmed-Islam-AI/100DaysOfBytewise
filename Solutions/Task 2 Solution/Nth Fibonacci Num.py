def fibonacci_Series(n):
    if n <= 1:
        return n
    else:
        return fibonacci_Series(n-1) + fibonacci_Series(n-2)

n = 10
nth_fibonacci = fibonacci_Series(n)
print(f"The {n}th Fibonacci number is {nth_fibonacci}.")
