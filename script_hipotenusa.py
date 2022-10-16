#!/usr/bin/env python3
import sys

X = sys.argv[1] # pega o valor de X

Y = sys.argv[2] # pega o valor de Y


if str.isdigit(X) == True: # etapa de confirmção se os caracteres digitados são números 
	if str.isdigit(Y) == True:
		X = int(X) # transforma a variavel X em um valor do tipo int
		Y = int(Y) # transforma a variavel Y em um valor do tipo int
	else:
		print('digite 2 numeros')
else:
	print('digite 2 numeros')


Z = X^2 + Y^2  # cria a variavel Z e armazena o valor do quadrado da hipotenuza nela



print('O valor do quadrado da hipotenusa para o triangulo com lados a=',X,'e b=',Y,' é',Z)