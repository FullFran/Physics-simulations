import numpy as np
import matplotlib.pyplot as plt


def costheta(n, maxtheta=np.pi/4):
    a = 1 - np.cos(maxtheta)
    return (1-a*np.random.rand(n))


def phi(n):
    return 2*np.pi*np.random.rand(n)


def direccion_emision(maxtheta):
    
    cosemision = costheta(1, maxtheta)
    phiemision = phi(1)

    return cosemision, phiemision



def coordenadas_incidencia(costheta, phi, dis_fm):
    '''
    Coordenadas de incidencia de un fotón en un plano situado a una distancia d de la fuente.

    costheta: coseno del ángulo de incidencia
    phi: ángulo de incidencia
    d: distancia de la fuente al plano
    '''
    sentheta = np.sqrt(1-costheta**2)
    tantheta = sentheta/costheta

    z = dis_fm
    x = z*tantheta*np.cos(phi)
    y = z*tantheta*np.sin(phi)
    
    return x, y, z

def atenuacion(n, a):
    '''
    Simulación de la atenuación de n fotones en un material con coeficiente 
    de atenuación a, el cual sigue una distribución exponencial. Nos devuelve
    la distancia que recorre el fotón antes de ser absorbido.

    n: numero de fotones
    a: coeficiente de atenuación
    '''
    x = -1 / a * np.log(np.random.rand(n))

    return x

def coordenadas_material(xo, yo, zo, costheto, phio, costhetan, phi, l_mod):
    
    sentheta = np.sqrt(1-costheto**2)
    zn = zo + l_mod * costheto
    xn = xo + l_mod * sentheta * np.cos(phio)
    yn = yo + l_mod * sentheta * np.sin(phio)

    return xn, yn, zn





