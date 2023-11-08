import random

print("******GENERADOR DE CONTRASEÑAS**********")

minuscula = int(input("Indique número mínimo de minusculas: "))
mayuscula = int(input("Indique número mínimo de mayusculas: "))
numerico = int(input("Indique número mínimo de caracteres númericos: "))
longitud = int(input("Indique longitud de la contraseña: "))

abecedario = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

contraseña = []
sumatoria = 0


def numAleatorio():
    return random.randint(0, len(abecedario) - 1)


def letra():
    return abecedario[numAleatorio()]


while sumatoria <= longitud:
    while minuscula > 0:
        if sumatoria == longitud:
            break

        contraseña.append(letra())
        minuscula -= 1
        sumatoria += 1

    while mayuscula > 0:
        if sumatoria == longitud:
            break

        contraseña.append(letra().upper())
        mayuscula -= 1
        sumatoria += 1

    while numerico > 0:
        if sumatoria == longitud:
            break

        contraseña.append(str(random.randint(1, 9)))
        numerico -= 1
        sumatoria += 1

    if sumatoria != longitud:
        minuscula, mayuscula, numerico = 1, 1, 1

    if sumatoria == longitud:
        break

# Con random.shuffle desordeno el array
random.shuffle(contraseña)

# Con "".join(contraseña) extraigo los elemntos del array y creo una cadena
clave = "".join(contraseña)

print(clave)
print(f"SU CONTRASEÑA ES: {contraseña}")