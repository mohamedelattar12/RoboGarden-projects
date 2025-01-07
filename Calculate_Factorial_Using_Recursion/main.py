def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

def main():
    num = 5  # You can change this number to test with other inputs
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
    return result

main()
