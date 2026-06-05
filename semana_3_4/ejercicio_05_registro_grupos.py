print("=== Clasificador de Situación Social (INDEC) ===\n")

VALOR_CBA = 212948.52
VALOR_CBT = 464227.77

print("=== Sistema de Registro de Grupos Familiares ===")

cantidad_grupos = int(input("\n¿Cuántos grupos familiares querés registrar? "))

# Variables acumuladoras para estadísticas al final
total_indigentes = 0
total_pobres = 0
total_sobre_linea = 0
suma_ingresos = 0

for i in range(1, cantidad_grupos + 1):
    print(f"\n--- Grupo Familiar {i} ---")
    ingreso = float(input(f"  Ingreso mensual del grupo {i}: $ "))
    adultos_equiv = float(input(f"  Adultos equivalentes del grupo {i}: "))
    
    linea_ind = VALOR_CBA * adultos_equiv
    linea_pob = VALOR_CBT * adultos_equiv
    
    suma_ingresos += ingreso  # Acumulamos para el promedio al final
    
    if ingreso < linea_ind:
        situacion = "INDIGENCIA"
        total_indigentes += 1
    elif ingreso < linea_pob:
        situacion = "POBREZA"
        total_pobres += 1
    else:
        situacion = "SOBRE LÍNEA"
        total_sobre_linea += 1
    
    print(f"Situación del grupo {i}: {situacion}")

# Resumen final
print("\n" + "="*45)
print("RESUMEN ESTADÍSTICO")
print("="*45)
print(f"  Total de grupos registrados: {cantidad_grupos}")
print(f"  En situación de indigencia:  {total_indigentes} ({total_indigentes/cantidad_grupos*100:.1f}%)")
print(f"  Bajo línea de pobreza:       {total_pobres} ({total_pobres/cantidad_grupos*100:.1f}%)")
print(f"  Sobre línea de pobreza:      {total_sobre_linea} ({total_sobre_linea/cantidad_grupos*100:.1f}%)")
print(f"  Ingreso promedio:            ${suma_ingresos/cantidad_grupos:,.2f}")