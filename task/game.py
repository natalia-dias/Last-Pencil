def possible_errors(p):
    values = [1, 2, 3]
    _step = 0
    while True:
        try:
            _step = int(input())
        except ValueError:
            print("Possible values: '1', '2' or '3'")
            continue
        if _step not in values:
            print("Possible values: '1', '2' or '3'")
        elif _step > p:
            print("Too many pencils were taken")
            continue
        else:
            return _step


def jack_strategy(jack_pen):
    jack_step = 0
    if jack_pen % 4 == 2:
        jack_step = 1
        print(jack_step)
    elif jack_pen % 4 == 3:
        jack_step = 2
        print(jack_step)
    elif jack_pen % 4 == 0:
        jack_step = 3
        print(jack_step)
    print(pencil_to_use * (jack_pen - jack_step))
    jack_pen -= jack_step
    while jack_pen != 0:
        print("John's turn!")
        a = possible_errors(jack_pen)
        print(pencil_to_use * (jack_pen - a))
        jack_pen -= a
        if jack_pen == 0:
            print("Jack won!")
            break
        if a == 1:
            jack_step = 3
            print("Jack's turn: \n", jack_step)
            print(pencil_to_use * (jack_pen - jack_step))
            jack_pen -= jack_step
        elif a == 2:
            jack_step = 2
            print("Jack's turn: \n", jack_step)
            print(pencil_to_use * (jack_pen - jack_step))
            jack_pen -= jack_step
        elif a == 3:
            jack_step = 1
            print("Jack's turn: \n", jack_step)
            print(pencil_to_use * (jack_pen - jack_step))
            jack_pen -= jack_step


def john_strategy(j_pencils):
    while True:
        print("John's turn!")
        a_j = possible_errors(j_pencils)
        print(pencil_to_use * (j_pencils - a_j))
        j_pencils -= a_j
        if j_pencils == 1:
            print("Jack's turn:")
            print("1")
            print("John won!")
            break
        elif j_pencils == 3:
            print("Jack's turn:", "2", sep="\n")
            j_pencils -= 2
            print(pencil_to_use * j_pencils)
            print("John's turn!")
            possible_errors(j_pencils)
            print("Jack won!")
            break
        elif j_pencils == 2:
            print("Jack's turn:", "1", sep="\n")
            j_pencils -= 1
            print(pencil_to_use * j_pencils)
            print("John's turn!")
            possible_errors(j_pencils)
            print("Jack won!")
            break
        elif j_pencils == 4:
            print("Jack's turn:", "3", sep="\n")
            j_pencils -= 3
            print(pencil_to_use * j_pencils)
            print("John's turn!")
            possible_errors(j_pencils)
            print("Jack won!")
            break
        elif j_pencils == 0:
            print("Jack won!")
            break
        else:
            print("Jack's turn:")
            jack_strategy(j_pencils)
            break


pencils = 0
pencil_to_use = "|"
print('How many pencils would you like to use:')
while True:
    try:
        pencils = int(input())
    except ValueError:
        print("The number of pencils should be numeric")
        continue
    if pencils <= 0:
        print("The number of pencils should be positive")
        continue
    else:
        break
print("Who will be the first (John, Jack):")
players = ['John', 'Jack']
step = 0
while True:
    player = input()
    if player in players:
        print(pencil_to_use * pencils)
        break
    else:
        print("Choose between 'John' and 'Jack'")
        continue
if player == "John":
    john_strategy(pencils)
else:
    if pencils == 1:
        print("Jack's turn:")
        print("1")
        print("John won!")
    else:
        jack_strategy(pencils)
