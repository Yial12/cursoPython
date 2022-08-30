def run():
    CONTRASENA = 'contrasena'
    contrasena = input('introduce una contrasena: '.capitalize())

    if contrasena == CONTRASENA:
        print('acceso autorizado'.capitalize())
    else:
        print('acceso denegado'.capitalize())


if __name__ == '__main__':
    run()