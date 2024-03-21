import numpy as np
import matplotlib.pyplot as plt

# tenemos que generar phi entre 0 y 2pi y theta entre 0 y pi
# la distribución de probabilidad de theta es p(theta) = 1/2sin(theta)
# la distribución de probabilidad de phi es uniforme entre 0 y 2pi

def costheta(n, maxtheta=np.pi/4):
    a = 1 - np.cos(maxtheta)
    return (1-a*np.random.rand(n))


def phi(n):
    return 2*np.pi*np.random.rand(n)

# la fuente está situada a una distancia d, e intersecciona con un plano.
# las coordenadas en el plano son (x,y) = (d*tan(theta)*cos(phi), d*tan(theta)*sin(phi))


def coordenadas(costheta, phi, d=1):
    '''
    Coordenadas de incidencia de un fotón en un plano situado a una distancia d de la fuente.

    costheta: coseno del ángulo de incidencia
    phi: ángulo de incidencia
    d: distancia de la fuente al plano
    '''

    sentheta = np.sqrt(1-costheta**2)
    tantheta = sentheta/costheta
    x = d*tantheta*np.cos(phi)
    y = d*tantheta*np.sin(phi)
    return x, y


def simulacion(Nphoto, dm, df):
    ''' 
    Simulación de Nphoto fotones que salen de una fuente situada a una distancia dm y llegan a un detector situado a una distancia df
    e interseccionan con dos planos, uno perteneciente al material y otro 
    donde son detectados.

    Nphoto: numero de fotones
    dm: distancia de la fuente al material
    df : distancia de la fuente al detector 
    '''
    costhetas = costheta(Nphoto)
    phis = phi(Nphoto)
    xm, ym = coordenadas(costhetas, phis, dm)
    xf, yf = coordenadas(costhetas, phis, df)

    return xm, ym, xf, yf

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


def absorcion(costheta, phi, d, l, a):
    '''
    Comprueba si un fotón que incide con un cierto ángulo en un material de
    espesor l y coeficiente de atenuación a, es absorbido o no.
    Devuelve True si el fotón es absorbido y False si no lo es.

    theta: incidence angle
    phi: incence angle
    d : distance to the material
    l: material tickness
    a: absortion coefficient 
    '''

    xi, yi = coordenadas(costheta, phi, d)
    xs, ys = coordenadas(costheta, phi, d+l)

    # calculamos el modulo de la distancia para 'salir' del material
    dsalida = np.sqrt((xi-xs)**2 + (yi-ys)**2 + l**2)

    # calculamos la atenuación
    drecorre = atenuacion(1, a)

    if dsalida < drecorre:
        return False, False
    
    return True, drecorre


def simate(Nphoto, dm, l, df, a):
    ''' 
    Simulación de Nphoto fotones que salen de una fuente situada a una distancia dm y llegan a un detector situado a una distancia df
    e interseccionan con dos planos, uno perteneciente al material y otro
    donde son detectados. Además, se tiene en cuenta la atenuación del material, por lo 
    que algunos fotones son absorbidos por este y no son detectados.

    Nphoto: numero de fotones
    dm: distancia de la fuente al material
    l: espesor del material
    df : distancia de la fuente al detector

    a: coeficiente de atenuación
    '''
    costhetas = costheta(Nphoto)
    phis = phi(Nphoto)

    passindex = []    

    for i in range(Nphoto):
        
        if not absorcion(costhetas[i], phis[i], dm, l, a)[0]:
            passindex.append(i)

    # ahora vamos a guardar en una lista los puntos que han pasado 
    costhetapass = costhetas[passindex]
    phispass = phis[passindex]


    xi, yi = coordenadas(costhetas, phis, dm)
    xf, yf = coordenadas(costhetapass, phispass, df)    

    return xi, yi, xf, yf


def colimado(Nphoto, dm, l, a):
    ''' 
    Simulación de la atenuación de un material con coeficiente de atenuación a, el cual sigue una distribución exponencial. Nos devuelve
    la distancia que recorre el fotón antes de ser absorbido.
    Con incidencia normal, nos devuelve la fracción de fotones que pasan a través del material.

    Nphoto: numero de fotones
    dm: distancia de la fuente al material
    l: espesor del material
    df : distancia de la fuente al detector

    a: coeficiente de atenuación
    '''
    costhetas = np.ones(Nphoto)
    phis = np.zeros(Nphoto)

    pasindex = []    

    for i in range(Nphoto):
        
        if not absorcion(costhetas[i], phis[i], dm, l, a)[0]:
            pasindex.append(i)

    return len(pasindex)/Nphoto


