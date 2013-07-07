# This Python file uses the following encoding: utf-8#
# ##############################################################################
# Trabalho de Teoria da Computaçao - COM 167
# Simulador de Máquinas de Wang
# Hudson Flávio, João Lucas, Renan Martins
# Arquivo wang.py
# -> Este arquivo implementa a classe Main para interações com o usuário e menus.
# ###############################################################################

from wang import *

class Main:
	def getProgram(self, programa):
		"""Método para carregar o programa a partir do arquivo.
		O parâmetro 'programa' indica o caminho do arquivo"""

		f = open(programa,'r+')
		linhas = f.readlines()

		program = {}

		for x in range(len(linhas)):
			linha = (linhas[x]).replace('\n','')
			program[int(linha.split('.')[0])] = linha.split('.')[1]

		return program


	def getTape(self, arq):
		"""Método para carregar a fita de entrada a partir do arquivo.
		O parâmetro 'arq' indica o caminho do arquivo"""
		
	    #Abre o arquivo para leitura e escrita
		f = open(arq, 'r+')

	    #pega cada linha e coloca em um item da lista, o '\n' vem junto
		linhas = f.readlines()

	    #essa parte eh usada para retirar os '\n'
		elementos = []
		for inst in linhas:
			elementos = elementos + [inst.replace('\n','')]

		f.close()

		return elementos
		
main = Main()
print 45*str('--')
info = """Este programa simula uma máquina de Wang (B-Machine).\nInforme o caminho do programa, em seguida o caminho da fita de entrada para o programa.
Após entrar com os dados, o programa iniciará uma execução passo-a-passo."""
print info
print 45*str('--')

program = raw_input('Entre com caminho do arquivo do programa:\n>>>')
program = main.getProgram(program)

tape = raw_input('Entre com caminho do arquivo da fita:\n>>>')
tape = main.getTape(tape)

wang = Wang(program, tape)
print '\nPrograma: ', program
print 'Numero de godel deste programa: ', wang.godel()
print 'Fita: ', tape

wang.executa(1, 0)



