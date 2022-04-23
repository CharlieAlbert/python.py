# lists sorting
# reverse function sorts the list from the last index to index 0
# sort function sorts the list in ascending order for integers or alphabetical order for strings


courses = ['Art', 'History', 'Physics', 'Maths']
numbers = [3, 5, 7, 9, 2]


sorted_courses = sorted(courses)
print(sorted_courses)

courses.reverse()
print(courses)

numbers.reverse()
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

