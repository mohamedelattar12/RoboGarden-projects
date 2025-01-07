def calculate_average(numbers):
    total_sum = sum(numbers)
    length = len(numbers)
    average = total_sum / length if length > 0 else 0  # To avoid division by zero
    return average

def main():
    numbers = [10, 20, 30, 40, 50]
    result = calculate_average(numbers)
    print(f"The average of the list is: {result}")
    return result
main()
