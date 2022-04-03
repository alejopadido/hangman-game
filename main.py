import random
import sys


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b)
    return s


def verify(x, y):
    if x == y:
        return True
    else:
        return False


def run():
    with open('./data.txt') as f:
        words = [line.rstrip() for line in f]

    n = random.randint(0, len(words))

    selected = (words[n])
    hidden = selected
    enumerated_selected = dict(enumerate(selected, 1))


    print(selected)

    for i in range(1, len(enumerated_selected) + 1):
        x = enumerated_selected.get(i)
        hidden = hidden.replace(x, '_')

    print(hidden)

    coincidence = []
    lifes = 6
    while not verify(hidden, selected):
        user_attemp = input('Letra: ')

        for i in enumerated_selected:
            if normalize(enumerated_selected.get(i)) == user_attemp:
                coincidence.append(i)

        if not (user_attemp in normalize(selected)):
            lifes -= 1
            print('Esa letra no está')
            print('Vidas: ', lifes)

        if lifes == 0:
            sys.exit()

        for i in coincidence:
            hidden = hidden[:i - 1] + enumerated_selected.get(i) + hidden[i:]

        print(hidden)

    print('Lo lograste!')





if __name__ == '__main__':
    run()
