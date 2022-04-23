# working with Key - value pairs
# you can access the value of a dictionary using square brackets or the get method
# you can also specify the output for keys that don't exist inside the get method


student = {'name': 'Charles', 'age': 25, 'courses': ['Maths', 'CompSci']}


print(student.get('age', ))
print(student.get('phone', 'Not Found'))

# adding values in a dictionary

student['phone'] = '254-321'
print(student.get('phone'))

# updating values using the update method

student.update({'name': 'Albert', 'age': 26})
print(student)

# deleting values using the del keyword and pop function

del student['age']
print(student)

name = student.pop('name')
print(name)
print(student)

# iterating through a list
# length of the dictionary
print(len(student))

# keys in the dictionary
print(student.keys())

# values in the dictionary
print(student.values())

# all items in the dictionary
print(student.items())
