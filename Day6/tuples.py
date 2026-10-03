# Day 6 - Tuples

# 1. Create an empty tuple
empty_tuple = ()
print(empty_tuple)

# 2. Create a tuple containing names of sisters
sisters = ('Aisha', 'Fathima', 'Riya')
print(sisters)

# 3. Create a tuple containing names of brothers
brothers = ('Arjun', 'Rahul', 'Adil')
print(brothers)

# 4. Join brothers and sisters
siblings = sisters + brothers
print('Siblings:', siblings)

# 5. Count the number of siblings
print('Number of siblings:', len(siblings))

# 6. Modify the tuple by creating a new tuple
family_members = siblings + ('Nashib',)
print('Family members:', family_members)

# 7. Unpack siblings
sister1, sister2, sister3, brother1, brother2, brother3 = siblings

print('Sister 1:', sister1)
print('Sister 2:', sister2)
print('Sister 3:', sister3)
print('Brother 1:', brother1)
print('Brother 2:', brother2)
print('Brother 3:', brother3)

# 8. Check if an item exists in the tuple
print('Aisha' in siblings)

# 9. Convert tuple to list
siblings_list = list(siblings)
print('Siblings as list:', siblings_list)

# 10. Convert list back to tuple
siblings_tuple = tuple(siblings_list)
print('Siblings as tuple:', siblings_tuple)

# 11. Delete the tuple
del empty_tuple

# 12. Check if a value exists in a tuple
countries = ('India', 'USA', 'UK', 'Canada', 'Australia')
print('India' in countries)

# 13. Find the index of an item
print('Index of India:', countries.index('India'))

# 14. Find the length of the tuple
print('Number of countries:', len(countries))

# 15. Slice the tuple
print('First three countries:', countries[:3])
print('Last three countries:', countries[-3:])

# 16. Count an item
numbers = (1, 2, 3, 2, 4, 2, 5)
print('Number of 2s:', numbers.count(2))

# 17. Find the minimum and maximum
print('Minimum:', min(numbers))
print('Maximum:', max(numbers))

# 18. Find the sum
print('Sum:', sum(numbers))