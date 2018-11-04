import random
import os

pronombres = []
pronombres.append(['pronombre personal','pronombre acusativo','adjetivo posesivo',
'pronombre posesivo','pronombre reflexivo','pronombre indefinido','pronombre relativo','pronombre reciproco'])
pronombres.append(['I','you','he','she','it','we','you(ustedes)','they'])
pronombres.append(['me','you','him','her','it','us','you','them'])
pronombres.append(['my','your','his','her','its','our','your','their'])
pronombres.append(['mine','yours','his','hers','--','ours','yours','theirs'])
pronombres.append(['myself','yourself','himself','herself','itself','ourselves','yourselves','themselves'])
pronombres.append([['everybody','everyone','everything'],['nobody','no one','nothing'],[['somebody','someone','something'],['anybody','anyone','anything']]])
pronombres.append(['who','which','that','whom','whose'])
pronombres.append(['each other','one another'])

repeticion_lista_pronombres = []
for x in pronombres:
	repeticion_lista_pronombres.append([])
	
def constructor(lista,repeticion_lista,limpia):
	numeros_buscar_lista = [x for x in range(len(lista))]
	
	while True:
		r = random.choice(numeros_buscar_lista)

		if not r in repeticion_lista:
			if limpia == True:
				repeticion_lista.append(r)
			return lista[r]

		if (len(repeticion_lista) == len(lista)) and (limpia == True):
			del repeticion_lista[:]

validacion = ''
i=0
c=0
e=0

pronombre = []
for x in pronombres:
	pronombre.append([])

indice = []
for x in pronombres:
	indice.append([])

modo = input('DIFICIL [d]/ FACIL [Cualquier tecla]: ')

os.system('cls')
for x in range(5):
	aux_p = pronombres[0][x]
	aux_i = pronombres[0][x].find(' ')
	print(aux_p[:aux_i], end = '\t')
print('')
for x in range(5):
	aux_p = pronombres[0][x]
	aux_i = pronombres[0][x].find(' ')
	print(aux_p[aux_i+1:], end = '\t')
print('')

for x in range(8):
	for y in range(1,6):
		if len(pronombres[y][x]) <= 7:
			print(pronombres[y][x], end = '\t\t')
		else:
			print(pronombres[y][x], end = '\t')
	print('')
input('Iniciar [enter]: ')

while validacion == '':
	os.system('cls')
	if modo == 'd':
		pronombre[0] = constructor(pronombres[0][:5],repeticion_lista_pronombres[0],True)
		indice[0] = pronombres[0].index(pronombre[0])
		pronombre[1] = constructor(pronombres[indice[0] + 1],repeticion_lista_pronombres[indice[0] + 1],True)
		indice[1] = pronombres[indice[0] + 1].index(pronombre[1])

		print('--{}---'.format(pronombres[1][indice[1]]))

		pro = pronombre[1]
		insercion = input('{}: '.format(pronombre[0]))
		print('{}: {}'.format(pronombre[0],pronombre[1]))
		if pro == insercion:
			print('BIEN')
			c = c + 1
		else:
			print('MAL')
			e = e + 1
	else:
		os.system('cls')
		if not i == 0:
			for x in range(5):
				aux_p = pronombres[0][x]
				aux_i = pronombres[0][x].find(' ')
				print(aux_p[:aux_i], end = '\t')
			print('')
			for x in range(5):
				aux_p = pronombres[0][x]
				aux_i = pronombres[0][x].find(' ')
				print(aux_p[aux_i+1:], end = '\t')
			print('')

			for x in range(8):
				for y in range(1,6):
					if len(pronombres[y][x]) <= 7:
						print(pronombres[y][x], end = '\t\t')
					else:
						print(pronombres[y][x], end = '\t')
				print('')
			input('Iniciar [enter]: ')
		os.system('cls')

		pronombre = constructor(pronombres[1],repeticion_lista_pronombres[0],True)
		indice = pronombres[1].index(pronombre)
		print('{}: {}'.format(pronombres[0][0], pronombre))

		print('--insertar--')
		for x in range(1,5):

			pro = pronombres[x+1][indice]

			insercion = input('{}: '.format(pronombres[0][x]))

			print('{}: {}'.format(pronombres[0][x], pro))

			if pro == insercion:
				print('BIEN')
				c = c + 1
			else:
				print('MAL')
				e = e + 1

	validacion = input('Continuar [enter]/ Salir [Cualquier tecla]: ')
	i = i + 1

print('intentos')
print(i)
print('correctos')
print(c)
print('incorrectos')
print(e)

input('FIN')