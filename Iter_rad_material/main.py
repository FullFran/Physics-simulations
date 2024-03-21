import numpy as np
import matplotlib.pyplot as plt

from unfoton import *

thetamax = np.pi/4
dist_fm = 2
rho_mu = 0.1 # coeficiente de atenuación másico

costheta, phi = direccion_emision(thetamax)

x, y, z = coordenadas_incidencia(costheta, phi, dist_fm)

l_mod = atenuacion(1, rho_mu)

costhetan = costheta
phin = phi

xn ,yn ,zn =  coordenadas_material(x, y, z, costheta, phi, costhetan, phin, l_mod)

