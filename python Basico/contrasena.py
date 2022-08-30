import random
import string

def generar_contrasena():
    caracter = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

    contrasena = []

    while len(contrasena) < 16:
        caracteres = random.choice(caracter)
        contrasena.append(caracteres)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    pregunta = 'tu nueva contrasena es:  '
    respuesta =input('quiere crear una contrasena? ')
    if respuesta == 'si':
        print(pregunta.capitalize() + contrasena)
    else:
        print('contrasena es la misma de siempre'.capitalize())


if __name__ == '__main__':
    run()