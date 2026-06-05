# Ejercicio 6: Bucles avanzados - ejercicios típicos de entrevistas técnicas

# --- Parte A: Tabla de multiplicar con bucles anidados ---
print("=== Tabla de Multiplicar ===\n")
for i in range (1,11):
    for b in range (1,11):
        print(i*b)
    

# --- Parte B: FizzBuzz (El ejercicio de entrevista más famoso del mundo) ---

print("\n=== FizzBuzz ===")
print("Para cada número del 1 al 30:")
print("- Si es divisible por 3, imprimí 'Fizz'")
print("- Si es divisible por 5, imprimí 'Buzz'")
print("- Si es divisible por ambos, imprimí 'FizzBuzz'")
print("- Si no, imprimí el número\n")

for i in range (1,31):
    if (i%3) == 0 and (i%5) != 0:
        print("Fizz")
    elif (i%5) == 0 and (i%3) != 0:
        print("Buzz")
    elif (i%3) == 0 and (i%5) == 0 :
        print ("FizzBuzz")
    else:
        print (i)
#Puede mejorarse poniendo la condición más compleja primero, para que luego en elif evalúe lo que no cumplió la doble condición