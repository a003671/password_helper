'''CLI to help create passwords.
alphabetic passwords;
verbal passwords'''


import argparse
from dataclasses import dataclass, field


from password_letters import LetterPassword
from password_words import WordPassword



@dataclass
class Password:
    '''The class stores the created data.'''
    passwords: str = field(default_factory=list, init=False)

MIN_quantity = 1
MAX_quantity = 1000


def __check(quantity: int) -> int:
    '''Checks the validity of password creation restrictions'''
    if quantity < MIN_quantity:
        return MIN_quantity
    if quantity > MAX_quantity:
        return MAX_quantity
    return quantity


def _create_password(func, quantity) -> None:
    '''
    The function takes the length and quantity of the password, displays the password to the console.
    '''
    password.passwords = [(func.create()) for _ in range(quantity)]
    print(*[F'{num}. -> {password}' for num, password in enumerate(password.passwords, 1)], sep='\n')


def letter(args) -> None:
    '''
    The input function accepts data received from the command line and runs the function to create a password_ letter.
    '''
    quantity = __check(args.quantity)
    PL = LetterPassword(length=args.length)
    _create_password(func=PL, quantity=quantity)


def word(args) -> None:
    '''
    The input function accepts data received from the command line and runs the function to create a password_word.
    '''
    quantity = __check(args.quantity)
    PW = WordPassword()
    _create_password(func=PW, quantity=quantity)


parser = argparse.ArgumentParser(prog='password helper')
subparser = parser.add_subparsers(title='subcommands', help='password creation options')
letter_parser = subparser.add_parser('letter', help='create letter password')
letter_parser.add_argument('-l', '--length', type=int, default=8, help='length create password', dest='length', metavar='from 4 to 10')
letter_parser.add_argument('-q', '--quantity', type=int, default=1, help='number of generated passwords', dest='quantity', metavar='from 1 to 1000')
letter_parser.set_defaults(func=letter)

word_parser = subparser.add_parser('word', help='create word password')
word_parser.add_argument('-q', '--quantity', type=int, default=1, help='number of generated passwords', dest='quantity', metavar='from 1 to 1000')
word_parser.set_defaults(func=word)



if __name__ == '__main__':
    password = Password()
    args = parser.parse_args()
    if vars(args):
        args.func(args)
    else:
        parser.print_help()