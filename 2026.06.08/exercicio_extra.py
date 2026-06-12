'''Crie uma lista contendo nomes de alunos:

["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

Verifique se um determinado nome está na lista.

Se estiver:

 - Aluno matriculado.

 Caso contrário:

 - Aluno não encontrado.

Objetivo: utilizar lista, variável, operador in e estrutura if...else em uma única solução.
'''

# Crie uma lista contendo nomes de alunos:
alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

# Verifique se um determinado nome está na lista.
nome_procurado = "carlos"
if nome_procurado.lower() in [nome.lower() for nome in alunos]:
    print(f"{nome_procurado} está matriculado.")
else:
    print("Aluno não encontrado.")