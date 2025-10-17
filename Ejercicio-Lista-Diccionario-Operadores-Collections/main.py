'''Ejercicio: Sistema de Géstión de Clientes en una Tienda en Línea
Una pequeña empresa de comercio electrónico ha exportado dos reportes en forma
de diccionarios de datos. Uno contiene los nombres de los clientes que han comprado
durante los últimos 30 días, y el otro contiene los nombres de clientes registrados
en su base total. La empresa desea:
• Identificar qué clientes nuevos han comprado sin estar registrados.
• Detectar duplicados en la lista de compras.
• Calcular cuántas veces cada cliente ha comprado.
• Crear un resumen personalizado por cliente, utilizando estructuras eficientes.'''

from collections import Counter, OrderedDict

'''Diccionarios a usar:  '''
# Diccionario {nombre del cliente:veces compradas}; clientes que han hecho compras en los ultimos 30 días
data_compras_dict = { "Luis": 3, "Ana": 2, "Carlos": 2, "Marta": 1, "Sofía": 1, "Elena": 1}

# Diccionario {nombre del cliente:True/False}; el booleano representa si ya está registrado en la base da datos totales
data_registrados_dict = {"Ana": True, "Carlos": True, "Marta": True, "Elena": True, "Javier": True
}


'''1. Filtrar clientes nuevos:
Obtener los nombres que aparecen en “compras”, pero que no están en registrados. '''
diferencia_conjuntos_lambda_dict = lambda x, y: set(x.keys()) - set(y.keys())

def filtrar_clientes_nuevos(compras_dict, registrados_dict):
    return diferencia_conjuntos_lambda_dict(compras_dict, registrados_dict)


'''2. Eliminar duplicados y mantener orden:
Obtén una lista sin repeticiones de compras, conservando el orden en el que llegaron.'''
#Convimos el diccionario de compras en una lista
def preprocesar_datos(compras_dict):
    compras_list = []
    for cliente, veces in compras_dict.items():
        compras_list.extend([cliente] * veces)
    return compras_list

def eliminar_duplicados_ordenados(compras_list):
    return list(OrderedDict.fromkeys(compras_list).keys())


'''3. Contar cuántas veces se repite cada nombre:
Usa collections.Counter para contar cuántas veces aparece cada cliente en la lista de compras.'''
def contar_compras(compras_list):
    return Counter(compras_list)


'''4. Crear un resumen personalizado:
Usando dict comprehension, crea un diccionario que relacione a cada cliente con un mensaje tipo:
"Luis": "Ha comprado 3 veces" Y que hayan comprado más de una vez. '''
crear_mensaje = lambda veces: f"Ha comprado {veces} veces"

def crear_resumen_frecuente(conteo_compras):
    resumen_clientes = {
        cliente: crear_mensaje(veces)
        for cliente, veces in conteo_compras.items()
        if veces > 1
    }
    return resumen_clientes


'''5. Formato final:
Imprime tres bloques:
-Clientes nuevos no registrados.
-Lista de clientes únicos.
-Resumen por cliente frecuente (más de 1 compra).'''
def imprimir_resultados(clientes_nuevos, clientes_unicos, resumen_frecuente):
    #Bloque 1 Clientes nuevos no registrados
    print("\n\nSISTEMA DE GESTIÓN DE CLIENTES EN TIENDA EN LÍNEA")
    print("\n  --Clientes nuevos no registrados--")
    print(f"Total: {len(clientes_nuevos)}")
    print(list(clientes_nuevos))

    #Bloque 2 Lista de clientes unicos
    print("\n \n## Lista de clientes únicos (orden conservado)")
    print(f"Total: {len(clientes_unicos)}")
    print(clientes_unicos)

    #Bloque 3 Resumen de clientes frecuentes
    print("\n \n## Resumen por cliente frecuente (Más de 1 compra)")
    print(f"Total de clientes frecuentes: {len(resumen_frecuente)}")
    for cliente, mensaje in resumen_frecuente.items():
        print(f"  -{cliente}: {mensaje}")

'''Uso de funciones '''
def gestionar_clientes_desde_diccionarios(compras_dict, registrados_dict):
    #PREPROCESAMIENTO: Lista de compras
    compras_list = preprocesar_datos(compras_dict)

    #FILTRADO
    clientes_nuevos = filtrar_clientes_nuevos(compras_dict, registrados_dict)

    #ELIMINAR DUPLICADOS, CONTEO, RESUMEN
    clientes_unicos = eliminar_duplicados_ordenados(compras_list)
    conteo_compras = contar_compras(compras_list)
    resumen_frecuente = crear_resumen_frecuente(conteo_compras)

    #IMPRESIÓN
    imprimir_resultados(clientes_nuevos, clientes_unicos, resumen_frecuente)

    #RETORNO
    return {
        "clientes_nuevos_no_registrados": list(clientes_nuevos),
        "lista_de_clientes_unicos": clientes_unicos,
        "resumen_por_cliente_frecuente": resumen_frecuente
    }

'''Llamada de la funcion principal '''
resultados = gestionar_clientes_desde_diccionarios(data_compras_dict, data_registrados_dict)