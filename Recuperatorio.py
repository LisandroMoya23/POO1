'''RECUPERATORIO PARCIAL Nº 2- ESTRUCTURAS DE DATOS Y ALGORITMOS
                                                                                                               18 de diciembre de 2020
Ejercicio 1: Considere el TAD Montículo Binario.
a)    Construya el objeto de datos.
b)    Especifique e implemente la operación insertar_elem().
c)    Calcule el T(N) de la operación construida en el inciso b) e indique a qué Orden de complejidad pertenece.
'''
import numpy as np
import math

class MonticuloBinario:
    __elementos: np.ndarray
    __cant = 0
    
    def __init__(self, cant: int):
        self.__elementos = np.full(cant, None)
        self.__cant = 0
        self.__elementos[0] = -math.inf
                    
    def intercambiar(self, pos1, pos2):
        aux = self.__elementos[pos1] #2U
        self.__elementos[pos1] = self.__elementos[pos2] #3u
        self.__elementos[pos2] = aux #2U

    def insertar(self, elemento):
        self.__cant += 1 #2U
        self.__elementos[self.__cant] = elemento #2U

        actual = self.__cant #1U
        padre = self.__cant // 2 #2U
        while self.__elementos[padre] > self.__elementos[actual]: #3N
            self.intercambiar(padre, actual) #7N en total 

            actual = padre #N
            padre = actual // 2 #2N
#C) El T(N) de la funcion "Insertar_elem()" 13N + 7U y su orden de complejidad es O(n) (orden de complejidad lineal)
'''
Ejercicio 2: Considere el TAD Grafo, formado por N vértices.
a)    Construya el objeto de datos, usando la representación más adecuada para lograr la optimizar la operación indicada en el inciso b)
b)    Especifique e implemente la operación que informe si existe un camino entre dos vértices cuyas etiquetas se ingresan previamente por teclado.
'''
class GrafoSecuencial:
    __CantidadV : int
    __matriz : np.ndarray

    def __init__(self, n):
        self.__CantidadV = n
        self.__matriz = np.zeros((n, n), dtype=int)

    def camino(self, origen, destino):
        return destino in self.rep(origen)

if __name__ == '__main__':
	grafo1 = GrafoSecuencial(5)
	origen = input("Ingrese origen:")
	destino = input("Ingrese destino:")
	if grafo1.camino(origen,destino):
		print("Existe un camino entre el origen {} y el dstino {}".format(origen,destino))
	else:
		print("No existe un camino entre el origen {} y el dstino {}".format(origen,destino)) 

'''
Ejercicio 3:  Considere trabajar con el TAD Tabla Hash, usando la política de manejo de colisiones Encadenamiento, para una cantidad aproximada  de 4000 claves, siendo éstas números de registro de alumnos.
a)    Construya el objeto de datos.
b)    Codifique la función hash Módulo.
c)    Especifique e implemente la operación Buscar_Clave().
d)    Calcule el T(N) de la operación construida en el inciso c) e indique a qué Orden de complejidad pertenece.
'''

import numpy as np

class Nodo:
    __dato = None
    __siguiente = None

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
    
    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self, dato):
        self.__dato = dato
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
class listaEncadenada:
    __cabeza = None
    __cantidad: int
    
    def __init__ (self):
        self.__cabeza 
        self.__cantidad = 0

    def buscar(self, dato):
        aux = self.__cabeza #1U
        
        while aux != None and aux.getDato() != dato: #3N
            aux = aux.getSiguiente() #2N
        
        if aux == None: #1u
            return -1
        else:
            return aux

class EncadenamientoHash:
    __dimension: int
    __tabla = None

    def __init__(self, dimension):
        self.__dimension = self.getPrimo(int(dimension//0.7)) #Factor de carga = 0.7 ejemplo 100 // 0.7 = 142 primo mas cercano 149
        self.__tabla = np.empty(self.__dimension, dtype=listaEncadenada)
    
        for i in range(0,self.__dimension):
            self.__tabla[i] = None
    
    def modulo(self,valor):
        return valor % self.__dimension

    def buscar_clave(self, clave):
        indice = self.modulo(clave) #2U

        if self.__tabla[indice] is not None: #2U
            resultado_busqueda = self.__tabla[indice].buscar(clave) #5N+4U
            
            if resultado_busqueda == -1: #1U
                print(f"La clave {clave} no se encontró en la tabla hash.")
            else:
                print(f"La clave {clave} se encontró en la posición {indice}, en la lista encadenada en esa posición.")
                return resultado_busqueda
        else:
            print(f"La clave {clave} no se encontró en la tabla hash.")
# El T(N) de la funcion "Buscar_clave()" 5N + 9U y su orden de complejidad es O(n) (orden de complejidad lineal)