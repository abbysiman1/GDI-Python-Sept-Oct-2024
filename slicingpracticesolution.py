# Given strings and numbers
string1 = "PythonIsFun"
string2 = "1234567890"
number = "9876543210"

# 1. Write slicing code to produce "Python" from string1
output1 = string1[0:6]

# 2. Write slicing code to produce "Fun" from string1
output2 = string1[8:]

# 3. Write slicing code to produce "34567" from string2
output3 = string2[2:7]

# 4. Write slicing code to produce "7890" from string2
output4 = string2[6:]

# 5. Write slicing code to produce "9876" from number
output5 = number[0:4]

# 6. Write slicing code to reverse the number
output6 = number[::-1]

# 7. Write slicing code to produce every second digit from the number
output7 = number[::2]

# Print the results to check if you are correct
print(output1)  # Output: Python
print(output2)  # Output: Fun
print(output3)  # Output: 34567
print(output4)  # Output: 7890
print(output5)  # Output: 9876
print(output6)  # Output: 0123456789
print(output7)  # Output: 97531

# Spicy Challenge: Write a program that checks if the variable word_or_number is a palindrome.
word_or_number = "racecar"  # Change this to test other words or numbers like "12321"

# Check if the word_or_number is the same when reversed
is_palindrome = word_or_number == word_or_number[::-1]  # Check if the original is equal to its reverse

# Print the result
print("Is palindrome:", is_palindrome)  # Output: Is palindrome: True