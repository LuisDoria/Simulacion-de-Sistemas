import random
import math

def box_muller_demanda(sem=int):
    pronostico = []
    sem_mitad = int(sem/2)
    for i in range(sem_mitad):
        ui = random.random()
        uj = random.random()
        zi = math.sqrt(-2*math.log(ui))*math.cos(2*math.pi*uj)
        zj = math.sqrt(-2*math.log(ui))*math.sin(2*math.pi*uj)
        di = int(120 + 15 * zi)
        dj = int(120 + 15 * zj)
        pronostico.append(di)
        pronostico.append(dj)
    return pronostico

# Solo se pueden producir 110, 120 o 130 unidades.

def politica_inventarios(L = int, U = int, inv_actual = int, prod_ult = int, demandalist = list):
    nivel_inferior = L
    nivel_superior = U
    produccion_semanal = [prod_ult]
    nivel_inventario_semanal = [inv_actual]
    demanda_actual = demandalist
    inv_proxima_semana = 0
    ultima_produc = 0
    costo_mantener = 0
    costo_cambio = 0
    # Definir ciclo para evaluar política con inventario nivel_inferior y nivel_superior (L, nivel_superior):
    for i in range(len(demanda_actual)-1):
        if nivel_inventario_semanal[i] < nivel_inferior:
            inv_proxima_semana = max(nivel_inventario_semanal[i] - demanda_actual[i] + 130, 0) #Lo que no se pueda vender se asume como venta perdida, no se compromete.
            ultima_produc = 130
            produccion_semanal.append(ultima_produc)
            nivel_inventario_semanal.append(inv_proxima_semana)
            if (nivel_inventario_semanal[i]-demanda_actual[i]+130) > 0:
                costo_mantener += (nivel_inventario_semanal[i]-demanda_actual[i]+130)*30
            if ultima_produc != produccion_semanal[-2]:
                costo_cambio += 3000
        elif nivel_inventario_semanal[i] > nivel_superior:
            inv_proxima_semana = max(nivel_inventario_semanal[i] - demanda_actual[i] + 110, 0)
            ultima_produc = 110
            produccion_semanal.append(ultima_produc)
            nivel_inventario_semanal.append(inv_proxima_semana)
            if (nivel_inventario_semanal[i]-demanda_actual[i]+110) > 0:
                costo_mantener += (nivel_inventario_semanal[i]-demanda_actual[i]+110)*30
            if ultima_produc != produccion_semanal[-2]:
                costo_cambio += 3000
        else:
            inv_proxima_semana = max(nivel_inventario_semanal[i] - demanda_actual[i] + produccion_semanal[i], 0)
            ultima_produc = 120
            produccion_semanal.append(ultima_produc)
            nivel_inventario_semanal.append(inv_proxima_semana)
            if (nivel_inventario_semanal[i]-demanda_actual[i]+produccion_semanal[i]) > 0:
                costo_mantener += (nivel_inventario_semanal[i]-demanda_actual[i]+produccion_semanal[i])*30
            if ultima_produc != produccion_semanal[-2]:
                costo_cambio += 3000
    costo_total = costo_mantener + costo_cambio
    return produccion_semanal, nivel_inventario_semanal, costo_mantener, costo_cambio, costo_total

#op = int(input('Indique el número de semanas en operación (número par): '))

#simul = int(input("Indique el número de simulaciones: "))
U = [30, 40, 50, 60, 70, 80]
costos = {30:0, 40:0, 50:0, 60:0, 70:0, 80:0}
costos_pol = [[], [], [], [], [], []] #lista de listas para guardar media y desviación estándar de cada política

for i in range(500): #se están realizando las 500 iteraciones.
    for inventario_mayor in U:
        demandita = box_muller_demanda(52)
        prod, nivel, mantener, cambio, total = politica_inventarios(30, inventario_mayor, 60, 120, demandita)
        costos[inventario_mayor] += total
        costos_pol[U.index(inventario_mayor)].append(total) #busca la posición de la política en la lista U y en esa misma posición pero en la lista costo_pol agrega el costo total (se agrega en la misma posición por mayor entendimiento).

#Calcular costo promedio por política (media muestral) y agregarlo en una lista en orden.
costos_promedio = []
for i in costos:
    promedio = costos.get(i)/499
    costos_promedio.append(promedio)
    
#Calcular desviación estándar.
desviaciones = []
for i in range(6):
    sumatoria = 0
    media = costos_promedio[i]
    for costo_simulado in costos_pol[i]:
        sumatoria += (costo_simulado - media)**2
    desv_estandar = (sumatoria/499)**0.5
    desviaciones.append(desv_estandar)

#Calcular número de iteraciones necesarias con precisión de 100.
n = []
Z = 2.576 #Valor aproximado de Z alfa medio con una precisión de 100
for i in range(6):
    n_iter = (Z**2)*(desviaciones[i]**2)/(100)**2
    n.append(n_iter)

print("---------------------------------------------------------------------------------")
print("U     Media muestral     Desviación estándar     Número de iteraciones")
for i in range(6):
    print(f"{U[i]}      {costos_promedio[i]:.2f}             {desviaciones[i]:.2f}                {n[i]:.2f}")

#Intervalo de confianza para el ganador (U=30) con un nivel de confianza del 95%.
media = costos_promedio[0]
desv = desviaciones[0]
Z = 1.96
lim_inferior = round(media - Z * (desv/(500)**0.5), 2)
lim_superior = round(media + Z * (desv/(500)**0.5), 2)
print("---------------------------------------------------------------------------------")
print(f"Intervalo de confianza para U = 30 con confianza del 95%: ({lim_inferior:.2f}, {lim_superior:.2f})")