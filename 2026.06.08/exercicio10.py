'''
Questão 10 – Sistema de acesso completo
Crie as variáveis:

 - idade = 20
 - possui_convite = True

Uma pessoa poderá entrar em um evento somente se:

 - tiver 18 anos ou mais e possuir convite.

Utilize o operador `and` dentro de uma estrutura `if`.

Saída esperada:

"Entrada autorizada."

ou

"Entrada negada."
'''

# Crie as variáveis:
idade = 30
possui_convite = True

# Utilize o operador `and` dentro de uma estrutura `if`.
if idade >= 18 and possui_convite:  
    print("Entrada autorizada.")
else:
    print("Entrada negada.")