def pedir_numero_positivo(mensaje):
    """
    Solicita al usuario un número positivo y no permite continuar hasta obtenerlo.
    Esta función usa un bucle while para garantizar un dato válido.
    """
    while True: 
        try:
            valor = float (input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo")
            else:
                return valor
        except ValueError:
            print("Ingrese un número")

print("=== Sistema de Registro de Ingresos (con validación) ===\n")
ingresos = pedir_numero_positivo("Ingresos familiares mensuales: ")
personas = pedir_numero_positivo("Cantidad de integrantes del grupo familiar: ")
print(f"Grupo familiar compuesto por {personas} personas")
print(f"Ingresos del grupo familiar {ingresos:,.2f}")
print(f"Ingresos por persona= {ingresos/personas:,.2f}")
