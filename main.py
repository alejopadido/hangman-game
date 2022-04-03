import random
import sys
import os
import keyboard


# def kb():
#     while True:
#         if keyboard.is_pressed('enter'):
#             print("A key was pressed")
#             sys.exit(0)


def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")


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


def game():
    try:
        while True:
            if keyboard.is_pressed('enter'):
                clear()
                with open('./data.txt') as f:
                    words = [line.rstrip() for line in f]

                n = random.randint(0, len(words))

                selected = (words[n])
                hidden = selected
                enumerated_selected = dict(enumerate(selected, 1))

                for i in range(1, len(enumerated_selected) + 1):
                    x = enumerated_selected.get(i)
                    hidden = hidden.replace(x, '_',)


                coincidence = []
                lifes = 6

                while not verify(hidden, selected):
                    clear()
                    print('''
            ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
            ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
            ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
            ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
            ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
            ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
    
    
    
    
    
    
                        ''')
                    print(hidden, '\n')
                    print('Letras: ', len(selected))
                    print('Intentos: ', lifes)
                    user_attemp = input('\nLetra: ')

                    if not (user_attemp in normalize(selected)):
                        lifes -= 1

                    for i in enumerated_selected:
                        if normalize(enumerated_selected.get(i)) == user_attemp:
                            coincidence.append(i)

                    if lifes == 0:
                        print('\nLa palabra era: ', selected)
                        sys.exit()

                    for i in coincidence:
                        hidden = hidden[:i - 1] + enumerated_selected.get(i) + hidden[i:]
                clear()
                print('''
        ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
        ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
        ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
        ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
        ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
    
    
    
                                    ''')
                print(hidden, '\n')
                print('Intentos: ', lifes)
                print('Lo lograste!')
                sys.exit()
    except KeyboardInterrupt:
        print('\n\nSee you later!')
        sys.exit()


def run():
    # Welcome message
    print('''
    
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
    ''')
    print('By Alejandro Parrado Di Domenico')
    print(
        '_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶_̶\n')

    print('''Instructions:
    
        1. To start the game press Enter.
        2. To exit the game press Esc.
        3. Enjoy!
    ''')
    game()


if __name__ == '__main__':
    run()
