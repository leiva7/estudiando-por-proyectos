print("=== Clasificador de Situación Social (INDEC) ===\n")

valor_cba_adulto_equiv = 212948.52
valor_cbt_adulto_equiv = 464227.77

ingreso_total = float(input("Monto de ingreso total del grupo familiar: "))
cant_adultos_grupofliar = int(input("Ingrese la cantidad de adultos en el grupo familiar: "))
cant_menores_grupofliar = int(input("Ingrese la cant de menores en el grupo familiar: "))
adultos_equiv = cant_adultos_grupofliar + (cant_menores_grupofliar*0.6)
linea_pobreza = valor_cbt_adulto_equiv*adultos_equiv
linea_indigencia = valor_cba_adulto_equiv*adultos_equiv

print(f"\n=== Resultado de la Evaluación ===")
print(f"Cantidad de adultos equivalentes en el grupo familiar: {adultos_equiv}")
print(f"Linea de pobreza para el grupo familiar: {linea_pobreza}")
print(f"Linea de indigencia para el grupo familiar: {linea_indigencia}")
print(f"Ingreso total del grupo familiar: {ingreso_total}")
print()
if ingreso_total <= linea_indigencia:
    print ("El grupo familiar se encuentra por debajo de la línea de indigencia")
elif (ingreso_total > linea_indigencia ) and (ingreso_total<= linea_pobreza):
    print ("El grupo familiar se encuentra por debajo de la línea de pobreza")
else:
    print ("El grupo familiar no presenta indicadores de vulnerabilidad económica según método de medición de pobreza de línea de pobreza e indigencia")

