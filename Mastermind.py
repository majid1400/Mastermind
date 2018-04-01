import random

colors = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'yellow',
    5: 'white',
}

L = 4


initial = []
while len(initial) < L:
    r = random.randint(1, 5)
    if r not in initial:
        initial.append(r)
initial = [colors[i] for i in initial]

win = False
for turn in range(2):
    guess = input()
    guess = guess.split(",")

    white = 0
    black = 0
    for i in range(len(initial)):
        if initial[i] == guess[i]:
            black += 1
        elif guess[i] in initial:
            white += 1
    print("black {} and white {}".format(black, white))
    if black == L:
        print("Your won!")
        win = True
if not win:
    initial_status = ' , '.join(initial)
    print("شما باختید کلمات مورد نظر {} بودند".format(initial_status))
