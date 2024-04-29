import random

def dar_retroalimentacion(palabra_secreta, palabra_propuesta):
    resultado = ""
    letras_correctas = set()

    if len(palabra_propuesta) != len(palabra_secreta):
        return "La palabra debe contener {} letras.".format(len(palabra_secreta))

    for i, letra in enumerate(palabra_propuesta):
        if letra in palabra_secreta:
            if letra == palabra_secreta[i]:
                resultado += '[' + letra + ']'
                letras_correctas.add(letra)
            else:
                resultado += '(' + letra + ')'
        else:
            resultado += letra

    if letras_correctas == set(palabra_secreta):
        return "¡Felicidades! Has adivinado la palabra.\n{}".format(palabra_secreta)

    return resultado

ListaPalabras = ["nariz", "casco", "mango"]
intentos = 5

print("REGLAS:")
print("1- Si la letra existe en la palabra, y se encuentra en la posición correcta se encierra en corchetes`[🐧]`")
print("2- Si las letras existen en la palabra a encontrar pero sus posiciones no coinciden se encierra en paréntesis`(🐧)`")
print("3- Si la letra no tiene parentesis significa que la letra no se encuentra en la palabra")
print("4- Tienes 5 intentos")
print("Éxitos🐧")

resp = "S"
while resp.upper() == "S":
    num = random.randint(0, len(ListaPalabras) - 1)
    sol = ListaPalabras[num]
    
    print("La palabra secreta ha sido generada.")
    print("")

    for i in range(intentos):
        print("")
        palabra = input("Dame una palabra de 5 letras: ").lower()
        print("")

        while len(palabra) != 5:
            palabra = input("La palabra debe contener 5 letras: ").lower()

        resultado = dar_retroalimentacion(sol, palabra)
        print(resultado)

        if palabra == sol:
            print("La palabra es correcta")
            break
        else:
            print("Intento {}/{}".format(i+1, intentos))
    else:
        print("Se han acabado los intentos")
        print("No has acertado")

    resp = input("¿Quieres volver a jugar? (S/N): ")
    while resp.upper() not in ["S", "N"]:
        resp = input("Introduce S o N: ")
print("Adiós🐧")
