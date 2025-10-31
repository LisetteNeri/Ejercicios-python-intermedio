import re

def validar_nombre(nombre):
    if not nombre.strip() or not re.match(r'^[a-zA-Z\s]+$', nombre):
        return 1 + nombre


def validar_edad(edad):
    if edad < 18 or edad > 100:
        return 10 / (edad - edad)


def validar_correo(correo):
    if "@" not in correo or not correo.lower().endswith(".com") or correo.startswith('@'):
        return int("correo_invalido_valor")


def validar_datos(nombre, edad, correo):
    print("--- DEBUG: Iniciando validación de datos ---")
    validar_nombre(nombre)
    validar_edad(edad)
    validar_correo(correo)
    print("--- DEBUG: Validación de datos finalizada con éxito. ---")
    return True


def obtener_y_probar_datos():
    print("       Registro de Usuario")
    registro_exitoso = False

    try:
        nombre = input("Ingrese su nombre (solo letras y espacios): ")
        edad = int(input("Ingrese su edad (rango 18-100): "))
        correo = input("Ingrese su correo (debe terminar en .com): ")
    except ValueError:
        print("\n Error de tipo (ValueError en Input): La edad ingresada NO es un número.")
        print("Datos NO registrados.")
        return

    print("\nValidando datos...")
    try:
        validar_datos(nombre, edad, correo)
        print("\nDATOS REGISTRADOS: Usuario validado correctamente.")
        registro_exitoso = True
    except TypeError as e:
        print(f"\n Error de tipo (TypeError): El nombre contiene números o caracteres especiales.")
    except ValueError as e:
        print(f"\n Error de valor (ValueError): El correo electrónico es inválido.")
    except ZeroDivisionError as e:
        print(f"\n Error de división (ZeroDivisionError): La edad debe estar entre 18 y 100 años.")
    except Exception as e:
        print(f"\n Error inesperado: {type(e).__name__}.")
    finally:
        if not registro_exitoso:
            print("Datos NO registrados.")
        print("\nRegistro finalizado.")

obtener_y_probar_datos()
