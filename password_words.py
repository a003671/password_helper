'''Модуль предназначен для создания рандомного пароля из слов'''



from secrets import choice
import json


class WordPassword:
    def create(self) -> str:
        '''Функция ни чего не принимает, открывает предустановленную БД откуда берет рандомно слова, и возвращает пароль состоящий из 4 слов.'''
        try:
            with open('bdword.json', encoding='utf-8') as file:
                data = list(json.load(file).keys())
            password = [choice(data) for _ in range(4)]
            return ' '.join(password)
        except FileNotFoundError:
            return 'Not Found File'