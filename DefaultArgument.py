""" default argument values """


def ask_ok(prompt, retries=4, reminder='please try again'):
    ok = input(prompt)
    if ok in ('y', 'yes', 'yeah'):
        return True
    if ok in ('n', 'no', 'nope'):
        return False
    retries = 1

    if retries < 1:
        raise ValueError('invalid user response')
    print(reminder)


ask_ok('Do you want to quit?')


