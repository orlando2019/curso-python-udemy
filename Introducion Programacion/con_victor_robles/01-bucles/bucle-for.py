#Tabla de Multiplicar Ingresando el usuario
print("\t\n###### EJEMPLO DE TABLA DE MULTIPLICAR ######")

numero_usuario = int(input("\t\n¿ Digite un número de cual quiere la tabla: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla de multiplicar del número {numero_usuario}")

for numero in range(1, 11):
    print(f"{numero_usuario} : {numero} = {numero_usuario*numero}")

else:
    print("La Tabla Finalizó")