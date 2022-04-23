
# looping through items in a dictionary


student = {'name': 'Albert', 'age': 26, 'courses': ['Maths', 'CompSci'], 'phone': '254-321'}

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
