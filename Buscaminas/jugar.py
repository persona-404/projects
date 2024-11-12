from buscaminas import Buscaminas
import sys

def empezarJuego():
    terminar = False

    tamanio = input("Ingresa el tamanio del tablero. Ej.: 7,8\n")
    
    b = Buscaminas(tamanio[0], tamanio[1])
    b.llenarTableroMinas()
    b.llenarTableroNumeros()

    #b.imprimirTablero(b.tablero)
    #print ""
    b.imprimirTablero(b.tableroUsuario)
    print ""

    instrucciones = "Para terminar, escrible 'salir'\n"
    instrucciones += "Para marcar una casilla escribe 'marcar' y la coordenada de la casilla. Ej.: "
    instrucciones += "marcar 1,1\n"
    instrucciones += "Para abrir casilla, escribe 'mostrar' y la coordenada de la casilla. Ej.: "
    instrucciones += "mostrar 1,1\n"

    print instrucciones

    while not terminar:
        comando = raw_input("\nOpcion: ")

        if comando == 'salir':
            terminar = True
        else:
            comando = comando.split(' ')

            if comando[0] == 'marcar':
                puntos = comando[1].split(',')
                
                if b.marcarTablero(int(puntos[0]), int(puntos[1])):
                    b.imprimirTablero(b.tableroUsuario)
                    print "\nGanaste"
                    
                    break

                b.imprimirTablero(b.tableroUsuario)
            elif comando[0] == "mostrar":
                puntos = comando[1].split(',')
                
                if not b.mostrarCasilla(int(puntos[0]), int(puntos[1])):
                    print "Perdiste"
                    
                    comando = raw_input("Jugar de nuevo? (s/n): ")

                    if comando == 's':
                        empezarJuego()
                    else:
                        sys.exit(0)
                else:
                    b.imprimirTablero(b.tableroUsuario)
            else:
                print "\nNo se reconocio la opcion.\n"
                print instrucciones

    
#Empezar juego
empezarJuego()
