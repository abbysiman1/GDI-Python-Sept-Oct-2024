# Start with an empty grocery list
grocery_list = []

# 1. Append 'apples' to the list
grocery_list.append('apples')
print(grocery_list)  # Should show ['apples']

# 2. Append 'bananas' to the list
grocery_list.append('bananas')
print(grocery_list)  # Should show ['apples', 'bananas']

# 3. Append 'carrots' to the list
grocery_list.append('carrots')
print(grocery_list)  # Should show ['apples', 'bananas', 'carrots']

# 4. Pop the last item from the list (remove 'carrots')
grocery_list.pop()
print(grocery_list)  # Should show ['apples', 'bananas']

# 5. Append 'oranges' to the list
grocery_list.append('oranges')
print(grocery_list)  # Should show ['apples', 'bananas', 'oranges']

# 6. Pop the last item from the list (remove 'oranges')
grocery_list.pop()
print(grocery_list)  # Should show ['apples', 'bananas']

# 7. Append 'grapes' to the list
grocery_list.append('grapes')
print(grocery_list)  # Should show ['apples', 'bananas', 'grapes']

# CHALLENGE QUESTION: What happens if you try to pop an item from an empty list?
empty_list = []
empty_list.pop()  # Attempt to pop from an empty list
# Output the empty list to confirm it's still empty
print(empty_list)  # Should show []