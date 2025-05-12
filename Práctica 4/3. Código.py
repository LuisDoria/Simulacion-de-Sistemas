import random
import math
import matplotlib.pyplot as plt
import numpy as np
import sympy

# Actividad 1. Aceptación - Rechazo

def Acept_Recha(N): #dadas N observaciones requeridas
    rechazados = []
    aceptados = []
    rech = 0
    while len(aceptados)<N:
        r1 = random.random() #Se genera un par de números, uno pa evaluar y otro pa comparar.
        r2 = random.random()
        x = 0 + (1*r1)
        gx = (20*x*(1-x)**3)/2.109375
        if r2 <= gx:
            aceptados.append(x)
        else:
            rechazados.append(x)
    return rechazados, aceptados

N = int(input("Ingrese el número de observaciones: "))
rech, acept= Acept_Recha(N)
print("---------------------------------------------------------------------------------------------")
print('**Actividad 1:**')
print(f'Requeridas {N} observaciones, se rechazaron {len(rech)}, en el proceso se rechazan en promedio {len(rech)/N}')
print("---------------------------------------------------------------------------------------------")

#Hacer un histograma con la cantidad de valores aceptados y comparar con la función
#Aplicando la regla de Sturges para separar en los intervalos adecuados los datos
bins_ = math.ceil(1 + (1.442 * math.log(len(acept))))
fig, ax = plt.subplots(1,2, figsize=(10,3))
ax[0].hist(acept, bins = bins_)
ax[0].set_title('Histograma de valores')
ax[0].set_xlabel('Valores')
ax[0].set_ylabel('Frecuencia')
x_valores = np.linspace(0,1,100) #Definiendo los valores que tomarían las x en la función (de 0 a 1, 100 valores distintos)
y = [20*x*(1-x)**3 for x in x_valores] #Evalúa la función con los valores de definidos de x.
ax[1].plot(x_valores, y)
ax[1].set_title('$f(x)=20x*(1-x)^3$')
ax[1].set_xlabel('x')
ax[1].set_ylabel('f(x)')
plt.tight_layout() #Para ajustar automáticamente el espacio entre los subplots

#-------------------------------------------------------------------------------------------------------------------------------
#Actividad 2: Integración con Monte Carlo
print('**Actividad 2:**')

def integral_montecarlo(N_i, a, b, c):
    duplas = []
    aceptados_x = []
    rechazados_x = []
    aceptados_y = []
    rechazados_y = []
    z = 1.96

    for i in range(N_i):
        r1 = random.random()
        r2 = random.random()
        duplas.append((r1, r2))
    
    for i in duplas:
        xi = a + i[0]*(b-a)
        gsin = math.sin(math.pi * xi)**2
        if gsin > (c * i[1]):
            aceptados_x.append(i[0])
            aceptados_y.append(i[1])
        else:
            rechazados_x.append(i[0])
            rechazados_y.append(i[1])

    NH = len(aceptados_x)/N_i
    theta = c * (b-a)*(NH)
    inf = theta - z * (b-a)*math.sqrt((NH*(1-NH))/N_i)
    sup = theta + z * (b-a)*math.sqrt((NH*(1-NH))/N_i)

    return aceptados_x, rechazados_x, aceptados_y, rechazados_y, theta, inf, sup

N_i = N

#Graficando el scatter.
acepX, rechX, acepY, rechY, theta, inf, sup = integral_montecarlo(N_i,0,1,1)
fig, ax = plt.subplots(1,2, figsize=(10, 3))
ax[0].scatter(acepX, acepY, color='blue', s=1, label='Aceptados')
ax[0].scatter(rechX, rechY, color='lightcoral', s=1, label='Rechazados')
ax[0].set_title('Diagrama de dispersión')
ax[0].set_xlabel('r1')
ax[0].set_ylabel('r2')
ax[0].legend()

valores = np.linspace(0,1,100) #Definiendo los valores que tomarían las x en la función (de 0 a 1, 100 valores distintos)
ysin = [math.sin(math.pi*x)**2 for x in valores] #Evalúa la función con los valores de definidos de x.
ax[1].plot(valores, ysin)
ax[1].set_title('$f(x)=\\sin^2(\\pi x)$')
ax[1].set_xlabel('x')
ax[1].set_ylabel('f(x)')
plt.tight_layout() #Para ajustar automáticamente el espacio entre los subplots

print(f'El intervalo de confianza al 95% con el método Montecarlo es: [{inf}, {sup}]')

x = sympy.Symbol('x')
f_sym = sympy.sin(sympy.pi * x)**2
integral_sym = float(sympy.integrate(f_sym, (x, 0, 1)))

print("")
print('El valor de la integral según cada método sería:\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
print('Método           Valor')
print("---------------------")
print(f'Montecarlo       {theta:.2f} ')
print(f'Sympy            {integral_sym:.2f}\n')

print('Abajo se ven las gráficas de las actividades:\n')