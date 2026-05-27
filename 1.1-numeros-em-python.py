# AULA COMPLETA: NUMEROS EM PYTHON

'''
    VAMOS APRENDER:
    1- TIPOS NUMERICOS
    2- CONVERSÕES DE TIPOS
    3- HIERARQUIA NUMERICA
    4- OPERAÇÃO MATEMATICAS
    5- COERÇÃO DE TIPOS
    6- VERIFICAÇÃO DE TIPOS
    7- ENTRADA DE DADOS
'''
###################################################################
# PASSO 01 - TIPOS NUMERICOS
###################################################################

# INT - > NUMEROS INTEIROS
# FLOAT - > NUMEROS COM CASAS DECIMAIS
# COMPLEX - > NUMEROS COMPLEXOS (USADO NA MATEMATICA/ENGENHARIA)

print ("======== TIPOS NUMERICOS ========")

# EXEMPLO 01 - NUMERO INTEIRO

# CRIAMOS A VARIAMVEL CHAMADA NUMERO_INTERIO
numero_inteiro = 10

# MOSTRAMOS O VALOR
print("valor: ", numero_inteiro)

# Type() MOSTRA QUAL O TIPO DA VARIAVEL
print("tipo: ", type(numero_inteiro))

print("---------------------------------")

#EXEMPLO 02 - NUMERO DECIMAL

# FLOAT É O NUMERO COM PONTO DECIMAL
numero_decimal = 3.14

# 
print("valor: ", numero_decimal)

print("tipo: ", type(numero_decimal))

print("---------------------------------")
# EXEMPLO 03 - NUMEROS COMPLEXOS

# UM NUMERO COMPLEXO POSSUI DUAS PARTES:
# PARTE REAL (NUMERO NORMAL)
# PARTE IMAGINARIA (MULTIPICADA POR J)

# ESTRUTURA GERAL:
# NUMERO = A + BJ

# A = PARTE REAL
# B = PARTE IMAGINARIA
# J = PARTE IMAGINARIA

numero_complexo = 2 + 3j

print("valor: ", numero_complexo)
print("tipo: ", type(numero_complexo))

print("---------------------------------")

#EXEMPLO 04 - ACESSANDO CADA PARTE DO NÚMERO

# .REAL RETORNA A PARTE REAL
print ("Parte Real: ", numero_complexo.real)

# .IMAG RETORNA A PARTE IMAGINARIA 
print("Parte Imaginaria: ", numero_complexo.imag)

#APENAS PARA SEPARAR VISUAL VISUALMENTE A SAIDA DO TERMINAL
print("\n\n")

#================================================

## PASSO 02 - CONVERSÃO DE DADOS

#================================================

## EXEMPLOS CLASSICOS
## DADOS VINDOS DO USUARIO SÃO TEXTO(STRING), MUITAS VEZES É NECESSARIO CONVERTER ELES.

print("======== Conversões ========")

valor = int(3.9)

print("int(3.9): ", valor)
print("Tipos: ", type(valor))

#STRING -> INT

valor1 = int("10")
print(type(valor1))

valor2 = int("10")
print('int("10"): ', valor)
print("tipo: ", type(valor2))

#INT --> FLOAT
valor3 = float(10)
print("float(10): ", valor3)
print("tipo: ", type(valor3))

.