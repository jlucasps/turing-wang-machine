# This Python file uses the following encoding: utf-8#
# ##############################################################################
# Trabalho de Teoria da Computaçao - COM 167
# Simulador de Máquinas de Wang
# Hudson Flávio, João Lucas, Renan Martins
# Arquivo wang.py
# -> Este arquivo implementa a classe Wang para simulações da máquina.
# ###############################################################################

class Wang:
	def __init__(self, program, tape):
		self.program = program
		self.tape = tape

	def executa(self, instAtual, square):
		"""Método que simula a execução de um máquina de Wang (B-Machine). 
		   instAtual indica a instrução que está sendo executada no momento.
		   square indica o square que está sendo scaneado no momento.
	    """

		passo = raw_input('\n>>>')

		print '\nInstrução atual: ', instAtual
		print 'Square: ', square
		print 'Configuração da máquina: ',
		print '(2^', self.godel(), ')*',
		print '(3^', self.tapeConfAnt(square), ')*',
		print '(5^', self.tapeConfPosAtual(square), ')*',
		print '(7^', self.tapeConfPost(square+1), ')*',
		print '(11^', instAtual, ')'

		if instAtual <= (len(self.program)):
			inst = self.program[instAtual]

			#Se instrução for seta à direita, move para o square à direita
			#e passa para próxima instrução do programa.
			if inst == '->':
				square += 1
				instAtual += 1

			#Se instrução for seta à esquerda, move para o square à esquerda
			#e passa para próxima instrução do programa.
			elif inst == '<-':
				square -= 1		
				instAtual += 1
				
			#Se instrução for *, marca a posição corrente na fita
			#e passa para próxima instrução do programa.
			elif inst == '*':
				self.tape[square] = '*'			
				instAtual += 1
			else:
				
				#Se instrução for do tipo Cn, move para a instrução n se o square corrente está marcado,
				#caso contrário, passa para próxima instrução do programa.
				if(self.tape[square] == '*'):
					prox = inst.replace('C','')
					instAtual = int(prox)
				else:
					instAtual+= 1
					
			self.executa(instAtual, square)
		else:
			print '\nEXECUCAO TERMINOU'
			return None

	def isPrime(self, n):
		"""Método para verificar se um número n é primo."""

		for x in range(2, n - 1):
			if n % x == 0:
				return False

		return True

	def nextPrime(self, n):
		"""Método para retornar o primeiro primo após n"""

		n += 1

		while not(self.isPrime(n)):
			n += 1 

		return n

	def godel(self):
		"""Método para codificar uma sequencia utilizando a função de godel.
		   Codifica o programa e retorna o número correspondente"""

		prime = 2
		godel = 1L

		#loop para gerar o número de godel do programa 
		#(primo_n) ^ (num_instrX) * (primo_n+1) ^ (num_instrX+1)
		for x in range(1, len(self.program)+1):
			inst = self.program[x]
			
			if inst == '->':
				godel *= pow(prime, 1)
			elif inst == '<-':
				godel *= pow(prime, 2)
			elif inst == '*':
				godel *= pow(prime, 3)
			else:
				prox = int(inst.replace('C',''))
				godel *= pow(prime,prox+3)
			
			prime = self.nextPrime(prime)

		return godel
	
	def tapeConfAnt(self, lim):
		"""Método para retornar o valor que representa a parte de fita que está
		   antes do simbolo atualmente scaneado.
		   Este valor é calculado conforme especificado por Hao Wang, em seu artigo de 1957"""

		if (lim < 0):
			lim = 0

		part = self.tape[0:lim]
		part.reverse()
		value = 0

		for x in part:
			value *= 10

			if x == '*':
				value += 1
			
		return value
	
	def tapeConfPost(self, lim):
		"""Método para retornar o valor que representa a parte de fita que
		   está após o simbolo atualmente scaneado.
		   Este valor é calculado conforme especificado por Hao Wang, em seu artigo de 1957"""

		part = self.tape[lim:len(self.tape)]
		part.reverse()
		value = 0

		for x in part:
			value *= 10

			if x == '*':
				value += 1
			
		return value
	
	def tapeConfPosAtual(self, pos):
		"""Método usado para retornar 1 se a posição atualemente scaneada é marcada,
		   caso contrário, retorna 0."""

		if self.tape[pos] == '*':
			return 1

		return 0
