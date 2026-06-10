

"""Crie um dicionário chamado "car" com as chaves "marca", "modelo", "ano" e valores "Ford", "Mustang", c24.
 Imprima o valor da chave "model".
 Adicione uma nova chave "cor" com o valor "vermelho".
 Remova a chave "marca" usando pop().
 Imprima o dicionário."""

car = {
    "marca": "Ford",
    "modelo": "mustang",
    "ano": "2024",
}

print(car["modelo"])

car["cor"] = "vermelho"

car.pop("marca")

print(car)