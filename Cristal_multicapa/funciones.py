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

    D =  np.array([[1,1],
            [n*np.cos(theta), -n*np.cos(theta)]])

    return D

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


