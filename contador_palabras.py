def contador_de_palabras(pensamiento = input("¿En qué estás pensando?\n")):
    numero_de_palabras = len(pensamiento.split(' '))
    print(f'¡Muy bien, tu me has mostrado tu pensamiento en {numero_de_palabras} palabras!') 

contador_de_palabras()