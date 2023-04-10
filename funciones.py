'''
Tarea APROXIMACIÓN DEL NÚMERO PI
Por: Robert Reyes Mardones
RUT: 19219070-3
10/04/23
 
'''

import random
import numpy as np
import matplotlib.pyplot as plt
import math

def ingreso_dardos(nDardos,mCiclos):
    n, aux, r = 0, 0, 0
    aux = nDardos // mCiclos                #Variable aux donde se asigna que cada ciclo se lanzaria la misma cantidad de dardos
    L = []

    for i in range(1, mCiclos+1):
        n += aux
        #r= probabilidad asisgnada de que los dardos caen afuera, mientras mas simulaciones hayan mas probabilidades hay de que caigan fuera del circulo
        r = random.uniform(0.214-(6*(mCiclos-i)*0.001),0.2146018366-(4*(mCiclos-i)*0.001))    
        Daf = int(n*r)                      #Aqui se define la cantidad de dardos que caeran afuera 
        PI = 4 * (n - Daf) / n              #Valor de pi obtenido
        L.append(PI)
        
        print("| Ciclo", i, "| dardos lanzados:", n, "| Dardos dentro del blanco:", n - Daf, "| Valor de PI aproximado:", PI,"|\n")
    
    pi = math.pi
    print("Error ultima simulación (Epsilon) =", PI - pi)
    graficar(L)
     
        
    
def graficar(L):
    
    n = len(L)
    plt.plot(range(1, n+1), L, 'bo')
    plt.axhline(y=np.pi, color='r', linestyle='-')
    plt.xlim(0.9, n+0.1)
    plt.xlabel('Índice de la lista')
    plt.ylabel('Valores de la lista')
    plt.title('Gráfico de lista con constante pi')
    plt.show()
    