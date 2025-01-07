def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    num = 6  
    result = fibonacci(num)
    print(f"The Fibonacci number at position {num} is: {result}")
    return result
main()
