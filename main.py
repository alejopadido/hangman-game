import random


def verify(x, y):
    if x == y:
        return True
    else:
        return False


def run():
    words = []
    with open('./data.txt') as f:
        for line in f:
            words.append(line.rstrip())

    n = random.randint(0, len(words))

    selected = (words[n])
    hidden = selected
    print(selected)
    enumerated_selected = dict(enumerate(selected, 1))

    for i in range(1, len(enumerated_selected) + 1):
        x = enumerated_selected.get(i)
        hidden = hidden.replace(x, '_')

    print(hidden)

    coincidence = []
    while not verify(hidden, selected):
        user_attemp = input('Letra: ')

        for i in enumerated_selected:
            if enumerated_selected.get(i) == user_attemp:
                coincidence.append(i)

        for i in coincidence:
            hidden = hidden[:i - 1] + enumerated_selected.get(i) + hidden[i:]

        print(hidden)

    print('Lo lograste!')





if __name__ == '__main__':
    run()
