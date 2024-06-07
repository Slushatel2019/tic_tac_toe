import random


def init_v():
    available = [x for x in range(1, 10) if x != 5]
    status = ["x" if x == 5 else x for x in range(1, 10)]
    choices = {'x': [5],
               'o': []}
    win_combs = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [1, 4, 7],
                 [2, 5, 8],
                 [3, 6, 9],
                 [1, 5, 9],
                 [3, 5, 7]]
    return (available, status, choices, win_combs)


def draw(status):
    c = 0
    for i in range(3):
        print("+"+("-"*7+"+")*3)
        print("|"+(" "*7+"|")*3)
        print("|", end="")
        for j in range(1, 4):
            print("   "+str(status[c])+"   "+"|", end="")
            c += 1
        print()
        print("|"+(" "*7+"|")*3)
    print("+"+("-"*7+"+")*3)
    pass


def check(choices, win_combs):
    for win_comb in win_combs:
        if all([True if x in choices else False for x in win_comb]):
            return True
    return False


def play():
    available, status, choices, win_combs = init_v()
    draw(status)
    while available:
        try:
            choice_user = int(input("Enter your move: "))
        except ValueError:
            print("Enter only digit")
            continue
        if  choice_user in available and choice_user > 0 and choice_user < 10:
            available.remove(choice_user)
            status[choice_user-1] = "o"
            draw(status)
        else:
            print("select available point")
            continue
        choices['o'].append(choice_user)
        if check(choices['o'], win_combs):
            print('You won!')
            break
        choice_comp = random.choice(available)
        status[choice_comp-1] = "x"
        draw(status)
        available.remove(choice_comp)
        choices['x'].append(choice_comp)
        if check(choices['x'], win_combs):
            print('Computer won!')
            break
    else:
        print("Tie")


while True:
    play()
    answer = input("Do you want to play another one game? [y/n] ")
    if answer == "n":
        break
