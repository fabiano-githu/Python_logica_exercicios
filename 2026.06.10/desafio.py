'''Desafio. Observe a variável abaixo:

users = [
	{
		"name": "Joca da Silva",
		"email": "jocasilva@email.com",
		"birth": "1980-10-25",
		"password": "Q1w2e3r4t5"
	},
	{
		"name": "Marineuza Siriliano",
		"email": "sirineuza@email.com",
		"birth": "2000-09-14",
		"password": "A1s2d3f4g5"
	},
	{
		"name": "Hermenildo Sagassuga",
		"email": "hermesaga@email.com",
		"birth": "1979-12-20",
		"password": "Z1x2c3v4b5"
	},
	{
		"name": "Setembrino Trocatapas",
		"email": "setbrino@email.com",
		"birth": "2002-04-18",
		"password": "P0o9i8u7y6"
	}
]
Mostre os códigos necessários para:

 Mostrar todos os dados do primeiro e último usuário cadastrados.
 Mostrar a senha do "Hermenildo Sagassuga".
 Mostrar o e-mail do "Setembrino Trocatapas".
 Criar uma lista contendo todos os e-mails e exibir.
 Mostrar apenas o primeiro nome de todos os usuários.
 Mostrar quantos usuários existem na lista.
 Criar uma lista contendo apenas os nomes e exibir em ordem alfabética.
 Alterar o e-mail de "Marineuza Siriliano".
 Adicionar um novo usuário à lista.
 Remover o usuário "Setembrino Trocatapas".
 Adicionar a chave "active": True em todos os usuários.'''


users = [
	{
		"name": "Joca da Silva",
		"email": "jocasilva@email.com",
		"birth": "1980-10-25",
		"password": "Q1w2e3r4t5"
	},
	{
		"name": "Marineuza Siriliano",
		"email": "sirineuza@email.com",
		"birth": "2000-09-14",
		"password": "A1s2d3f4g5"
	},
	{
		"name": "Hermenildo Sagassuga",
		"email": "hermesaga@email.com",
		"birth": "1979-12-20",
		"password": "Z1x2c3v4b5"
	},
	{
		"name": "Setembrino Trocatapas",
		"email": "setbrino@email.com",
		"birth": "2002-04-18",
		"password": "P0o9i8u7y6"
	}
]

print(users[0])


print(users[-1])


for user in users:
    if user["name"] == "Hermenildo Sagassuga":
        print(user["password"])
        
        
for user in users:
    if user["name"] == "Setembrino Trocatapas":
        print(user["email"])
        

		
		
# 4. Criar uma lista contendo todos os e-mails e exibir
emails = []

for user in users:
    emails.append(user["email"])

print(emails)


# 5. Mostrar apenas o primeiro nome de todos os usuários
for user in users:
    print(user["name"].split()[0])
    


# 6. Mostrar quantos usuários existem na lista
print(len(users))
    



# 7. Criar uma lista contendo apenas os nomes e exibir em ordem alfabética
nomes = []

for user in users:
    nomes.append(user["name"])

nomes.sort()

print(nomes)


# 8. Alterar o e-mail de "Marineuza Siriliano"
for user in users:
    if user["name"] == "Marineuza Siriliano":
        user["email"] = "marineuza@email.com"

print(users)


# 9. Adicionar um novo usuário à lista
novo_usuario = {
    "name": "Fabiano Santos",
    "email": "fabiano@email.com",
    "birth": "1990-01-01",
    "password": "123456"
}

users.append(novo_usuario)

print(users)



# 10. Remover o usuário "Setembrino Trocatapas"
for user in users:
    if user["name"] == "Setembrino Trocatapas":
        users.remove(user)

print(users)



# 11. Adicionar a chave "active": True em todos os usuários
for user in users:
    user["active"] = True

print(users)