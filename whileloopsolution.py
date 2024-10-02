# -----------------------------------
# PROBLEM #1: Guessing Game
# -----------------------------------
# Goal: Write a program that keeps asking the user to guess a number until
# they guess the correct number (5). After the correct guess, print "You guessed it!" and stop the loop.

# Initialize the correct number
correct_number = 13
# Get the user's guess
guess = int(input("Guess a number:"))
# Keep asking the user for a guess until they get it right
while guess != correct_number:
    if guess > 13:
        print("Try again! Go lower")
    else:
        print("Try again! Go higher")
    guess = int(input("Guess a number:"))
# When they guess correctly, print this:
print("You guessed it!")

# -----------------------------------
# PROBLEM #2: Counting to 10
# -----------------------------------
# Goal: Write a program that counts from 1 to 10 and prints each number.
counter = 0
# Initialize a counter variable

# While the counter is less than or equal to 10, repeat the loop
while counter < 10:
    print(counter+1)
    counter += 1


# -----------------------------------
# PROBLEM #3: Storing Positive Numbers
# -----------------------------------
# Goal: Write a program that keeps asking the user for a number and adds it to a list. The loop stops when the user enters a negative number. At the end, print the total sum of the positive numbers and also print the list of numbers entered.


# Initialize an empty list to store the numbers

list = []
# Initialize the first number
number = int(input("Please enter a positive number: "))
# Keep asking for numbers and add them to the list until the user enters a negative number
while number > 0:
    list.append(number)
    number = int(input("Please enter a positive number: "))

total = sum(list)

print(total)


# Calculate the total sum of the numbers in the list


# Print the list of numbers and the total sum



# -----------------------------------
# PROBLEM #3: Countdown Timer
# -----------------------------------
# Goal: Write a program that starts at 10, prints each number as it counts down,
# and prints "Blast off!" when it reaches 0.

# Initialize the countdown number
number = 10
# Create a while loop that continues as long as countdown is greater than or equal to 0
while number >= 0:
    print(number)
    number -= 1

print("Blast off!")


# After the loop finishes, print "Blast off!"



# -----------------------------------
# PROBLEM #4 SPICY CHALLENGE: Number Guessing with a Limit
# -----------------------------------
# Goal: Write a program that lets the user guess the correct number (5),
# but they only have 5 tries. If they guess the number within 5 tries, print "You guessed it!"
# If they don't guess correctly after 5 attempts, print "Out of attempts!"

# Initialize the correct number and the number of attempts
number = 15
counter = 1
num_attempts = 5
# Get the user's first guess
guess = int(input("Guess a number:"))
while counter < num_attempts:
    if guess == number:
        print("You guessed it!")
    elif counter < num_attempts:
        guess = int(input("Guess a number:"))
        counter += 1

if guess != number:
    print("Out of attempts!")




# Loop while the user hasn't guessed the correct number and still has attempts left


# After the loop, check if they guessed correctly or ran out of attempts
