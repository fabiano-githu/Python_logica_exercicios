'''
Questão 1 – Cadastro simples
Crie um programa que:

 - Armazene o nome de uma pessoa em uma variável.
 - Armazene a idade em outra variável.
 - Exiba a seguinte mensagem:
    "Olá João, você tem 20 anos."

(Os valores devem vir das variáveis.)
'''
# Armazene o nome de uma pessoa em uma variável.
name = "Joca"

# Armazene a idade em outra variável.
age = 65

# Exiba a seguinte mensagem: (usando interpolação)
print(f"Olá {name}, você tem {age} anos.")

# debug
# print("-----", type(age), "-----")

# Exiba a seguinte mensagem: (usando concatenação)
print("Olá " + name + ", você tem " + str(age) + " anos.")