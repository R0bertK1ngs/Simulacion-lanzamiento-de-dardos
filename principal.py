'''
Tarea APROXIMACIÓN DEL NÚMERO PI
Por: Robert Reyes Mardones
10/04/23
 
'''

from funciones import ingreso_dardos

while True:
    
    print("\nMENU\n")
    print("Elija una de las siguientes opciones: \n")
    print("Opción 1: simulacion con n=9*10^6 y m=50")
    print("Opción 2: Ingresar manuelmente cantidad de dardos(n) y ciclos(m) para la simulacion\n")
    
    opcion = input("Seleccione una opción (1 o 2): ")
    
    if opcion == "1":                            
        print("Ha seleccionado la Opción 1\n")
        n,m=9000000,50
        ingreso_dardos(n,m)
        break
    elif opcion == "2":
        print("Ha seleccionado la Opción 2\n")
        n = int(input("Ingrese cantidad de dardos que desea lanzar: "))
        print("dardos:", n)
        m = int(input("Ingrese cantidad ciclos que desea lanzar: "))
        print("Ciclos:", m)
        ingreso_dardos(n,m)
        break
    else:
        print("\nOpción inválida. Por favor seleccione 1 o 2.")

        
