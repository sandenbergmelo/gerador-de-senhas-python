from random import shuffle, choice
from string import ascii_letters, digits
import PySimpleGUI as sg

punctuation  = '@#.,*%+=-!?&'

# Funções
def gerar_senha(letras=8, numeros=4, caracteres_especiais=2):
	generated = ''
	generated += gerar_caracteres(letras, ascii_letters)
	generated += gerar_caracteres(numeros, digits)
	generated += gerar_caracteres(caracteres_especiais, punctuation)
	return embaralhar_caracteres(generated)

def gerar_caracteres(length, chars):
	generated = ''
	for _ in range(length):
		generated += choice(chars)
	return generated

def embaralhar_caracteres(chars):
	chars = list(chars)
	shuffle(chars)
	return ''.join(chars)

def salvar_senha(senha):
	with open('senhas.txt', 'a') as senhas:
		senhas.write(f'{senha}\n')

def limpar_saida(obj):
	janela.FindElement(obj).Update('')

# Layout
layout = [
	[sg.Text('Quantidade de letras: '),
	sg.Combo(values=list(range(17)), default_value=8, key='letras')],
	[sg.Text('Quantidade de números: '),
	sg.Combo(values=list(range(17)), default_value=4, key='numeros')],
	[sg.Text('Quantidade de caracteres especiais: '),
	sg.Combo(values=list(range(17)), default_value=2, key='chars')],
	[sg.Checkbox('Salvar senha', key='salvar')],
	[sg.Button('Gerar Senha', key='gerar'),
	sg.Button('Limpar', key='limpar'),
	sg.Button('Sair', key='sair')],
	[sg.Output(key='resultado', size=(36, 10), font='Consolas')]
]

# Janela
janela = sg.Window('Gerador de senhas', layout=layout)

# Eventos
while True:
	evento, valores = janela.read()
	if evento == sg.WIN_CLOSED or evento == 'sair':
		break
	if evento == 'limpar':
		limpar_saida('resultado')
	if evento == 'gerar':
		senha = gerar_senha(valores['letras'], valores['numeros'], valores['chars'])
		print(senha)
		if valores['salvar']:
			salvar_senha(senha)
			sg.popup('Senha salva em senhas.txt', title='Salvar senha')
