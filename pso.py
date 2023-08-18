# Asignar posiciones y velocidades aleatorias iniciales a las partículas

# c1,c2, r1,r2 constantes definidas por nosotros
# c1, c2 constantes definidas por nosotros
# r1,r2 numeros aleatorios entre 0 y 1

# Funcion unimodal, que solo tiene 1 optimo global

import random

# Función unimodal: f(x) = (x - 2)^2 + 3 (f(2) = 3; minimo global)
fun_objetivo = lambda x: ((x - 2) ** 2) + 3


class Particula:
    def __init__(self, posicion: list, velocidad: list, cognitivo: float, social:float, inercia: float):
        self.posicion  = posicion
        self.velocidad = velocidad
        self.mejor_pos_personal = []
        self.c1 = cognitivo
        self.c2 = social
        self.w  = inercia

    def fitness(self, funcion):
       resultado = funcion(self.posicion[0])
       


    def actualiza_velocidad(self):
        for i in range(0, dim):
            r1= random.random()
            r2 = random.random()
            factor_cognitivo = self.c1 * r1 * (self.mejor_pos_personal[i] - self.posicion[i])
            factor_social    = self.c2 * r2 * (mejor_pos_global[i] - self.posicion[i]) #como comunicarse entre todas las particulas?
            self.velocidad[i] = self.w * self.velocidad[i] + factor_cognitivo + factor_social


    def actualiza_posicion(self):
        pass


def PSO(num_particulas: int,bordes_x: list, dim: int, max_iter: int):
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
            enjambre[j].fitness(fun_objetivo)
            enjambre[j].actualiza_velocidad()
            enjambre[j].actualiza_posicion()
            
        i+=1
    return


if __name__ == "__main__":
    num_particulas = 50
    max_iter = 100
    bordes_x = (0, 10)  # dominio de TODAS las particulas (min, max) en el eje x
    global dim
    dim = 2
    PSO(num_particulas, bordes_x, 2, max_iter, )
