ingreso_titular = float(input("Ingresá el ingreso del titular del hogar: $ "))
ingreso_secundario = float (input("Ingresá el ingreso de otras personas en el hogar: $ "))

ingreso_total = ingreso_titular+ingreso_secundario

cantidad_personas = int(input("¿Cuántas personas viven en el hogar?"))
ingreso_per_capita = ingreso_total/cantidad_personas

print(f"\n=== Resumen ===")
print(f"Ingreso total del grupo familiar: {ingreso_total:.2f}")
print(f"Ingreso per capita: {ingreso_per_capita:,.2f}")
