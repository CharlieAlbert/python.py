# sets use curly braces and are unordered


courses = {'History', 'Maths', 'Physics', 'CompSci'}
art_courses = {'History', 'Maths', 'Art', 'Design'}

print(courses)
print(courses.intersection(art_courses))
print(courses.difference(art_courses))
print(courses.union(art_courses))

# Empty set
create = set()
print(create)
