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


def inter(n, theta):
    '''
    Calcula la matriz para la interfase.

    n: refraction index
    theta: angle

    return D: matrix
    '''

    D = np.array([[1, 1],
                  [n*np.cos(theta), -n*np.cos(theta)]])

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


