from functools import reduce
import time

'''DECORADOR PERSONALIZADO: crea un decorador que imprima el nombre de la funcion 
que se está ejecutando, cuente cuantas veces ha sido llamada y muestre la duracion 
de ejecucion'''
llamadas_contadas = {}


def auditar_funcion(func):
    def wrapper(*args, **kwargs):
        nombre_funcion = func.__name__
        llamadas_contadas[nombre_funcion] = llamadas_contadas.get(nombre_funcion, 0) + 1
        inicio = time.time()

        resultado = func(*args, **kwargs)

        fin = time.time()

        print(f"\n--- Ejecutando función auditada: {nombre_funcion} ---")
        print(f"Llamada #{llamadas_contadas[nombre_funcion]} a {nombre_funcion}")
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
        print("------------------------------------------")

        return resultado

    return wrapper

'''GENERADOR DE DATOS: Crear una función generadora que devuelva, una a una,
tuplas con el formato: ("Ciudad", temperatura)'''

def leer_temperaturas():
    yield ("CDMX", 26)
    yield ("Monterrey", 34)
    yield ("Toluca", 19)
    yield ("Cancún", 38)
    yield ("Veracruz", 32)
    yield ("Puebla", 20)
    yield ("Hermosillo", 40)
    yield ("Guadalajara", 35)
    yield ("Oaxaca", 37)

"""Aplicamos el decorador"""
@auditar_funcion
def procesar_alertas(generador):
    # 1. FILTRADO CON FILTER() Y LAMBDA:
    temperaturas_mayores_30 = list(filter(lambda x: x[1] >= 30, generador))

    if not temperaturas_mayores_30:
        return [], 0.0

    '''ORDENAMIENTO CON SORTED() Y KEY=LAMBDA: 
    Ordena la lista de tuplas POR TEMPERATURA (índice 1) en orden descendente.'''
    temperaturas_ordenadas = list(sorted(
        temperaturas_mayores_30,
        key=lambda x: x[1],
        reverse=True
    ))

    '''RESUMEN CON REDUCE(): Extraer y sumar temperaturas
    Extraemos solo los valores de temperatura de la lista ordenada'''
    temperaturas_solo_valor = list(map(lambda x: x[1], temperaturas_ordenadas))

    suma_temperaturas = reduce(lambda acc, temp: acc + temp, temperaturas_solo_valor)
    promedio = suma_temperaturas / len(temperaturas_solo_valor)

    '''TRANSFORMACIÓN CON MAP() Y LAMBDA: (Se hace al final para preservar el orden)'''
    alertas_finales = list(map(
        lambda x: f"Alerta de calor en {x[0]}: {x[1]}°C",
        temperaturas_ordenadas
    ))

    return alertas_finales, promedio


'''SALIDA: Imprimir la lista ordenada de alertas Y el promedio de temperaturas en formato:
"Temperatura promedio de alertas: 33.5°C '''
alertas_finales, promedio_final = procesar_alertas(leer_temperaturas())

print("\n Salida Final: ")
for alerta in alertas_finales:
    print(f"  {alerta}")
print(f"\nTemperatura promedio de alertas: {promedio_final:.1f}°C")