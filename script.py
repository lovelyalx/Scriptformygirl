import os
import time
from colorama import Fore, Style, init
import pygame

init()


texto = "Creador por @stevendz.28" 
texto_part1 = "                                                Creado por "
texto_morado = "@"
texto_amarillo = "stevendz.28"
lineas = "            _______________________________________________________________________________________________"
autores_1 = "Blanca Varela"
adaptado_2 = "Lovely"
op_1 = "1. Sunflower"
op_2 = "2. Tiroteo"
op_3 = "3. Te quiero tanto"
op_4 = "4. salir"

hola_grande = r"""






                                                          is
                            $$$$$                                                         $$$$$$$$$
                            $$$$$                                                        $$$$$ $$$$$
                            $$$$$    $$$$$$$$$$$    $$$$$     $$$$$   $$$$$$$$$$$$$            $$$$$
                            $$$$$  $$$$$    $$$$$$   $$$$$   $$$$$   $$$$$    $$$$$$          $$$$$ 
                            $$$$$  $$$$$    $$$$$$    $$$$$ $$$$$    $$$$$$$$$$$$$$$         $$$$$  
                            $$$$$  $$$$$    $$$$$$     $$$$$$$$$     $$$$$         				
                            $$$$$    $$$$$$$$$$$        $$$$$$$       $$$$$$$$$$$$$          $$$$$  
                     what
"""
amor = """
¿Qué es el amor?
Tal vez un suspiro.
Un gesto, sin ruido.

No está en las palabras,
ni en los actos grandes.
Se esconde.

A veces es silencio,
a veces es vacío,

El aire ya no es el mismo.
Lo que una vez brilló
ahora se desliza entre sombras.

Como una flor que ya no huele,
pero sigue siendo flor.

Las primeras lluvias ya no caen
con la misma fuerza.
El agua se mueve más despacio.

No siempre se siente
como aquella primera chispa.
Pero el fuego sigue.

Y quizás eso esté bien.
Quizás el amor
no necesita ser igual
para seguir siendo amor.

¿Acaso no es más profundo ahora?
Como un bloque de hierro,
la primera vez que lo calientas,
hirviendo, ardiendo.

Pero con el tiempo se enfría,
pierde ese brillo abrasante,
y aún así, se vuelve más sólido.

Más fuerte que nunca,
aunque ya no arda
como al principio.

¿Realmente lo he dicho?
¿Realmente lo haz dicho?
¿Lo he sentido también?
¿Lo has sentido también?

"""
os.system("cls")
# Parte 1
print(hola_grande)
print(lineas + "\n")
print(texto_part1 + Fore.MAGENTA + texto_morado + Fore.LIGHTYELLOW_EX + texto_amarillo + Style.RESET_ALL)

time.sleep(10)  # Esperar 4 segundos antes de cerrar
os.system("cls")

# Parte2
print(amor)
print("                                                                     Inspirado en " + Fore.MAGENTA + autores_1 + Fore.RESET + " , adaptado por " + Fore.MAGENTA + adaptado_2 + Fore.RESET + "." )
input()

os.system("cls")

def menu_1():
    print("¿Qué deseas hacer? - tienes el poder. Pero no los huevos!\n")
    print(Fore.LIGHTYELLOW_EX + op_1 + Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + op_2 + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + op_3 + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + op_4 + Style.RESET_ALL)

def opcion_1():
    os.system("cls")  
    print("Iniciando..")
    time.sleep(2)
    os.system("cls")

    # Inicializar pygame
    pygame.init()

    # Cargar la música
    pygame.mixer.music.load("song.mp3")  # Cambia esto por la ruta de tu archivo de música

    # Definir la letra de la canción con sus tiempos
    letra = [
        (0.5, "\n♪ Pensando de una mala manera ♪"),
        (1.7, "♪ Perdiendo el agarré ♪\n"),
        (3, "♪ Gritando en mi cara ♪"),
        (4.3, "♪ Bebé no tropieces ♪\n"),
        (5.7, "♪ Alguien tomo una big L ♪"),
        (6.8, "♪ No sé como se sintió ♪\n"),
        (8.4, "♪ Mirandote de lados ♪"),
        (9.7, "♪ Fiesta en el TILT ♪\n"),
        (11.3, "♪\n"),
        (13.4, "♪ Hay algunas cosas que simplemente no se pueden rechazar ♪"),
        (15.9, "♪ Ella quiere montarme como un crucero ♪\n"),
        (18.8, "♪ Y no estoy intentando perderlo ♪"),
        (22.8, "♪ Entonces te quedas en polvo ♪"),
        (25.2, "♪ A menos que me quede atascado por ti ♪\n"),
        (27.9, "♪ Eres mi girasol ♪\n"),  # Amarillo
        (30.5, "♪ Creo que tu amor seria demasiado ♪"),
    ]

    # Función para mostrar la letra sincronizada
    def mostrar_letra(letra):
        inicio = time.time()  # Tiempo de inicio de la reproducción
        pygame.mixer.music.play()  # Reproducir la música

        for tiempo, linea in letra:
            while True:
                # Calcular el tiempo transcurrido
                tiempo_actual = time.time() - inicio
                # Si es el momento de mostrar la línea, imprímela y sal del bucle
                if tiempo_actual >= tiempo:
                    if tiempo == 27.9:  # Si es la línea que quieres colorear
                        print(Fore.LIGHTYELLOW_EX + linea + Style.RESET_ALL)  # Amarillo
                    else:
                        print(linea)  # Otras líneas en color normal
                    break
                time.sleep(0.1)  # Esperar un poco para no consumir demasiada CPU

        # Esperar a que termine la música
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    # Llamar a la función para mostrar la letra
    mostrar_letra(letra)

    # Finalizar pygame
    pygame.quit()
    os.system("cls")
