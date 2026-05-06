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