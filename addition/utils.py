from sys import argv


def add(n1, n2):
    print('-' * 6, 'Welcome to Add Program', '-' * 6)
    print('#' * 30)

    addition = n1 + n2
    print(f'Addition Result : {addition}')

    print('#' * 30)
    print('-' * 15, 'END', '-' * 15)


if __name__ == '__main__':
    add(3, 5)

