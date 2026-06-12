'''
Questão 3 – Lista de frutas
Crie uma lista contendo pelo menos 5 frutas.

Depois:

 - Exiba a lista completa.
 - Exiba apenas a primeira fruta.
 - Exiba apenas a última fruta.
 - Adicione algumas frutas e exiba a última, independente da quantidade.
'''

# Crie uma lista contendo pelo menos 5 frutas.
fruits = ["banana", "laranja", "kiwi",
          "abacate", "tangerina", "morango", "pêra"]

# Exiba a lista completa.
print(fruits)

# Exiba apenas a primeira fruta.
print(fruits[0])

# Exiba apenas a última fruta.
print(fruits[4])  

# Adicione algumas frutas 
fruits.append("uva")
fruits.append("melancia")
fruits.append("abacaxi")

# e exiba a última, independente da quantidade.
print(fruits[len(fruits) - 1])
# outra forma de obter o último elemento da lista é usando índice negativo
print(fruits[-1])  