# AULA COMPLETA - STRINGS EM PYTHON

# - Criação de strings
# - Strings multilinha
# - Indices e slices
# - Operações com strings
# - Imutabilidade
# - Métodos uteis
# - Formatação de texto
# - Unicode e bytes

#-------------------------------------------------------------
# 1) CRIAÇÃO DE STRINGS
#-------------------------------------------------------------
#String são textos em python.
#Podem ser criadas usando aspas ou duplas

texto1 = "Python"
texto2 = 'curso de Python'
texto3 = "Copa 'padrão FIFA'"
texto4 = 'Copa "padrão FIFA"'

print(texto1, texto2, texto3, texto4)

# Python permite misturas aspas silples e duplas, dentro das strings sem precisar escapar caracteres

#------------------------------------------------------------
# 2) STRINGS MULTILINHA
#------------------------------------------------------------
# Usando três aspas(""" ou ''') para criar textos que ocupam varias linhas.

menu = """\
uso: programa[OPÇÕES]
-h Exibe ajuda
-U url do dataset
"""

print(menu)
# Esse formato é muito usado para:
# - menus
# - documentação
# - textos longos

#------------------------------------------------------------
# 3) CONCATENÇÃO AUTOMATICA
#------------------------------------------------------------
#Quando duas strings aparecem lado a lado, o Python junta automaticamente

texto = ("Copa " "2026 " "Neymar é show mesmo?" " SIM")
print(texto)

#------------------------------------------------------------
# 4) STRINGS COMO SEQUÊNCIAS
#------------------------------------------------------------
#Uma strings funciona como sequencia de caracteres, cada caractere possui um indice

st = "Maracana"
print("Primeira Letra:", st[0])

# só exibir a letra: m

print("ultima letra:", st[-1])

print("Trecho 1:4:", st[1:4])

print("Do inicio até 3:", st[:3])

print("Do 2 até o fim:", st[2:])

print("Tamanho:", len(st))


