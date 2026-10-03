# Day 5 - Lists

# 1. Declare an empty list
my_list = []
print(my_list)

# 2. Declare a list with more than 5 items
my_items = ['Python', 'C++', 'HTML', 'CSS', 'JavaScript', 'GitHub']
print(my_items)

# 3. Find the length of your list
print('Length of my list:', len(my_items))

# 4. Get the first item, middle item and last item
print('First item:', my_items[0])
print('Middle item:', my_items[len(my_items) // 2])
print('Last item:', my_items[-1])

# 5. Declare a list with mixed data types
mixed_data_types = ['Nashib', 18, 1.65, 'Nilambur', 'Single']
print(mixed_data_types)

# 6. Declare a list of companies
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(companies)

# 7. Print the list
print(companies)

# 8. Print the number of companies
print('Number of companies:', len(companies))

# 9. Print the first, middle and last company
print('First company:', companies[0])
print('Middle company:', companies[len(companies) // 2])
print('Last company:', companies[-1])

# 10. Print each company
for company in companies:
    print(company)

# 11. Change each company name to uppercase
for company in companies:
    print(company.upper())

# 12. Add a new company to the companies list
companies.append('Tesla')
print(companies)

# 13. Insert a company in the middle of the companies list
companies.insert(len(companies) // 2, 'Netflix')
print(companies)

# 14. Change one of the company names
companies[0] = 'Meta'
print(companies)

# 15. Change one of the company names to uppercase
companies[1] = companies[1].upper()
print(companies)

# 16. Join the companies with a string
print('#; '.join(companies))

# 17. Check if a company exists in the list
print('Apple' in companies)

# 18. Sort the list
companies.sort()
print(companies)

# 19. Reverse the list
companies.reverse()
print(companies)

# 20. Slice out the first 3 companies
print(companies[:3])

# 21. Slice out the last 3 companies
print(companies[-3:])

# 22. Slice out the middle company or companies
middle = len(companies) // 2
print(companies[middle])

# 23. Remove the first company
companies.pop(0)
print(companies)

# 24. Remove the middle company
companies.pop(len(companies) // 2)
print(companies)

# 25. Remove the last company
companies.pop()
print(companies)

# 26. Remove all companies
companies.clear()
print(companies)

# 27. Destroy the companies list
del companies

# 28. Join two lists
front_end = ['HTML', 'CSS', 'JavaScript', 'React']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

# 29. Copy the list
my_list = ['Python', 'C++', 'HTML', 'CSS']
copied_list = my_list.copy()

print('Original list:', my_list)
print('Copied list:', copied_list)

# 30. Count an item in a list
numbers = [1, 2, 3, 4, 5, 5, 5, 6]
print('Number of 5s:', numbers.count(5))

# 31. Find the index of an item
print('Index of Python:', my_list.index('Python'))

# 32. Check if an item exists
print('Python' in my_list)

# 33. Add an item using append()
my_list.append('GitHub')
print(my_list)

# 34. Remove an item using remove()
my_list.remove('GitHub')
print(my_list)

# 35. Create a list of numbers
numbers = [1, 2, 3, 4, 5]

print('Sum:', sum(numbers))
print('Minimum:', min(numbers))
print('Maximum:', max(numbers))