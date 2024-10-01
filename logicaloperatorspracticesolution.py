# Example 1: Using 'and' (both conditions must be True)
x = 5
y = 10
print(x > 0 and y > 5)  # Guess: True or False?

# Example 2: Using 'or' (one of the conditions must be True)
a = 7
b = 3
print(a < 10 or b > 5)  # Guess: True or False?

# Example 3: Using 'not' (reverses the result)
c = 15
print(not c > 20)  # Guess: True or False?

# Example 4: Combining 'and' and 'or'
age = 18
has_ID = True
print(age >= 18 and has_ID or age > 16)  # Guess: True or False?

# Example 5: More complex with 'not'
password = "Python123"
is_admin = False
print(password == "Python123" and not is_admin)  # Guess: True or False?

# CHALLENGE QUESTION #1: Can you create a logical expression that checks if a number is between 10 and 20 (inclusive)?

number = 15

if number < 20 and number > 10:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20")
# Hint: You’ll need to use and to check if the number is greater than or equal to 10 and less than or equal to 20.
# What happens if you use multiple and and or conditions? Try combining at least 3 different comparisons with both operators!

if (number == 15) or (number / 10 < 2 and number > 10) or (number == 18):
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20")

# CHALLENGE QUESTION #2:
# The user must answer whether they have a key, a map, and a flashlight.
# The treasure can only be found if:
# They have the key and the flashlight, or
# They have the key and the map.
# If the user meets these conditions, print "You found the treasure!". If not, print "You did not find the treasure."

key = input("Do you have a key? (yes/no): ").strip().lower()
map = input("Do you have a map? (yes/no): ").strip().lower()
flashlight = input("Do you have a flashlight? (yes/no): ").strip().lower()

# Check the treasure conditions
if (key == "yes" and flashlight == "yes") or (key == "yes" and map == "yes"):
    print("You found the treasure!")
else:
    print("You did not find the treasure.")





# EXTENSION Challenge Questions:
# Can you modify the game so that the player must have all three items (key, map, and flashlight) to find the treasure?
# What happens if the user enters something other than "yes" or "no"? Try to handle that in the program.

# Without while loop - does not ask multiple times to enter again if input is invalid:
key = input("Do you have a key? (yes/no): ").strip().lower()
if (key != "yes") and (key != "no"):
    key = input("Please enter yes or no. Do you have a key? (yes/no): ").strip().lower()
map = input("Do you have a map? (yes/no): ").strip().lower()
if (map != "yes") and (map != "no"):
    map = input("Please enter yes or no. Do you have a map? (yes/no): ").strip().lower()
flashlight = input("Do you have a flashlight? (yes/no): ").strip().lower()
if (flashlight != "yes") and (flashlight != "no"):
    flashlight = input("Please enter yes or no. Do you have a map? (yes/no): ").strip().lower()

if (key == "yes" and flashlight == "yes" and map == "yes"):
    print("You found the treasure!")
else:
    print("You did not find the treasure.")

# With while loop
key = input("Do you have a key? (yes/no): ").strip().lower()
while (key != "yes") and (key != "no"):
    key = input("Please enter yes or no. Do you have a key? (yes/no): ").strip().lower()
map = input("Do you have a map? (yes/no): ").strip().lower()
while (map != "yes") and (map != "no"):
    map = input("Please enter yes or no. Do you have a map? (yes/no): ").strip().lower()
flashlight = input("Do you have a flashlight? (yes/no): ").strip().lower()
while (flashlight != "yes") and (flashlight != "no"):
    flashlight = input("Please enter yes or no. Do you have a map? (yes/no): ").strip().lower()

if (key == "yes" and flashlight == "yes" and map == "yes"):
    print("You found the treasure!")
else:
    print("You did not find the treasure.")