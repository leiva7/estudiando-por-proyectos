nombre = "Franco" 
apellido = "Leiva"
edad = 34
altura_metros = 1.6
es_activa_laboralmente = True
genero = "masculino"
sexo = "m"
ocupacion = "Trabajador social, docente de informática"

nombre_completo = nombre + " " + apellido
anio_nacimiento = 2026-edad


print("=== Datos Personales ===")
print(f"Nombre completo: {nombre_completo}")
print(f"Sexo: {sexo}. Género: {genero}")
print(f"Edad: {edad}")
print(f"Año de nacimiento aprox: {anio_nacimiento}")
print(f"Altura: {altura_metros}")
print(f"Trabaja actualmente: {es_activa_laboralmente}. Ocupaciones: {ocupacion}")

