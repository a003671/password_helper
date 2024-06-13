from secrets import choice
import json


def create(length: int) -> str:
    '''
    The function takes as input the number of words used to create the password and returns the password.
    '''
    try:
        with open('bdword.json', encoding='utf-8') as file:
            data = list(json.load(file).keys())
        password = [choice(data) for _ in range(length)]
        return ' '.join(password)
    except FileNotFoundError:
        return 'Not Found File'

if __name__ == '__main__':
    create()