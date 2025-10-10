from functools import reduce
import time
'''---Funciones definidas sin lambda---'''

# Función para FILTER():
def es_alerta_calor(tupla_ciudad_temp):
    return tupla_ciudad_temp[1] >= 30

# Función para SORTED() (Key):
def obtener_temperatura(tupla_ciudad_temp):
    return tupla_ciudad_temp[1]

# Función para MAP() (Transformación):
def formatear_alerta(tupla_ciudad_temp):
    ciudad, temperatura = tupla_ciudad_temp
    return f"Alerta de calor en {ciudad}: {temperatura}°C"

# Función para REDUCE():
def sumar_temperaturas(acumulador, temperatura):
    return acumulador + temperatura


''' --- DECORADOR --- '''
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

''' --- GENERADOR --- '''
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


'''--- DECORADOR CON FUNCIONES INCLUIDAS ---'''

@auditar_funcion
def procesar_alertas(generador):
    # FILTER()
    temperaturas_mayores_30 = list(filter(es_alerta_calor, generador))

    if not temperaturas_mayores_30:
        return [], 0.0

    # SORTED()
    temperaturas_ordenadas = list(sorted(
        temperaturas_mayores_30,
        key=obtener_temperatura,  # Usamos la función obtener_temperatura
        reverse=True
    ))

    # REDUCE():
    temperaturas_solo_valor = list(map(obtener_temperatura, temperaturas_ordenadas))
    suma_temperaturas = reduce(sumar_temperaturas, temperaturas_solo_valor)
    promedio = suma_temperaturas / len(temperaturas_solo_valor)

    # MAP():
    alertas_finales = list(map(
        formatear_alerta,
        temperaturas_ordenadas
    ))
    return alertas_finales, promedio


''' --- SALIDA --- '''

alertas_finales, promedio_final = procesar_alertas(leer_temperaturas())

print("\n Salida Final: ")
for alerta in alertas_finales:
    print(f"  {alerta}")
print(f"\nTemperatura promedio de alertas: {promedio_final:.1f}°C")