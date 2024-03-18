import numpy as np


def snell_law(n1, n2, theta1):
    '''
    Ley de Snell, calcula el angulo de refracción

    n1: refraction index
    n2: refraction index
    theta1: incidence angle

    return theta2: refraction angle    
    '''

    stheta2 = n1*np.sin(theta1)/n2

    return np.arcsin(stheta2)


def inters(n, theta):
    '''
    Calcula la matriz para la interfase.

    n: refraction index
    theta: angle

    return D: matrix
    '''
    cos = np.cos(theta)

    D = np.array([[1, 1],
                  [n*cos, -n*cos]])

    return D

def interp(n, theta):
    '''
    Calcula la matriz para la interfase.

    n: refraction index
    theta: angle

    return D: matrix
    '''
    cos = np.cos(theta)

    D = np.array([[cos, cos],
                  [n, -n]])

    return D

def prop(theta, d, n, wavelenth):
    '''

    '''

    phi = n*2*np.pi/wavelenth*np.cos(theta)*d

    P = np.array([[np.exp(1j*phi), 0],
                  [0, np.exp(-1j*phi)]])
    return P


def coef_form(n1, n2, theta1, theta2):
    '''
    Calcula los coeficientes de transmisión y reflexión

    n1: refraction index
    n2: refraction index
    theta1: incidence angle
    theta2: refraction angle

    return t: transmission coefficient
    return r: reflection coefficient
    '''

    c1 = np.cos(theta1)
    c2 = np.cos(theta2)

    r = (n1*c1 - n2*c2)/(n1*c1 + n2*c2)

    t = 2*n1*c1/(n1*c1 + n2*c2)

    return t, r


def coef_monocapa(n1, n2, n3, d, theta1, theta2, theta3, wavel):
    '''
    '''

    t12, r12 = coef_form(n1, n2, theta1, theta2)

    t23, r23 = coef_form(n2, n3, theta2, theta3)

    phi = n2*2*np.pi*d/wavel*np.cos(theta2)

    t = t12*t23*np.exp(-1j*phi)/(1 + r12*r23*np.exp(-2*1j*phi))
    r = (r12 + r23 * np.exp(-2*1j*phi))/(1 + r12*r23*np.exp(-2*1j*phi))

    return t, r


def coef_TR(t, r, theta0, thetaf, n0, nf):
    '''
    '''

    T = nf/n0*np.abs(t)**2*np.cos(thetaf)/np.cos(theta0)
    R = np.abs(r)**2

    return T, R


def multicapa(n, d, wavel, theta0=0):
    '''
    Calcula los coeficientes de transmisión y reflexión para una multicapa

    nperiods: number of periods
    n refraction index
    d: thickness
    wavel: wavelenth
    ws: weight of the s component
    return T: transmission coefficient
    return R: reflection coefficient
    '''
    theta = [theta0]
    D = [inters(n[0], theta0)]
    Dinv = [np.linalg.inv(D[0])]
    P = [0]
    dtot = Dinv[0]

    for i in range(len(n)-1):
        theta.append(snell_law(n[i], n[i+1], theta[-1]))

        D = inters(n[i+1], theta[i+1])
        Dinv = np.linalg.inv(D)
        P.append(prop(theta[i+1], d[i+1], n[i+1], wavel))
        dtot = dtot @ D @ P[i+1] @ Dinv

    D = inters(n[0], theta[-1])

    dtot = dtot @ D

    t = 1/dtot[0, 0]
    r = dtot[1, 0]/dtot[0, 0]

    Ts, Rs = coef_TR(t, r, theta0, theta[-1],  n[0], n[0])


    D = [interp(n[0], theta0)]
    Dinv = [np.linalg.inv(D[0])]
    dtot = Dinv[0]

    for i in range(len(n)-1):
        theta.append(snell_law(n[i], n[i+1], theta[-1]))

        D = interp(n[i+1], theta[i+1])
        Dinv = np.linalg.inv(D)
        dtot = dtot @ D @ P[i+1] @ Dinv

    D = interp(n[0], theta[-1])

    dtot = dtot @ D

    t = 1/dtot[0, 0]
    r = dtot[1, 0]/dtot[0, 0]

    Tp, Rp = coef_TR(t, r, theta0, theta[-1],  n[0], n[0])



    return Rs, Rp, Ts, Tp

