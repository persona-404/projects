'''
    Clase buscaminas.
    Encargada de crear arreglo de minas y llevar cuenta de las minas salvadas
    Encargada de decir si perdio
'''

from random import randint

class Buscaminas(object):
    def __init__(self, columnas, filas):
        self.tablero = []
        self.columnas = columnas
        self.filas = filas
        self.totalMinas = 0
        self.minasRestantes = 0
        self.finalMinas = 0

        self.tableroUsuario = [[u'\u25a1' for x in range(self.columnas)]
                               for x in range(self.filas)]


    def calcularNumeroMinas(self):
        espacios = self.columnas * self.filas
        porcentajeMinas = randint(25, 40)
        
        self.totalMinas = int(porcentajeMinas * espacios / 100)
        self.minasRestantes = self.finalMinas
        

    def llenarTableroMinas(self):
        self.calcularNumeroMinas()

        v1 = self.totalMinas / self.columnas
        v2 = self.totalMinas / self.filas
        
        for fila in range(self.filas):
            lista = []
            totalMinasPorFila = randint(1, ((v1 + v2) * 2))
            minasPorFila = totalMinasPorFila
            for columna in range(self.columnas):
                if randint(0, 1) == 1 and minasPorFila > 0:
                    lista.append('x')
                    self.finalMinas += 1
                    minasPorFila -= 1
                else:
                    lista.append(0)

            self.tablero.append(lista)
                        
                #if fila <= int(self.filas / 2):
                #    if minas >= int((self.totalMinas / 2)) and randint(0, 1) == 1:
                #        lista.append('x')
                #        self.finalMinas += 1
                #        minas -= 1
                #    else:
                #        lista.append(0)    
                #else:
                #    if randint(0, 1) == 1 and minas >= 0:
                #        lista.append('x')
                #        self.finalMinas += 1
                #        minas -= 1
                #    else:
                #        lista.append(0)   

        #self.tablero = [['x' if randint(0, 1) == 1 else 0 for x in range(self.columnas)]
        #                for x in range(self.filas)]
        

    def llenarTableroNumeros(self):
        for fila in range(0, self.filas):
            for columna in range(0, self.columnas):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = self.traerNumeroMinas(fila, columna)


    def traerNumeroMinas(self, fila, columna):
        totalMinas = 0
        
        for f in range(-1, 2):
            for c in range(-1, 2):
                if fila + f >= 0 and columna + c >= 0:
                    try:
                       if self.tablero[fila + f][columna + c] == 'x':
                           totalMinas += 1
                    except:
                        continue

        return totalMinas
    
                    
    def hayMina(self, fila, columna):
        try:
            if self.tablero[fila][columna] == 'x':
                return True
            else:
                return False
        except:
            return False


    def verTablero(self):
        print self.tablero
        

    def marcarTablero(self, fila, columna):
        self.tableroUsuario[fila][columna] = 'm'

        return self.verificarSiYaGano(fila, columna)


    def verificarSiYaGano(self, fila, columna):
        if self.hayMina(fila, columna):
            self.minasRestantes -= 1

        if self.minasRestantes == 0:
            return True

        return False


    def mostrarCasilla(self, fila, columna):
        if self.hayMina(fila, columna):
            return False
        else:
            if self.tablero[fila][columna] == 0:
                self.tableroUsuario[fila][columna] = ' '
                self.tablero[fila][columna] = ' '
                self.abrirCasillasContiguas(fila, columna)
            elif self.tablero[fila][columna] != ' ':
                self.tableroUsuario[fila][columna] = self.tablero[fila][columna]

        return True


    def imprimirTablero(self, tableroMostrar):
        print "\t",
        for x in range(self.columnas):
            if x > 9:
                print str(x),
            else:
                print str(x) + " ",

        print ""
        print "___________________________________"
        
        for fila in range(self.filas):
            print str(fila) + "\t",
            for columna in range(self.columnas):
                if type(tableroMostrar[fila][columna]) is int:
                    print str(tableroMostrar[fila][columna]) + " ",
                else:
                    print tableroMostrar[fila][columna] + " ",

            print ""


    def abrirCasillasContiguas(self, fila, columna):
        for f in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                if fila + f == fila and columna + c == columna:
                    continue
                if fila + f >= 0 and columna + c >= 0:
                    try:
                       self.mostrarCasilla(fila + f, columna + c)
                    except:
                        continue
