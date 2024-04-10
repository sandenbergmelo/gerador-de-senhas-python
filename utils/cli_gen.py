from pathlib import Path
from secrets import SystemRandom
from string import ascii_letters, digits

random = SystemRandom()
chars = '@#.,*%+=-!?&'


def generate_password(num_letters: int = 8, num_numbers: int = 4, num_chars: int = 2) -> str:
    generated = generate_chars(num_letters, ascii_letters) + \
        generate_chars(num_numbers, digits) + \
        generate_chars(num_chars, chars)

    password = str(shuffle_chars(generated))
    return password


def generate_chars(length: int, chars: str) -> str:
    return ''.join(random.choice(chars) for _ in range(length))


def shuffle_chars(chars: str) -> str:
    char_list = list(chars)
    random.shuffle(char_list)
    return ''.join(char_list)


def save_password(password: str, file: str = 'senhas.txt') -> None:
    with open(file, 'a') as passwords:
        passwords.write(f'{password}\n')


def main() -> None:
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--letras', '-l', type=int,
                        default=8, help='Quantidade de letras')
    parser.add_argument('--numeros', '-n', type=int,
                        default=4, help='Quantidade de números')
    parser.add_argument('--chars', '-c', type=int, default=2,
                        help='Quantidade de caracteres especiais')
    parser.add_argument('--salvar', '-s', type=bool, nargs='?',
                        default=False, help='Salvar senha em arquivo txt')
    parser.add_argument('--output', '-o', type=str, nargs='?', default='',
                        help='Arquivo de saída (Padrão "senhas.txt")',)

    args = parser.parse_args()

    password = generate_password(args.letras, args.numeros, args.chars)

    print(password)

    if args.salvar:
        path = Path(args.output)
        if path.is_dir():
            path /= 'senhas.txt'

        save_password(password, str(path))
        print(f'Senha salva em {path}')
        return

    print('Senha não salva.')


if __name__ == '__main__':
    main()
