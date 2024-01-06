import random

palabras=['python','java','javascript','html','css']
letras_correctas=[]
letras_incorrectas=[]
intentos=6
aciertos=0
juego_terminado=False

def elegir_palabra(palabras):
    palabra_elegida=random.choice(palabras)
    letras_unicas= len(set(palabra_elegida))

    return palabra_elegida,letras_unicas

def pedir_letra():
    letra_elegida=""
    es_valida=False
    abecedario='abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida=input("Escribe una sola letra: ").lower()

        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")
            
    return letra_elegida

def mostrar_tablero(palabra_elegida):
    lista_oculta=[]
    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append("_ ")
    print(" ".join(lista_oculta))

def chequear_letra(letra_elegida,palabra_oculta,intentos,aciertos):
    fin = False
    
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        aciertos +=1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra, intenta con otra letra.")
    else:
        letras_incorrectas.append(letra_elegida)
        intentos -=1
    
    if intentos == 0:
        fin = perder()
    elif aciertos == letras_unicas:
        fin = ganar(palabra_oculta)
    
    return intentos, fin, aciertos

def perder():
    print("Te has quedado sin vidas... Has perdido.")
    print(f"La palabra oculta era '{palabra}'")

    return True

def ganar(palabra_oculta):

    mostrar_tablero(palabra_oculta)
    print("Has ganado!!")

    return True

palabra,letras_unicas=elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 40 + '\n')
    print('Palabra Oculta aquí debajo: ')
    mostrar_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ', letras_incorrectas)
    print('Vidas: ', intentos)
    print('\n' + '*' * 40 + '\n')

    letra=pedir_letra()
    
    intentos,terminado,aciertos=chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado=terminado

    
