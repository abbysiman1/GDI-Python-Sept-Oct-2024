# -----------------------------------
# Practice 0: Say Hi to Someone
# -----------------------------------
print("Practice 0: Say Hi to Someone")
# Define a function that says "Hi" to a given name
def say_hi(name):
    print("Hi", name)

# Call the function with a name
say_hi("Linette")
say_hi("Gwen")
say_hi("Keiko")
say_hi("Melissa")
print("\n")


# -----------------------------------
# Practice 1: Simple Calculator Function
# -----------------------------------
print("Practice 1: Simple Calculator")

# Define a function that adds, subtracts, multiplies, and divides two numbers
def calculator(num1, num2):
    print(f"You typed in {num1} and {num2}")
    print("The sum of these numbers is", num1 + num2)
    print("The difference of these numbers is", num1 - num2)
    print("The product of these numbers is", num1 * num2)
    print("The quotient of these numbers is", num1 / num2 if num2 != 0 else "undefined")

# Call the function with some test data
calculator(1, 3)
print("\n")


# -----------------------------------
# Practice 2: Tip Calculator Function
# -----------------------------------
print("Practice 2: Tip Calculator")

# Define a function that calculates the tip for a given bill and tip percentage
def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip
    print(f"The total amount after a {tip_percentage}% tip is: ${total_amount:.2f}")

# Call the function with some test data
calculate_tip(100, 15)
print("\n")


# -----------------------------------
# Practice 3: Celsius to Fahrenheit Converter
# -----------------------------------
print("Practice 3: Celsius to Fahrenheit Converter")

# Define a function that converts Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Call the function with some test data
print(f"30°C is {celsius_to_fahrenheit(30)}°F")
print("\n")


# -----------------------------------
# Practice 4: Finding the Largest Number in a List
# -----------------------------------
print("Practice 4: Finding the Largest Number in a List")

# Define a function that finds the largest number in a list
def find_largest_number(numbers_list):
    largest = numbers_list[0]
    for number in numbers_list:
        if number > largest:
            largest = number
    return largest

# Call the function with some test data
numbers = [99, 49, 11, 2, 9, 50]
largest_number = find_largest_number(numbers)
print("The largest number in the list is:", largest_number)
print("\n")


# -----------------------------------
# Practice 5: Grade Calculator
# -----------------------------------
print("Practice 5: Grade Calculator")

# Define a function that calculates the grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

# Call the function with some test data
grade = calculate_grade(85)
print(f"A percentage of 85% gives a grade of: {grade}")
print("\n")


# -----------------------------------
# Practice 6: Prime Number Checker
# -----------------------------------
print("Practice 6: Prime Number Checker")

# Define a function that checks if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Call the function with some test data
test_number = 7
print(f"{test_number} is prime: {is_prime(test_number)}")
test_number = 15
print(f"{test_number} is prime: {is_prime(test_number)}")