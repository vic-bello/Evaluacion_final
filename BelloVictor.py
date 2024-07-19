import random
import csv

trabajadores = ["Juan Perez”,”Maria Garcia”,”Carlos Lopez”,”Ana Martinez”,”Pedro Rodriguez”,”Laura Hernandez”,”Miguel Sanchez”,”Isabel Gomez”,”Francisco Diaz”,”Elena Fernandez"]
trabajadores_sueldos =[]
def asignar_sueldos_aleatorio():
    # Generar 10 sueldos aleatorios entre 300 y 2500
    sueldos_aleatorios = [random.randint(300, 2500) for _ in range(10)]
    
 
 
def clasificar_sueldos():
    sueldos_menores_800 = []
    sueldos_entre_800_2000 = []
    sueldos_superior_2000 = []
    pass


def ver_estadisticas():
    pass


def reporte_sueldos(sueldo_aleatorio):
    descuento_salud = 7
    descuento_afp = 12

    salud = sueldo_aleatorio * (descuento_salud/100)
    afp = sueldo_aleatorio * (descuento_afp/100)
    sueldo_liquido = sueldo_aleatorio - salud - afp 
    with open("Reporte_sueldos.csv", "w" ) as archivo_csv:
        pass


def salir_del_programa():
    print("""
Saliendo del programa...
Desarrollado por Victor Bello
Rut 26.504.001-2  """)
    
    
def funcion_principal():
    while True:
        opcion = input("""
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa

Selecciona una opcion: """)
        if opcion == "1":
            asignar_sueldos_aleatorio()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_sueldos()
        elif opcion == "5":
            salir_del_programa()
            break
        else:
            print("Opcion no valida, intentelo nuevamente.")
            
funcion_principal()

# Calculos para reporte de sueldo 
descuento_salud = 7
descuento_afp = 12
