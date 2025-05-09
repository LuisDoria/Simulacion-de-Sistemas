import random

posibilidades = ["CCC", "CCS","CSC", "CSS", "SCC", "SCS", "SSC", "SSS"] #Distintas posibilidades de tripletas

n = int(input("Ingrese el número de simulaciones: "))

def simulacionTripletax(a = str, b = str, c = str, simulaciones = int):

  numLanz = [] #Aquí se almacena el número de lanzamientos requeridos para ganar cada ronda

  for i in range(simulaciones):

    listaTripletax = [] #Aquí se van a ir almacenando cada uno de los lanzamientos
    lanzamientos = 0 #Contador pa agregarlo a la lista anterior, por cada ronda

    while listaTripletax[-3:] != [a, b, c]: #revisa si los últimos 3 elementos agregados son iguales a la tripleta abc
      numero = random.random()
      lanzamientos += 1
      if numero <= 0.5:
        listaTripletax.append("C") #Si el número aleatorio es menor o igual a 0.5, se enlista como cara (C)
      else:
        listaTripletax.append("S") #Si el número aleatorio es mayor a 0.5, se enlista como sello (S)

    numLanz.append(lanzamientos) #Cuando ya no se cumple el while, quiere decir que ya salió la tripleta y por ende se tiene el número de lanzamientos necesarios

  promedio_lanzamientos = sum(numLanz)/len(numLanz) #Para hallar el promedio de lanzamientos en TODAS las simulaciones de la tripleta abc

  return numLanz, promedio_lanzamientos

resultadosCCC, promedioCCC = simulacionTripletax("C","C","C", n)
#print(f"Número de lanzamientos requeridos para que salga la tripleta CCC en las {n} simulaciones: {resultadosCCC}")
print(f"Promedio de lanzamientos para obtener CCC en {n} rondas: {promedioCCC}")

resultadosCCS, promedioCCS = simulacionTripletax("C","C","S", n)
#print(f"Número de lanzamientos requeridos para que salga la tripleta CCS en las {n} simulaciones: {resultadosCCS}")
print(f"Promedio de lanzamientos para obtener CCS en {n} rondas: {promedioCCS}")

resultadosCSC, promedioCSC = simulacionTripletax("C","S","C", n)
#print(f"Número de lanzamientos requeridos para que salga la tripleta CSC en las {n} simulaciones: {resultadosCSC}")
print(f"Promedio de lanzamientos para obtener CSC en {n} rondas: {promedioCSC}")

resultadosCSS, promedioCSS = simulacionTripletax("C","S","S", n)
#print(f"Número de lanzamientos requeridos para que salga la tripleta CSS en las {n} simulaciones: {resultadosCSS}")
print(f"Promedio de lanzamientos para obtener CSS en {n} rondas: {promedioCSS}")

resultadosSCC, promedioSCC = simulacionTripletax("S","C","C", n)
#print(f"Número de lanzamientos requeridos para que salga la tripleta SCC en las {n} simulaciones: {resultadosSCC}")
print(f"Promedio de lanzamientos para obtener SCC en {n} rondas: {promedioSCC}")

resultadosSCS, promedioSCS = simulacionTripletax("S","C","S", n)
#print(f"Número de lanzamientos requeridos para que salga la tripleta SCC en las {n} simulaciones: {resultadosSCS}")
print(f"Promedio de lanzamientos para obtener SCS en {n} rondas: {promedioSCS}")

resultadosSSC, promedioSSC = simulacionTripletax("S","S","C", n)
#print(f"Número de lanzamientos requeridos para que salga la tripleta SSC en las {n} simulaciones: {resultadosSSC}")
print(f"Promedio de lanzamientos para obtener SSC en {n} rondas: {promedioSSC}")

resultadosSSS, promedioSSS = simulacionTripletax("S","S","S", n)
#print(f"Número de lanzamientos requeridos para que salga la tripleta SSS en las {n} simulaciones: {resultadosSSS}")
print(f"Promedio de lanzamientos para obtener SSS en {n} rondas: {promedioSSS}")

import matplotlib.pyplot as plt

#Diagrama de barras del promedio para obtener cada tripleta:

promedios = [promedioCCC, promedioCCS, promedioCSC, promedioCSS, promedioSCC, promedioSCS, promedioSSC, promedioSSS]

plt.bar(posibilidades, promedios)
plt.xlabel("Tripleta")
plt.ylabel("Promedio de lanzamientos")
plt.title("Promedio de lanzamientos para obtener cada tripleta")
plt.show()