from pathlib import Path
from secrets import SystemRandom
from string import ascii_letters, digits

random = SystemRandom()
symbols = '@#.,*%+=-!?&'


def generate_password(letras=8, numeros=4, caracteres_especiais=2):
    generated = ''
    generated += generate_chars(letras, ascii_letters)
    generated += generate_chars(numeros, digits)
    generated += generate_chars(caracteres_especiais, symbols)

    password = shuffle_chars(generated)
    return password


def generate_chars(length, chars):
    generated = ''
    for _ in range(length):
        generated += random.choice(chars)
    return generated


def shuffle_chars(chars):
    chars = list(chars)
    random.shuffle(chars)
    return ''.join(chars)


def save_password(senha, arquivo='senhas.txt'):
    with open(arquivo, 'a') as passwords:
        passwords.write(f'{senha}\n')


if __name__ == '__main__':
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

    if args.salvar != False:
        path = ''
        if args.output != '':
            path = args.output
        if Path(path).is_dir():
            path = Path(path) / 'senhas.txt'

        if path != '' and path != None:
            save_password(password, path)
            print(f'Senha salva em {path}')
        else:
            save_password(password)
            print('Senha salva em senhas.txt')
