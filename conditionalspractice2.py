# QUESTION #1 NUMBER COMPARISON: Write a program that given a number checks if it is positive, negative, or zero. Use if, else, and if-else statements to print the correct result.
number = float(input("Enter a number:"))

if number > 0:
    print("Your number is positive")
elif number == 0:
    print("Your number is zero")
else:
    print("Your number is negative")

#QUESTION #2 CHECK AGE FOR VOTING: Write a program that asks the user for their age and checks if they are old enough to vote (18 or older). Print a message depending on whether they can vote or not.

age = float(input("What is your age? "))

if age >= 18:
    print("You can vote!")
else:
    print("Sorry, you are not old enough to vote.")
#CHALLENGE QUESTION #3: As a bonus challenge, write a program that asks for the current temperature and:
# Prints "It's hot!" if the temperature is greater than or equal to 85.
# Prints "It's cold!" if the temperature is less than 60.
# Prints "It's a nice day!" for any temperature in between.

temperature = float(input("What is the temperature? "))

if temperature >= 85:
    print("It's hot!")
elif temperature < 60:
    print("It's cold!")
else:
    print("It's a nice day!")