'''
Optica de multicapa
'''

import numpy as np
import matplotlib.pyplot as plt

from funciones import *
# Unidades en nanómetros

# Definimos los indices de refracción y los anchos de las capas
# Como listas (nota: sumar elementos de una lista los concatena)
n = [3.4] +  [3.6] + [3.4, 3.6] * 15 + [3.4]
d = [0] + [500] + [500, 500] * 15 + [0]

# Este es el parámetro utilizado en el libro
omega = np.linspace(0, 3 * np.pi, 1000)

# Lo pasamos a longitudes de onda que es lo que hemos estado usando
wavelengths = 2 * np.pi / omega * 1000

# Calculamos los coeficientes de reflexión y transmisión
Rss = []
Rpp = []

for wavel in wavelengths:
    Rs, Rp, Ts, Tp = multicapa(n, d, wavel, theta0 = np.pi / 180 * 40)
    Rss.append(Rs)
    Rpp.append(Rp)


plt.figure(figsize=(20,5))
plt.plot(omega, Rss, label='Rs')
plt.plot(omega, Rpp, label='Rp')

plt.legend()
plt.show()