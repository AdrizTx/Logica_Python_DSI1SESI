#DESAFIOS PYTHON - PROF FALABELLA

# EX1
# Um aluno tem 10 anos. Armazene essa idade em uma variável
# e exiba seu tipo.

idade = 10
print("Idade: ", idade)
print("Tipo: ", type(idade))

# EX2
# A temperatura medida é 23.5°C.
# Armazene esse valor e mostre seu tipo.

print("=====================================")
temperatura = 23.5
print("Temperatura: ", temperatura)
print("Tipo: ", type(temperatura))

# EX3
# Crie um número complexo representando uma impedância elétrica
# de 5 + 8j e mostre sua parte real.

print("=====================================")
numero_complexo = 5 + 8j
print("Parte Real: ", numero_complexo.real)

# EX4
# Mostre a parte imaginária do número complexo
# criado no exercício anterior.

print("=====================================")
numero_complexo = 5 + 8j
print("Parte Imaginaria: ", numero_complexo.imag)
# EX5
# Declare uma variável chamada "populacao"
# com o valor 8_000_000_000 (8 bilhões)
# e mostre seu tipo.

print("=====================================")
populacao = 800000000
print("populacao: ", populacao)
print("Tipo: ", type(populacao))

# EX6
# Verifique se o número 7 é do tipo int
# usando a função type().

print("=====================================")
num = 7
print("numero: ", num)
print("Tipo: ", type(num))

# EX7
# Crie uma variável chamada "aprovado"
# com o valor booleano True e mostre seu tipo.

print("=====================================")
aprovado = True
print("Aprovado: ", aprovado)
print("Tipo: ", type(aprovado))

# EX8
# Some True e False e mostre o resultado
# e também o tipo do resultado.

print("=====================================")
resultado = True + False
print("Resultado: ", resultado)
print("Tipo: ", type(resultado))

# EX9
# Pesquise e mostre qual é o valor máximo
# que um número inteiro pode ter em Python.

import sys

print(sys.maxsize)

# EX10
# Mostre a representação em binário
# do número 10 usando uma função do Python.

print(bin(10))
