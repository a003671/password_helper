import argparse
from dataclasses import dataclass, field


from password_letters import create as PL
from password_words import create as PW



@dataclass
class Password:
    '''
    The class stores the created data.
    '''
    passwords: str = field(default_factory=list, init=False)


def _create_password(func, length, counter) -> None:
    '''
    The function takes the length and quantity of the password, displays the password to the console.
    '''
    password.passwords = [(func(length)) for _ in range(counter)]
    print(*[F'{num}. -> {password}' for num, password in enumerate(password.passwords, 1)], sep='\n')


def letter(args) -> None:
    '''
    The input function accepts data received from the command line and runs the function to create a password_ letter.
    '''
    _create_password(func=PL, length=args.length, counter=args.counter)


def word(args) -> None:
    '''
    The input function accepts data received from the command line and runs the function to create a password_word.
    '''
    _create_password(func=PW, length=4, counter=args.counter)


parser = argparse.ArgumentParser(prog='password helper')
subparser = parser.add_subparsers(title='subcommands', help='password creation options')
letter_parser = subparser.add_parser('letter', help='create letter password')
letter_parser.add_argument('-l', '--length', type=int, choices=range(4, 21), default=8, help='length create password', dest='length', metavar='from 4 to 20')
letter_parser.add_argument('-c', '--counter', type=int, choices=range(1, 1001), default=1, help='number of generated passwords', dest='counter', metavar='from 1 to 1000')
letter_parser.set_defaults(func=letter)

word_parser = subparser.add_parser('word', help='create word password')
word_parser.add_argument('-c', '--counter', type=int, choices=range(1, 101), default=1, help='number of generated passwords', dest='counter', metavar='from 1 to 100')
word_parser.set_defaults(func=word)



if __name__ == '__main__':
    password = Password()
    args = parser.parse_args()
    if vars(args):
        args.func(args)
    else:
        parser.print_help()