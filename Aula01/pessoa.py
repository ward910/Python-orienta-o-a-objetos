from datetime import datetime


class Pessoa:
	ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

	def __init__(self, nome, idade, comendo=False, falando=False):
		self.nome = nome
		self.idade = idade
		self.comendo = comendo
		self.falando = falando 

	def falar(self, assunto):
		self.assunto = assunto
		if self.comendo:
			print(f'{self.nome} não pode comer falando')
			return

		if self.falando:
			print(f'{self.nome} já está falando sobre {self.assunto}')
		
		print(f'{self.nome} você está falando sobre {self.assunto}')
		self.falando = True

	def parar_de_falar(self):
		if not self.falando:
			print(f'{self.nome} não está falando')
		else:
			print(f'{self.nome} parou de falar sobre {self.assunto}')
			self.falando = False

	def comer(self, alimento):
		if self.comendo:
			print(f'{self.nome} já está comendo')
		else:
			print(f'{self.nome} está comendo {alimento}')
			self.comendo = True

	def parar_de_comer(self):
		if not self.comendo:
			print(f'{self.nome} não está comendo')
		else:
			print(f'{self.nome} parou de comer')
			self.comendo = False

	def get_ano_nascimento(self):
		return self.ano_atual - self.idade
