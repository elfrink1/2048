f = [0] * 16
f[1] = f[2] = 2
import random


def field(f):
    for i in range(0, 13, 4):
        print(f[i], f[i + 1], f[i + 2], f[i + 3])


def move(k, f):
    if k == 's' or k == 'S':
        for i in range(12, 16):
            if f[i] == 0:
                f[i] = f[i - 4]
                f[i - 4] = f[i - 8]
                f[i - 8] = f[i - 12]
                f[i - 12] = 0
            if f[i - 4] == 0:
                f[i - 4] = f[i - 8]
                f[i - 8] = f[i - 12]
                f[i - 12] = 0
            if f[i - 8] == 0:
                f[i - 8] = f[i - 12]
                f[i - 12] = 0
            if f[i] == f[i - 4]:
                f[i] = 2 * f[i]
                f[i - 4] = f[i - 8]
                f[i - 8] = f[i - 12]
                f[i - 12] = 0
            if f[i - 4] == f[i - 8]:
                f[i - 4] = 2 * f[i - 4]
                f[i - 8] = f[i - 12]
                f[i - 12] = 0
            if f[i - 8] == f[i - 12]:
                f[i - 8] = 2 * f[i - 8]
                f[i - 12] = 0
    if k == 'w' or k == 'W':
        for i in range(0, 4):
            if f[i] == 0:
                f[i] = f[i + 4]
                f[i + 4] = f[i + 8]
                f[i + 8] = f[i + 12]
                f[i + 12] = 0
            if f[i + 4] == 0:
                f[i + 4] = f[i + 8]
                f[i + 8] = f[i + 12]
                f[i + 12] = 0
            if f[i + 8] == 0:
                f[i + 8] = f[i + 12]
                f[i + 12] = 0
            if f[i] == f[i + 4]:
                f[i] = 2 * f[i]
                f[i + 4] = f[i + 8]
                f[i + 8] = f[i + 12]
                f[i + 12] = 0
            if f[i + 4] == f[i + 8]:
                f[i + 4] = 2 * f[i + 4]
                f[i + 8] = f[i + 12]
                f[i + 12] = 0
            if f[i + 8] == f[i + 12]:
                f[i + 8] = 2 * f[i + 8]
                f[i + 12] = 0
    if k == 'd' or k == 'D':
        for i in range(15, 2, -4):
            if f[i] == 0:
                f[i] = f[i - 1]
                f[i - 1] = f[i - 2]
                f[i - 2] = f[i - 3]
                f[i - 3] = 0
            if f[i - 1] == 0:
                f[i - 1] = f[i - 2]
                f[i - 2] = f[i - 3]
                f[i - 3] = 0
            if f[i - 2] == 0:
                f[i - 2] = f[i - 3]
                f[i - 3] = 0
            if f[i] == f[i - 1]:
                f[i] = 2 * f[i]
                f[i - 1] = f[i - 2]
                f[i - 2] = f[i - 3]
                f[i - 3] = 0
            if f[i - 1] == f[i - 2]:
                f[i - 1] = 2 * f[i - 1]
                f[i - 2] = f[i - 3]
                f[i - 3] = 0
            if f[i - 2] == f[i - 3]:
                f[i - 2] = 2 * f[i - 2]
                f[i - 3] = 0
    if k == 'a' or k == "A":
        for i in range(0, 12, 4):
            if f[i] == 0:
                f[i] = f[i + 1]
                f[i + 1] = f[i + 2]
                f[i + 2] = f[i + 3]
                f[i + 3] = 0
            if f[i + 1] == 0:
                f[i + 1] = f[i + 2]
                f[i + 2] = f[i + 3]
                f[i + 3] = 0
            if f[i + 2] == 0:
                f[i + 2] = f[i + 3]
                f[i + 3] = 0
            if f[i] == f[i + 1]:
                f[i] = 2 * f[i]
                f[i + 1] = f[i + 2]
                f[i + 2] = f[i + 3]
                f[i + 3] = 0
            if f[i + 1] == f[i + 2]:
                f[i + 1] = 2 * f[i + 1]
                f[i + 2] = f[i + 3]
                f[i + 3] = 0
            if f[i + 2] == f[i + 3]:
                f[i + 2] = 2 * f[i + 2]
                f[i + 3] = 0


def spawn(f):
    rl = []
    for i in range(16):
        if f[i] == 0:
            rl.append(i)
    f[random.choice(rl)] = random.randrange(2, 5, 2)
    return f


def game():
    global f
    field(f)
    k = input("What direction do you want to move the tiles?\nPress W, A, S or D.\n")
    move(k,f)
    # win(f)
    # reset
    game()


def lose():
    pass


def reset():
    for s in f:
        f[s] = 0
    spawn(f)


def win():
    if 2048 in f:
        print("yay")
        exit()
    else:
        return False


def rungame():
    field(f)
    k = input()
    move(k, f)
    spawn(f)
    rungame()


field(f)
move(input("\n"),f)
field(f)
move(input(),f)
field(f)
move(input(),f)
field(f)

