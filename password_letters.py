from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits, ascii_letters


def __letter_password(string: str) -> str:
    '''
    The function takes a string of characters as input and returns a random character from the string as output.
    '''
    return choice(string)


def create(counter_symbol: int) -> str:
    '''
    The function takes as input the number of characters used to create the password and returns the password.
    '''
    punctuation = '!#$%&*+-/<=>?@[^~\\'
    counter = counter_symbol // 4
    password = set()
    
    password.update({__letter_password(ascii_lowercase) for _ in range(counter)} | 
    {__letter_password(ascii_uppercase) for _ in range(counter)} |
    {__letter_password(digits) for _ in range(counter)} |
    {__letter_password(punctuation) for _ in range(counter)})

    while len(password) < counter_symbol:
        password.update({__letter_password(ascii_letters)})

    return ''.join(password)


if __name__ == '__main__':
    create()