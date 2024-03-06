'''
Optica de multicapa
'''

import numpy as np
import funciones as fn

n1 = 1.0
n2 = 1.5
theta1 = np.pi/2

theta2 = fn.snell_law(n1, n2, theta1)

D1 = fn.inter(n1, theta1)
D2 = fn.inter(n2, theta2)

D1inv = np.linalg.inv(D1)

dtot = D1inv @ D2

t = 1/dtot[0,0]

r = dtot[1,0]/dtot[0,0]

ta, ra = fn.coef_form(n1, n2, theta1, theta2)

print(f't = {t}, ta = {ta} \n r = {r}, ra = {ra}')

