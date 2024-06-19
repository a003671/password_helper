'''Модуль предназначен для создания рандомного пароля из символов и букв в разных регистрах.'''



from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits, ascii_letters
from typing import Any, Literal, LiteralString


class LetterPassword:
    '''
    класс по созданию буквосимольного пароля.
    длина пароля от 4 до 10 символов;
    
    '''
    __slots__: tuple[Literal['__length']] = ('__length',)
    
    MIN_length = 4
    MAX_length = 10
    
    def __init__(self, length) -> None:
        self.__length: Any = self.__check(length)

    def __check(self, lenght):
        '''при инициализации проверяет количество символов, при выходе за указаные границы устанавливает минимальное значение.'''
        return lenght if self.MIN_length <= lenght <= self.MAX_length else 4

    def __random_letter(self, string: str) -> str:
        '''Функция принимает строку символов в качестве входных данных и возвращает случайный символ из этой строки в качестве выходных.'''
        return choice(string)


    def create(self) -> LiteralString:
        '''Функция вызывает функцию random_letter, передает строку символов или букв, собирает пароль по указанной длине, возвращает пароль в виде строки.'''

        punctuation = '!#$%&*+-/<=>?@[^~\\'
        counter = self.__length // 4
        password = set()
        
        password.update({self.__random_letter(ascii_lowercase) for _ in range(counter)} | 
                        {self.__random_letter(ascii_uppercase) for _ in range(counter)} | 
                        {self.__random_letter(digits) for _ in range(counter)} | 
                        {self.__random_letter(punctuation) for _ in range(counter)})

        while len(password) < self.__length:
            password.update({self.__random_letter(ascii_letters)})

        return ''.join(password)