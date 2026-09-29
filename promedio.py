#Calcular el promedio de tres notas
nota1 = float(input("Ingrese la nota 2:"))
nota2 = float(input("Ingrese la nota 2:"))
nota3 = float(input("Ingrese la nota 2:"))
promedio = (nota1+nota2+nota3)/3
print(f"Promedio: {promedio:.2f}")

if promedio >= 10.5:
    print ("Condicion: APROBADO")
else:
    print ("Condicion: DESAPROBADO")