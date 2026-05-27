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

#------------------------------------------------------------
# 5) OPERAÇÕES COM STRINGS
#------------------------------------------------------------
#Python permite várias operções com strings

print("M" in st)
# Significa que a letra "m" existe dentro da string

print("x" not in st)
# Significa que "x" não existe na string

print("M" * 20)
#Multi´licação repete na string

print("m" + "aracana" + texto1)
# Operador + concatena strings

#------------------------------------------------------------
# 6) STRIGS SÃO IMUTÁVEIS
#------------------------------------------------------------
# Strings não podem ser alteradas diretamente!
#Isso significa que o  conteudo original não muda.
#O que acontece é a criação de uma nova string.

textoPY = "python 3"

#metodo replace cria uma nova string
textoPY = textoPY.replace("3", "2")

print(textoPY)

#------------------------------------------------------------
# 7) METODOS IMPORTANTES
#------------------------------------------------------------
# Strings possuem vários métodos úteis.

cidade = "maracana"
#Coloca a primeira letra em maiúscula.
print(cidade.capitalize())

#Conta quantas vees "a" aparece
print(cidade.count("a"))

#Verificar se começa com "m"
print(cidade.startswith("m"))

#Verificar se terminha com "m"
print(cidade.endswith("z"))

frase = "copa de 2002"
print(frase.split(" "))

#------------------------------------------------------------
# 8) FORMATAÇÃO DE STRINGS
#------------------------------------------------------------