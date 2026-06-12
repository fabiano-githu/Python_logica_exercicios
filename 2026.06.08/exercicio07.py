'''
Questão 7 – Acesso ao sistema (operador AND)
Crie as variáveis:

 - usuario = "admin"
 - senha = "1234"

Utilize o operador `and` para verificar se:

 - usuário é "admin"
 - senha é "1234"

 - Se ambas as condições forem verdadeiras: "Acesso permitido."
 - Caso contrário: "Acesso negado."
'''

# Crie as variáveis:
usuario = "admin"
senha = "1234"

# Utilize o operador `and` para verificar se:
if usuario == "admin" and senha == "1234":
    print("\n\nAcesso permitido.\n\n")
else:
    print ("\n\nAcesso negado.\n\n")