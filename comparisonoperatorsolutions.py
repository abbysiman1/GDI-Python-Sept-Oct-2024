# Comparing numbers
number1 = 10
number2 = 20

# Try to guess the output before running!
print(number1 > number2)    # Guess: True or False?
print(number1 < number2)    # Guess: True or False?
print(number1 == 10)        # Guess: True or False?
print(number2 != 15)        # Guess: True or False?
print(number1 >= 10)        # Guess: True or False?
print(number2 <= 25)        # Guess: True or False?

# Comparing strings
string1 = "apple"
string2 = "banana"

# Try to guess the output before running!
print(string1 == string2)   # Guess: True or False?
print(string1 != string2)   # Guess: True or False?
print(string1 > string2)    # Guess: True or False? (Hint: Alphabetical order)
print(string1 < string2)    # Guess: True or False? (Hint: Alphabetical order)

# Now, let's compare strings with different capitalizations
string3 = "Apple"
string4 = "apple"

# Try to guess the output before running!
print(string3 == string4)   # Guess: True or False? (Does capitalization matter?)
print(string3 != string4)   # Guess: True or False?
print(string3 > string4)    # Guess: True or False? (Hint: Alphabetical order with capitalization)
print(string3 < string4)    # Guess: True or False?

# Comparing string lengths
print(len(string1) == len(string2))  # Guess: True or False?
print(len(string1) < len(string2))   # Guess: True or False?

# CHALLENGE QUESTION #1 Can you write a comparison to check if the length of string1 is greater than or equal to 5?
if len(string1) >= 5:
    print("True")
else:
    print("False")
# CHALLENGE QUESTION #2: What happens when you compare the number 10 and the string "10"? Try it and see the result.
print(10 == "10")