def opcion_2():
    os.system("cls")  
    print("Iniciando..")
    time.sleep(2)
    os.system("cls")

    # Inicializar pygame
    pygame.init()

    # Cargar la música
    pygame.mixer.music.load("song_1.mp3")  # Cambia esto por la ruta de tu archivo de música

    # Definir la letra de la canción con sus tiempos y colores
    letra = [
        (0.5, "\n♪\n", Fore.RED),  # Rojo
        (3.4, "♪ Se me congela el mundo ♪", Fore.LIGHTYELLOW_EX),  # Amarillo
        (5, "♪ Siempre que nos vemos ♪\n", Fore.LIGHTRED_EX),  # Rojo
        (7.8, "♪ Discutir contigo ♪", Fore.LIGHTBLUE_EX),  # Azul
        (9.5, "♪ Es como un tiroteo ♪", Fore.LIGHTMAGENTA_EX),  # Magenta
        (12, "♪ Y pienso morirme primero ♪\n", Fore.LIGHTCYAN_EX),  # Cian
        (15, "♪ Oh ♪", Fore.LIGHTGREEN_EX),  # Verde
        (16, "♪ Oh ♪", Fore.LIGHTGREEN_EX),  # Verde
        (16.5, "♪ Oh ♪", Fore.LIGHTGREEN_EX),  # Verde
        # Agrega más líneas con sus tiempos y colores
    ]

    # Función para mostrar la letra sincronizada
    def mostrar_letra(letra):
        inicio = time.time()  # Tiempo de inicio de la reproducción
        pygame.mixer.music.play()  # Reproducir la música

        for tiempo, linea, color in letra:
            while True:
                # Calcular el tiempo transcurrido
                tiempo_actual = time.time() - inicio
                # Si es el momento de mostrar la línea, imprímela y sal del bucle
                if tiempo_actual >= tiempo:
                    print(color + linea + Style.RESET_ALL)  # Imprimir en el color correspondiente
                    break
                time.sleep(0.1)  # Esperar un poco para no consumir demasiada CPU

        # Esperar a que termine la música
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    # Llamar a la función para mostrar la letra
    mostrar_letra(letra)

    # Finalizar pygame
    pygame.quit() 
    os.system("cls")      
def opcion_3():
    # Limpiar pantalla e iniciar
    os.system("cls")
    print("Iniciando..")
    time.sleep(2)
    os.system("cls")

    pygame.init()

    # Cargar la música
    pygame.mixer.music.load("song_2.mp3")  # Cambia esto por la ruta de tu archivo de música

    # Definir la letra de la canción con sus tiempos y colores
    letra = [
        (0.5, "\n♪ Si tal vez ♪", Fore.RESET),  # Rojo
        (3.9, "♪ Detalle a detalle ♪\n", Fore.RESET),  # Amarillo
        (7, "♪ Podrias conquistarme ♪", Fore.RESET),  # Rojo
        (9.3, "♪ Seria tuya ♪", Fore.RESET),  # Azul
        (12.7, "♪ Te quiero ♪\n", Fore.LIGHTRED_EX),  # Magenta
        (13.5, "♪ Tanto ♪", Fore.RESET),  # Cian
        (14.2, "♪ Tanto ♪", Fore.RESET),  # Verde
        (15, "♪ Tanto ♪", Fore.RESET),
        (15.8, "♪ Tanto ♪", Fore.RESET),
        (16.6, "♪ Tanto ♪\n", Fore.RESET),  # Verde
        (17.8, "♪ Cada un poco mas ♪\n", Fore.RESET),
        (22, "♪", Fore.RESET),  # Verde
         # Agrega más líneas con sus tiempos y colores
       ]

    # Función para mostrar la letra sincronizada
    def mostrar_letra(letra):
        inicio = time.time()  # Tiempo de inicio de la reproducción
        pygame.mixer.music.play()  # Reproducir la música

        for tiempo, linea, color in letra:
            while True:
                # Calcular el tiempo transcurrido
                tiempo_actual = time.time() - inicio
                # Si es el momento de mostrar la línea, imprímela y sal del bucle
                if tiempo_actual >= tiempo:
                    print(color + linea + Style.RESET_ALL)  # Imprimir en el color correspondiente
                    break
                time.sleep(0.1)  # Esperar un poco para no consumir demasiada CPU

        # Esperar a que termine la música
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    # Llamar a la función para mostrar la letra
    mostrar_letra(letra)

    # Finalizar pygame
    pygame.quit()
    os.system("cls")
# Función principal
def main():
    while True:
        menu_1()
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "4":
            print("Saliendo del Script")
            time.sleep(2)
            break
        else:
            os.system("cls")
            print("Opción no válida. Por favor escriba bien cabeza de cholito!")
            time.sleep(3)
            os.system("cls")

# Ejecutar el programa
if __name__ == "__main__":
    main()








