import random


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
    print(enumerated_selected)
    print(len(enumerated_selected))

    for i in range(1, len(enumerated_selected) + 1):
        x = enumerated_selected.get(i)
        hidden = hidden.replace(x, '_')

    print(hidden)

    user_attemp = input('Letra: ')
    coincidence = []

    for i in enumerated_selected:
        if enumerated_selected.get(i) == user_attemp:
            coincidence.append(i)
    print(coincidence)

    for i in coincidence:
        hidden = hidden[:i - 1] + enumerated_selected.get(i) + hidden[i + 1:]

    print(hidden)


if __name__ == '__main__':
    run()
