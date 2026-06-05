# Ejercicio 6: Bucles avanzados - ejercicios típicos de entrevistas técnicas

# --- Parte A: Tabla de multiplicar con bucles anidados ---
print("=== Tabla de Multiplicar ===\n")
for fila in range(1, 11):
    for columna in range(1, 11):
        resultado = fila * columna
        # El formato :3d reserva 3 caracteres de ancho (para alinear la tabla)
        print(f"{resultado:3d}", end=" ")
    print()  # Salto de línea al terminar cada fila

# --- Parte B: FizzBuzz (El ejercicio de entrevista más famoso del mundo) ---
print("\n=== FizzBuzz ===")
print("Para cada número del 1 al 30:")
print("- Si es divisible por 3, imprimí 'Fizz'")
print("- Si es divisible por 5, imprimí 'Buzz'")
print("- Si es divisible por ambos, imprimí 'FizzBuzz'")
print("- Si no, imprimí el número\n")

for numero in range(1, 31):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz", end=" | ")
    elif numero % 3 == 0:
        print("Fizz", end=" | ")
    elif numero % 5 == 0:
        print("Buzz", end=" | ")
    else:
        print(numero, end=" | ")

print()  # Salto de línea al final

# --- Parte C: FizzBuzz INDEC ---
print("\n=== FizzBuzz INDEC ===")
print("Para cada número del 1 al 30:")
print("- Si es divisible por 3, imprimí 'CBT'")
print("- Si es divisible por 5, imprimí 'CBA'")
print("- Si es divisible por ambos, imprimí 'INDEC'")
print("- Si no, imprimí el número\n")

for numero in range(1, 31):
    if numero % 3 == 0 and numero % 5 == 0:
        print("INDEC", end=" | ")
    elif numero % 3 == 0:
        print("CBT", end=" | ")
    elif numero % 5 == 0:
        print("CBA", end=" | ")
    else:
        print(numero, end=" | ")

print()  # Salto de línea al final

# --- TU TURNO ---
# Variante de FizzBuzz para docencia:
# Modificá el ejercicio para que imprima:
#   "CBA" si el número es divisible por 5
#   "CBT" si el número es divisible por 3
#   "INDEC" si es divisible por ambos
#   El número si no es ninguno