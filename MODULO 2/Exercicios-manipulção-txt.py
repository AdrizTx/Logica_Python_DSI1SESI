# ======================================================
# MÓDULO 1 — CRIAÇÃO DE STRINGS
# ======================================================

# EX1
# Crie uma variável chamada texto1 com o valor "Logica"
# usando aspas duplas e exiba o conteúdo.
print("\n\n")
print("======== EXERCICIO 1 ========")
print("\n\n")

texto1 = "Logica"
print(texto1)

# EX2
# Crie uma variável chamada texto2 com o valor
# 'Eu sou top em python' usando aspas simples e exiba.

print("\n\n")
print("======== EXERCICIO 2 ========")
print("\n\n")

texto2 = 'Eu sou top em python'
print(texto2)

# EX3
# Crie uma string usando aspas simples que contenha
# aspas duplas dentro do texto: copa "padrão fifa".

print("\n\n")
print("======== EXERCICIO 3 ========")
print("\n\n")

string1 = 'copa "padrao fifa".'
print(string1)

# EX4
# Crie uma string usando aspas duplas que contenha
# aspas simples dentro do texto: copa 'padrão fifa'.

print("\n\n")
print("======== EXERCICIO 4 ========")
print("\n\n")

string2 = "copa 'padrao fifa'."
print(string2)

# ======================================================
# MÓDULO 2 — STRINGS MULTILINHA
# ======================================================

# EX5
# Crie uma string multilinha representando um menu
# com as opções:
# -A  Exibe ajuda
# -E  Execute agora, quero jogar!

print("\n\n")
print("======== EXERCICIO 5 ========")
print("\n\n")

menu = """\
menu[OPÇÕES]
-A Exibe ajuda
-E Execute agora, quero jogar!
"""
print(menu)

# EX6
# Crie uma string multilinha contendo um poema
# com três versos.

print("\n\n")
print("======== EXERCICIO 6 ========")
print("\n\n")

poema = """\
No silêncio da noite, a lua vem cantar,
Folhas dançam leves ao vento do mar,
E o coração desperta só para sonhar.
"""
print(poema)

# ======================================================
# MÓDULO 3 — CONCATENAÇÃO AUTOMÁTICA
# ======================================================

# EX7
# Use concatenação automática de literais para unir
# as palavras "Volei" e "top!".

print("\n\n")
print("======== EXERCICIO 7 ========")
print("\n\n")

cadl = ("Volei " "top!")
print(cadl)

#CADL = concatenação automática de literais

# EX8
# Concatene automaticamente as strings
# "Python", " é ", "demais" em uma única string.

print("\n\n")
print("======== EXERCICIO 8 ========")
print("\n\n")

concatenação = ("Python " "é " "demais")
print(concatenação)

# ======================================================
# MÓDULO 4 — STRINGS COMO SEQUÊNCIAS
# ======================================================

# EX9
# Atribua "software" a uma variável chamada st
# e mostre a primeira letra da string.

print("\n\n")
print("======== EXERCICIO 9 ========")
print("\n\n")

st = "software"
print("Primeira Letra: ", st[0])

# EX10
# Usando a mesma string "software",
# mostre a última letra.

print("\n\n")
print("======== EXERCICIO 10 ========")
print("\n\n")

print("Ultima letra: ", st[-1])

# EX11
# Mostre os caracteres do índice 1 até o índice 4
# (sem incluir o 4) da string "software ".

print("\n\n")
print("======== EXERCICIO 11 ========")
print("\n\n")

print("Trecho 1 até 4: ", st[1:4])

# EX12
# Mostre os caracteres do início até o índice 3
# da string "software".

print("\n\n")
print("======== EXERCICIO 12 ========")
print("\n\n")

print("Trecho inicio ao 3: ", st[:3])

# EX13
# Mostre os caracteres do índice 2 até o final
# da string "software".

print("\n\n")
print("======== EXERCICIO 13 ========")
print("\n\n")

print("Trecho 2 adiante: ", st[2:])

# EX14
# Mostre o tamanho da string "software"
# usando a função len().

print("\n\n")
print("======== EXERCICIO 14 ========")
print("\n\n")

print("Tamanho: ", len(st))

# EX15
# Acesse o último caractere de "software"
# usando índice positivo (sem usar -1).

print("\n\n")
print("======== EXERCICIO 15 ========")
print("\n\n")

print("Ultimo Caractere(sem usar -1): ", st[7])

# EX16
# Mostre os caracteres que estão nos índices pares
# da string "software"
# .

print("\n\n")
print("======== EXERCICIO 16 ========")
print("\n\n")

print("indices Pares: ", st[::2])

# EX17
# Inverta a string "software".

print("\n\n")
print("======== EXERCICIO 17 ========")
print("\n\n")

print("string invertida: ", st[::-1])