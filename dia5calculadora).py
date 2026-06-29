horas = int(input("Horas trabajadas hoy: "))
pago_hora = int(input("¿Cuánto te pagan la hora?: "))
total = horas * pago_hora
print("Ganaste:", total)
horas = input("¿Cuántas horas trabajaste? ")
pago_por_hora = input("¿Cuánto te pagan la hora? ")

if horas.isdigit() and pago_por_hora.isdigit():
    sueldo = int(horas) * int(pago_por_hora)
    print("Tu sueldo es: $", sueldo)
else:
    print("Error: Solo mete números, no letras")