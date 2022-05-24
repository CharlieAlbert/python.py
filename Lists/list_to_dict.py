# merging two lists to form one dictionary


def merge():
    names = ['Charles', 'Derrick', 'Mohammed', 'Tracy']
    age = []

    n = len(names)
    for i in range(0, n):
        print('Enter age at index', i, )
        item = int(input())
        age.append(item)

    print('Names of the students are', names)
    print('The ages of the students is', age)

    data = dict(zip(names, age))

    return data


print(merge())

