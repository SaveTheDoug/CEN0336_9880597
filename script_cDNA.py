#!/usr/bin/env python3
import sys

DNA = sys.argv[1] # captura a string do dna
n1 = sys.argv[2]  # captura o valores de n1
n2 = sys.argv[3]  # captura o valores de n2
n3 = sys.argv[4]  # captura o valores de n3
n4 = sys.argv[5]  # captura o valores de n4

n1 = int(n1) # converte os n1 para tipo int
n2 = int(n2) # converte os n2 para tipo int
n3 = int(n3) # converte os n3 para tipo int
n4 = int(n4) # converte os n4 para tipo int

CDS1 = DNA[n1:n2] # delimita CDS1 e CDS2
print(CDS1)
CDS2 = DNA[n3:n4]
print(CDS2)

if CDS1[0:3] == 'ATG': # averigua se CDS1 começa com ATG
	if CDS2[-3:] == 'TAA' or CDS2[-3:] == 'TAG' or CDS2[-3:] == 'TGA': # verifica se CDS2 se encerra com algum dos codon desejados
                print(CDS1 + CDS2)
	else:
                print('CDS2 não termina com um codon de fechamento')
else:
        print('CDS1 não inicia com um codon de inicio')