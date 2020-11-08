meses = ['Enero', 'Febrero','Enero', 'Marzo', 'Abril']


#Aqui recorro el arreglo con su respectivo iten
for i in range(len(meses)):
	print(i, meses[i])


print(":::::::::::::::::::::")
#Aqui recorremos el arreglo solamente con los valores
for mes in meses:
	print(mes)


#Con este metodo sort ordenamos el array

meses.sort()
print(meses)

print(":::::::::::::::::::::")




#Aqui separo como un arreglo la frase con metodo split
mensaje = 'Hola Mundo Con orlAndo orlando ospino ospino'

datos = mensaje.split()

for i in range(len(datos)):
	print(i, datos[i])


print(f"La Vocal A o a repite: {mensaje.count('a')}")

#Modificando valores de un array
meses[2] = 'Mayo'
print(meses)

