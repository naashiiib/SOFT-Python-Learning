# Day 7 - Sets

# 1. Create an empty set
empty_set = set()
print(empty_set)

# 2. Create a set containing 0 to 10
numbers = set(range(11))
print(numbers)

# 3. Remove an item from the set
numbers.remove(10)
print(numbers)

# 4. Add an item to the set
numbers.add(10)
print(numbers)

# 5. Add multiple items to the set
numbers.update([11, 12, 13])
print(numbers)

# 6. Remove an item from the set
numbers.remove(13)
print(numbers)

# 7. Clear the set
numbers_copy = numbers.copy()
numbers_copy.clear()
print(numbers_copy)

# 8. Delete the set
del empty_set

# 9. Create two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 10. Find the union of A and B
print('Union:', A.union(B))

# 11. Find the intersection of A and B
print('Intersection:', A.intersection(B))

# 12. Check if A is a subset of B
print('A is subset of B:', A.issubset(B))

# 13. Check if A and B are disjoint
print('A and B are disjoint:', A.isdisjoint(B))

# 14. Join A with B
print('Union using |:', A | B)

# 15. Find the symmetric difference
print('Symmetric difference:', A.symmetric_difference(B))

# 16. Delete the sets
del A
del B

# 17. Create two sets
python = {'Python', 'JavaScript', 'C++', 'HTML', 'CSS'}
web = {'HTML', 'CSS', 'JavaScript', 'React', 'Node.js'}

# 18. Find the union
print('Union:', python | web)

# 19. Find the intersection
print('Intersection:', python & web)

# 20. Find the difference
print('Python only:', python - web)
print('Web only:', web - python)

# 21. Check if a set is a subset
frontend = {'HTML', 'CSS'}
print('Frontend is subset:', frontend.issubset(web))

# 22. Check if two sets are disjoint
print('Python and web are disjoint:', python.isdisjoint(web))

# 23. Find the symmetric difference
print('Symmetric difference:', python ^ web)

# 24. Add an item
python.add('Django')
print(python)

# 25. Add multiple items
python.update(['Flask', 'FastAPI'])
print(python)

# 26. Remove an item
python.remove('Flask')
print(python)

# 27. Discard an item
python.discard('FastAPI')
print(python)

# 28. Create a set of programming languages
languages = {
    'Python',
    'C++',
    'JavaScript',
    'Java',
    'C'
}

print('Programming languages:', languages)

# 29. Check if Python is in the set
print('Python' in languages)

# 30. Find the number of programming languages
print('Number of languages:', len(languages))