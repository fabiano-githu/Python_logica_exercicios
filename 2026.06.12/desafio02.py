
'''Mostre a tabuada de multiplicação do número 5 à partir de 5 x 0 até 5 x 10 usando while.
Mostre a tabuada completa desde 0 x 0 até 10 x 10 usando while aninhado.'''

'''print(f"\n---Tabuada de {i}---\n")
print("\n")

i = 0

while i <= 10:
    j = 0

    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1

    print("-" * 20)
    i += 1

    print("\n")'''



i = 0

while i <= 10:
    print(f"\n--- Tabuada de {i} ---\n")

    j = 0

    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1

    print("-" * 12)
    i += 1
    print()