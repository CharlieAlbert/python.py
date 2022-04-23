# adding or removing from a list


courses = ['Art', 'History', 'Physics', 'Maths']
courses_2 = ['CompSci', 'Geography', 'Chemistry']

courses.append(courses_2)
print(courses)

courses.insert(0, courses_2)
print(courses)

courses.extend(courses_2)
print(courses)

popped = courses.pop()
print('Popped string is ' + popped)
print(courses)
