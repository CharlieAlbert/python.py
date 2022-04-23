#least employee id is 300

nam = input('Enter your name: ')
name = str(nam)

id = input('Enter your employee id: ')
ID = int(id)

if ID <= 400:
    print('Janitors are not allowed to access this site')
elif ID >= 450:
    print('Welcome ', name)
    inp_hr = input('Enter the number of hours worked: ')
    hours = int(inp_hr)
    rate = 300
    total = hours * rate

print('Your total wage is ', total)



