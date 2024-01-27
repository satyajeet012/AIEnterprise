def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number = int(input("Enter a number: "))

# Calculating and display the factorial
factorial_result = calculate_factorial(number)
print(f"The factorial of {number} is: {factorial_result}")