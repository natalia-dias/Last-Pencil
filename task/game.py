# function that prevents errors with number of taken pencils (== _step)
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


# winning strategy for bot. Is used in case of Jack's first step
# and in case John lets winning combination for the bot
def jack_strategy(jack_pen):
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
            print("Jack's turn:")
            print(jack_step)
            print(pencil_to_use * (jack_pen - jack_step))
            jack_pen -= jack_step
        elif a == 2:
            jack_step = 2
            print("Jack's turn:")
            print(jack_step)
            print(pencil_to_use * (jack_pen - jack_step))
            jack_pen -= jack_step
        elif a == 3:
            jack_step = 1
            print("Jack's turn:")
            print(jack_step)
            print(pencil_to_use * (jack_pen - jack_step))
            jack_pen -= jack_step


pencils = 0
pencil_to_use = "|"

# 1st fase: number of pencils
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

# 2nd fase: players chose and avoidance of possible errors
print("Who will be the first (John, Jack):")
players = ['John', 'Jack']
while True:
    player = input()
    if player in players:
        print(pencil_to_use * pencils)
        break
    else:
        print("Choose between 'John' and 'Jack'")
        continue

# 3rd fase: game
while True:
    if pencils == 0:
        print(f'{player} won!')
        break
    if player == "Jack":
        if pencils == 1:
            print("Jack's turn:")
            print("1")
            print("John won!")
            break
        elif pencils == 2 or pencils % 4 == 2:
            print("Jack's turn:")
            print("1")
            pencils -= 1
            print(pencil_to_use * pencils)
            jack_strategy(pencils)
            break
        elif pencils == 3 or pencils % 4 == 3:
            print("Jack's turn:")
            print("2")
            pencils -= 2
            print(pencil_to_use * pencils)
            jack_strategy(pencils)
            break
        elif pencils == 4 or pencils % 4 == 0:
            print("Jack's turn:")
            print("3")
            pencils -= 3
            print(pencil_to_use * pencils)
            jack_strategy(pencils)
            break
        elif pencils % 4 == 1:
            print("Jack's turn:")
            print("2")
            pencils -= 2
            print(pencil_to_use * pencils)
            player = "John"
    else:
        if pencils == 1:
            print("John's turn!")
            step = possible_errors(pencils)
            print("Jack won!")
            break
        print('John\'s turn!')
        step = possible_errors(pencils)
        pencils -= step
        print(pencil_to_use * pencils)
        player = "Jack"
