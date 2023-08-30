import random
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     -|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     -|-  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     -|-  |
     |    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     -|-  |
     | |  |
          |
    =========''']
palabras = """valoracion aprenderpython comida juego python web imposible
           variable curso volador cabeza reproductor mirada escritor billete
           lapicero celular valor revista gratuito disco voleibol
           anillo estrella""".split()


def buscarPalabraAleat(listaPalabras):
    # Esta funcion retorna una palabra aleatoria.
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)])
    print("")
    fin = " "
    print('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print(letra, fin)
    print("")
    espacio = '_' * len(palabraSecreta)
    # Remplaza los espacios en blanco por la letra bien escrita
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    # Mostrará la palabra secreta con espacios entre letras
    for letra in espacio:
        print(letra, fin)
    print("")


def elije_letra(algunaLetra):
    # Devuelve la letra que el jugador ingreso.
    # Esta función hace que el jugador ingrese
    # una letra y no cualquier otra cosa
    while True:
        print('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print('Introduce una sola letra.')
        elif letra in algunaLetra:
            print('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print('Elije una letra.')
        else:
            return letra


def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar,
    # de lo contrario devuelve False
    print('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')


print('A H O R C A D O')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
    # El usuairo elije una letra.
    letra = elije_letra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        # Se fija si el jugador ganó
