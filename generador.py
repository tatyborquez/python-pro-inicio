import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("introduce la longitud de la contraseña:"))
contrasena = ""
for i in range(longitud):
    contrasena += random.choice(caracteres)

print("la contraseña es:" , contrasena)
