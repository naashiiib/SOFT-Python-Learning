# Day 4 - Strings

# 1. Concatenate strings
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# 2. Concatenate strings
print('Coding' + ' ' + 'For' + ' ' + 'All')

# 3. Declare company variable
company = 'Coding For All'

# 4. Print company
print(company)

# 5. Print the length of company
print(len(company))

# 6. Change to uppercase
print(company.upper())

# 7. Change to lowercase
print(company.lower())

# 8. Use capitalize(), title(), swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut out the first word
print(company[7:])

# 10. Check if company contains Coding
print(company.find('Coding'))

# 11. Replace Coding with Python
print(company.replace('Coding', 'Python'))

# 12. Change Python for Everyone to Python for All
sentence = 'Python for Everyone'
print(sentence.replace('Everyone', 'All'))

# 13. Split Coding For All
print(company.split())

# 14. Split companies at comma
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))

# 15. Character at index 0
print(company[0])

# 16. Last index of company
print(len(company) - 1)

# 17. Character at index 10
print(company[10])

# 18. Acronym for Python For Everyone
print('PFE')

# 19. Acronym for Coding For All
print('CFA')

# 20. Position of first C
print(company.index('C'))

# 21. Position of first F
print(company.index('F'))

# 22. Last occurrence of l
company_people = 'Coding For All People'
print(company_people.rfind('l'))

# 23. First occurrence of because
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 24. Last occurrence of because
print(sentence.rfind('because'))

# 25. Slice out 'because because because'
start = sentence.find('because')
end = sentence.find('is a conjunction')

print(sentence[start:end].strip())

# 26. Find the first occurrence of because
print(sentence.find('because'))

# 27. Slice out 'because because because'
print(sentence[start:end].strip())

# 28. Does Coding For All start with Coding?
print(company.startswith('Coding'))

# 29. Does Coding For All end with coding?
print(company.endswith('coding'))

# 30. Remove left and right spaces
spaced_company = '   Coding For All   '
print(spaced_company.strip())

# 31. Check isidentifier()
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32. Join Python libraries with '# '
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))

# 33. Use new line escape sequence
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34. Use tab escape sequence
print('Name\tAge\tCountry\tCity')
print('Nashib\t18\tIndia\tKerala')

# 35. String formatting
radius = 10
area = 3.14 * radius ** 2

print('The area of a circle with radius {} is {} meters square.'.format(
    radius, int(area)
))

# 36. String formatting with arithmetic operations
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))