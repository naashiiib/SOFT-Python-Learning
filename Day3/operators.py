# Day 3 - Operators

# 1. Declare your age as integer variable
age = 18
print('My age is:', age)

# 2. Declare your height as a float variable
height = 1.65
print('My height is:', height)

# 3. Declare a variable that store a complex number
complex_number = 2 + 3j
print('Complex number:', complex_number)

# 4. Calculate the area of a triangle
base = float(input('Enter base: '))
triangle_height = float(input('Enter height: '))
area_of_triangle = 0.5 * base * triangle_height
print('The area of the triangle is:', area_of_triangle)

# 5. Calculate the perimeter of a triangle
side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))
perimeter_of_triangle = side_a + side_b + side_c
print('The perimeter of the triangle is:', perimeter_of_triangle)

# 6. Calculate area and perimeter of a rectangle
length = float(input('Enter length: '))
width = float(input('Enter width: '))

area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)

print('Area of rectangle:', area_of_rectangle)
print('Perimeter of rectangle:', perimeter_of_rectangle)

# 7. Calculate area and circumference of a circle
radius = float(input('Enter radius: '))
pi = 3.14

area_of_circle = pi * radius * radius
circumference = 2 * pi * radius

print('Area of circle:', area_of_circle)
print('Circumference of circle:', circumference)

# 8. Calculate slope, x-intercept and y-intercept of y = 2x - 2
slope = 2
y_intercept = -2
x_intercept = 1

print('Slope:', slope)
print('X-intercept:', x_intercept)
print('Y-intercept:', y_intercept)

# 9. Find slope and Euclidean distance
x1 = 2
y1 = 2
x2 = 6
y2 = 10

slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print('Slope:', slope)
print('Euclidean distance:', distance)

# 10. Compare the slopes in tasks 8 and 9
slope_task_8 = 2
slope_task_9 = (10 - 2) / (6 - 2)

print('Are the slopes equal:', slope_task_8 == slope_task_9)

# 11. Calculate y = x^2 + 6x + 9
x = -3
y = x ** 2 + 6 * x + 9

print('Value of y:', y)

# 12. Find length of python and dragon
python_length = len('python')
dragon_length = len('dragon')

print('Length of python:', python_length)
print('Length of dragon:', dragon_length)
print('Python length is less than dragon:', python_length < dragon_length)

# 13. Check if 'on' is found in both python and dragon
print('on' in 'python' and 'on' in 'dragon')

# 14. Check if 'jargon' is in the sentence
sentence = 'I hope this course is not full of jargon.'
print('jargon' in sentence)

# 15. Check if 'on' is not in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')

# 16. Find length of python, convert to float and string
python_length = len('python')
python_float = float(python_length)
python_string = str(python_length)

print('Length:', python_length)
print('Float:', python_float)
print('String:', python_string)

# 17. Check if a number is even
number = 10
print('Is the number even:', number % 2 == 0)

# 18. Check floor division of 7 by 3 and int value of 2.7
print(7 // 3 == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# 20. Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)

# 21. Calculate weekly earning
hours = float(input('Enter hours: '))
rate_per_hour = float(input('Enter rate per hour: '))

weekly_earning = hours * rate_per_hour
print('Your weekly earning is:', weekly_earning)

# 22. Calculate number of seconds lived
years_lived = int(input('Enter number of years you have lived: '))

seconds_in_a_year = 365 * 24 * 60 * 60
seconds_lived = years_lived * seconds_in_a_year

print('You have lived for', seconds_lived, 'seconds.')

# 23. Display the table
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')