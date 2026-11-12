


def leer_entero(mensaje):
    """Pide un entero y repite la pregunta si se ingresa otro dato"""
    valido = False
    while valido == False:
        try:
            numero = int(input(mensaje).strip())
            valido = True
        except ValueError:
            print("Ingrese un numero entero valido")
    return numero


def leer_entero_no_negativo(mensaje):
    """Pide un entero mayor o igual a cero"""
    numero = leer_entero(mensaje)
    while numero < 0:
        print("El numero no puede ser negativo")
        numero = leer_entero(mensaje)
    return numero


def leer_edad(mensaje):
    """Pide una edad entre 15 y 45, incluyendo ambos limites"""
    edad = leer_entero(mensaje)
    while edad < 15 or edad > 45:
        print("La edad debe estar entre 15 y 45")
        edad = leer_entero(mensaje)
    return edad


def leer_decimal_no_negativo(mensaje):
    """Pide un valor decimal finito mayor o igual a cero"""
    valido = False
    while valido == False:
        try:
            numero = float(input(mensaje).strip().replace(",", "."))
            if numero >= 0 and str(numero) != "inf":
                valido = True
            else:
                print("Ingrese un numero finito mayor o igual a cero")
        except ValueError:
            print("Ingrese un numero valido")
    return numero


def leer_texto_no_vacio(mensaje):
    """Pide un texto que contenga algo mas que espacios"""
    texto = input(mensaje).strip()
    while texto == "":
        print("El texto no puede estar vacio")
        texto = input(mensaje).strip()
    return texto


def leer_nombre_jugador(mensaje):
    """Pide un nombre con letras, espacios, apostrofes o guiones"""
    letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúüÁÉÍÓÚÜ"
    permitidos = letras + " '-"
    nombre = leer_texto_no_vacio(mensaje)

    valido = False
    while valido == False:
        if nombre[0] not in letras:
            print("El nombre debe comenzar con una letra")
            nombre = leer_texto_no_vacio(mensaje)
        else:
            bien = True
            for caracter in nombre:
                if caracter not in permitidos:
                    bien = False
            if bien == True:
                valido = True
            else:
                print("El nombre solo puede tener letras, espacios, apostrofes o guiones")
                nombre = leer_texto_no_vacio(mensaje)

    return nombre