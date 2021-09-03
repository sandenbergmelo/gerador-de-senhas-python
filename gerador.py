import PySimpleGUI as sg
from gerador_cli import gerar_senha, salvar_senha
punctuation  = '@#.,*%+=-!?&'

# Funções
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
		letras, numeros, chars = valores['letras'], valores['numeros'], valores['chars']

		if letras != 0 or numeros != 0 or chars != 0:
			senha = gerar_senha(letras, numeros, chars)
			print(senha)

			if valores['salvar']:
				sg.popup(salvar_senha(senha), title='Salvar senha')
		else:
			sg.popup('Impossível gerar senha vazia!', title='Erro!')
