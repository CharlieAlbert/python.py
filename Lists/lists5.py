# iterating through lists


courses = ['Art', 'History', 'Physics', 'Maths']
numbers = [3, 5, 7, 9, 2]

for item in numbers:
    print(item)

for index, item in enumerate(courses, start=1):
    print(index, item)