def distribucion(dm, lmin, lmax, a, points=100, Nphoto=1000, modo='colimado'):
    '''
    Simulación de la atenuación de un material con coeficiente de atenuación a, nos devuelve la fracción de fotones que pasan a través del material.
    Se puede elegir entre incidencia normal o no.
    Nos devuelve la fracción de fotones que son detectados en función del espesor del material l.

    dm: distancia de la fuente al material
    lmin: espesor mínimo del material
    lmax: espesor máximo del material
    a: coeficiente de atenuación
    points: número de puntos en los que se divide el intervalo [lmin, lmax]
    Nphoto: numero de fotones
    modo: 'colimado' o 'no colimado'
    '''


    l = np.linspace(lmin, lmax, points)
    I = []

    if modo !='colimado':
        for i in l:
            xi, yi, xf, yf = simate(Nphoto, dm, i, 10, a)
            I.append(len(xf)/Nphoto)
        return l, I

    for i in l:
        I.append(colimado(Nphoto, dm, i, a))
    return l, I

########################################################################
# Añadiendo procesos a la simulción: efecto fotoeléctrico, raileight y crompton
########################################################################

def fotoelectrico(costhetafoto, phifoto, z, E=1):

    pass

def raileight(cosraleight, phiraileight, z, E=1):
    '''
    
    ''' 
    cosr = costheta(1)
    phir = phi(1)

    return cosr, phir


def comtom(costhetacom, phicom, E=1):
    pass

def pares(costhetap, phip, E=1):
    pass

def interaccion(costheta, phi, z, prob, E=1):
    '''
    '''
    inter = np.random.choice([fotoelectrico, raileight, comtom, pares], p=prob)

    return inter(costheta, phi, z ,E )

def simulation(Nphoto, dm, l, df, a):
    ''' 
    Simulación de Nphoto fotones que salen de una fuente situada a una distancia dm y llegan a un detector situado a una distancia df
    e interseccionan con dos planos, uno perteneciente al material y otro
    donde son detectados. Además, se tiene en cuenta la atenuación del material, por lo 
    que algunos fotones son absorbidos por este y no son detectados.

    Nphoto: numero de fotones
    dm: distancia de la fuente al material
    l: espesor del material
    df : distancia de la fuente al detector

    a: coeficiente de atenuación
    prob = [fotoelectrico, raileight, compton, pares]

    '''
    prob = [0.0, 1, 0.0, 0.0]


    costhetas = costheta(Nphoto)
    phis = phi(Nphoto)

    passindex = []
    interationindex = []    
    zinter = []


    for i in range(Nphoto):
        pasa, z = absorcion(costhetas[i], phis[i], dm, l, a)
        if not pasa:
            passindex.append(i)
            continue
        
        interationindex.append(i)
        zinter.append(z)
    
    # ahora vamos a guardar en una lista los puntos que han pasado 
    costhetapass = costhetas[passindex]
    phispass = phis[passindex]

    # ahora vamos a guardar en una lista los puntos que han interactuado
    costhetainter = costhetas[interationindex]
    phisinter = phis[interationindex]

    xentrada, yentrada = coordenadas(costhetas, phis, dm+zinter)

    xinter, yinter = [], []

    for i in range(len(costhetainter)):
        if interaccion(costhetainter[i], phisinter[i], zinter[i], prob)[0] is not None:
            cosnuevo, phinuevo = interaccion(costhetainter[i], phisinter[i], zinter[i], prob)
            
            x, y = coordenadas(cosnuevo, phinuevo, dm+zinter[i])
            
            xinter.append(x)
            yinter.append(y)

    

    xi, yi = coordenadas(costhetas, phis, dm)
    xf, yf = coordenadas(costhetapass, phispass, df)    
    xf = np.append(xf, xinter)
    yf = np.append(yf, yinter)
    return xi, yi, xf, yf


