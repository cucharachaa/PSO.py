
"""
implementación básica de PSO (particle swarm optimization) por github.com/cucharachaa, 18-08-2023.
"""
import random

# Función unimodal: f(x) = (x - 2)^2 + 3 (f(2) = 3; minimo global)
#fun_objetivo = lambda x: ((x - 2) ** 2) + 3

#Funcion multimodal: f(x)= x^4 -4x^3 -4x^2 + 12x  
fun_objetivo = lambda x: x**4 - 4*x**3 -4*x**2 + 12*x

#Funcion ????
import math
fun_objetivo = lambda x: math.sin(x) + math.sin(10*x) + math.log(x**2 + 1)

class Particula:
    def __init__(self, posicion: list, velocidad: list, cognitivo: float, social:float, inercia: float):
        self.posicion  = posicion
        self.velocidad = velocidad
        self.c1 = cognitivo
        self.c2 = social
        self.w  = inercia
        self.resultado_personal = 0
        self.mejor_resultado_personal = float("inf")
        self.mejor_pos_personal = posicion

    def fitness(self, funcion_obj):
        self.resultado_personal = funcion_obj(self.posicion[0])

        #Actualizamos mejor personal basado en el resultado de la funcion objetivo
        if self.resultado_personal < self.mejor_resultado_personal:
            self.mejor_pos_personal = self.posicion.copy()
            self.mejor_resultado_personal = self.resultado_personal

       
    def actualiza_velocidad(self):
        # c1,c2 constantes definidas por nosotros (cognitiva y social)
        # r1,r2 numeros aleatorios entre 0 y 1
        for i in range(0, dim):
            r1= random.random()
            r2 = random.random()
            factor_cognitivo = self.c1 * r1 * (self.mejor_pos_personal[i] - self.posicion[i])
            factor_social    = self.c2 * r2 * (mejor_pos_global[i] - self.posicion[i])
            self.velocidad[i] = self.w * self.velocidad[i] + factor_cognitivo + factor_social

    def actualiza_posicion(self):
        for i in range(0,dim):
            self.posicion[i] = self.posicion[i] + self.velocidad[i]
            #borde maximo
            if self.posicion[i] > bordes_x[1]:
                self.posicion[i] = bordes_x[1]
            #borde minimo
            if self.posicion[i] < bordes_x[0]:
                self.posicion[i] = bordes_x[0]


def PSO(num_particulas: int,bordes_x: list, dim: int, max_iter: int):
    global mejor_pos_global
    mejor_pos_global = None
    # Asigna respectivamente pos, vel (aleatorias) iniciales a las partículas y constantes c1, c2, w
    enjambre = []
    for _ in range(0, num_particulas):
        x = random.uniform(bordes_x[0], bordes_x[1])
        enjambre.append(
            Particula(
                [x, fun_objetivo(x)], 
                [random.uniform(-1, 1), random.uniform(-1, 1)], 
                1, 
                2,
                0.5,
            )
        )
    
    i = 0
    while i < max_iter:
        for j in range (0, num_particulas):
            # Actualiza la mejor posición global
            if mejor_pos_global is None or enjambre[j].mejor_resultado_personal < fun_objetivo(mejor_pos_global[0]):
                            mejor_pos_global = enjambre[j].mejor_pos_personal
            enjambre[j].actualiza_velocidad()
            enjambre[j].actualiza_posicion()
            enjambre[j].fitness(fun_objetivo)        
        i+=1
    print("FINAL:")
    print("Mejor posición global (x):", mejor_pos_global[0])
    print("Mejor resultado global (y):", fun_objetivo(mejor_pos_global[0]))



if __name__ == "__main__":
    num_particulas = 20
    max_iter = 100
    bordes_x = (-100, 100)  # dominio de TODAS las particulas (min, max) en el eje x
    global dim  #para no pasarlo como parametro de cada particula
    dim = 2
    PSO(num_particulas, bordes_x, 2, max_iter) 

