n = int(input("Ingrese cantidad de notas: "))
suma = 0
for i in range(n):
    x = float(input("Ingrese notas: "))
    suma = suma + x
    promedio = suma / n
print ("El promedio es:" ,promedio)
