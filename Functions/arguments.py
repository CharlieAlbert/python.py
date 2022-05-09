# *args is for positional arguments and **kwargs is for key word arguments


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


units = ['Numerical analysis', 'Computer networks', 'Design analysis', 'Software engineering']
info = {'name': 'Charles', 'course': 'Computer Science', 'campus': 'Kabarak'}


student_info(*units, **info)




