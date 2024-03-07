'''
Optica de multicapa
'''

import numpy as np
import funciones as fn

# Unidades en nanómetros

n1 = 1.0
n2 = 1.5
n3 = 1.0
d = 100.0
wavel = 440


theta1 = np.pi/2

theta2 = fn.snell_law(n1, n2, theta1)

theta3 = fn.snell_law(n2, n3, theta2)

D1 = fn.inter(n1, theta1)
D2 = fn.inter(n2, theta2)
D3 = fn.inter(n3, theta3)

D1inv = np.linalg.inv(D1)
D2inv = np.linalg.inv(D2)
P2 = fn.prop(n2, d, theta2, wavel)

dtot = D1inv @ D2 @ P2 @ D2inv @ D3

t = 1/dtot[0,0]
r = dtot[1,0]/dtot[0,0]

ta, ra = fn.coef_monocapa(n1, n2, n3, d, theta1, theta2, theta3, wavel)

print(f't = {t}, ta = {ta} \n r = {r}, ra = {ra}')

def multicapaperiodo(nperiods, n0, n1, n2, d1, d2, wavel):
    
    n = [n0] + [n1, n2]*nperiods + [n0]
    d = [0] + [d1, d2]*nperiods + [0]

    theta0 = np.pi/180 * 15
    theta = [theta0]
    D = [fn.inter(n0, theta0)]
    Dinv = [np.linalg.inv(D[0])]
    P = [0]
    dtot = Dinv[0]

    for i in range(len(n)-1):
        theta.append(fn.snell_law(n[i], n[i+1], theta[-1]))

        D = fn.inter(n[i+1], theta[i+1])
        Dinv =np.linalg.inv(D)
        P = fn.prop(theta[i+1], d[i+1], n[i+1], wavel)
        dtot = dtot @ D @ P @ Dinv


    D = fn.inter(n0, theta[-1])

    dtot = dtot @ D

    t = 1/dtot[0,0]
    r = dtot[1,0]/dtot[0,0]



    T, R = fn.coef_TR(t,r, theta0, theta[-1],  n0, n0)

    return T, R

T, R = multicapaperiodo(10, n1, n2, n3, d, d, wavel)

print(f'T = {T}, R = {R}')