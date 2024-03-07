import numpy as np
import matplotlib.pyplot as plt
from funciones import *
from IPython.display import clear_output

class GeneticAlgorithm():
    '''
    Clase para implementar el algoritmo genético para optimizar un cristal multicapa
    '''
    def __init__(self, ciudades, poblationSize=100, mutationRate=0.05, generations=10, stopcriteria = 20, elitism=True, elitePercentage=0.01, tournamentSize=5):
        ''' 
        Ciudades: array con las coordenadas de las ciudades
        poblationSize: tamaño de la población
        mutationRate: probabilidad de mutación
        generations: número de generaciones
        stopcriteria: número de generaciones sin mejora para detener el algoritmo
        elitism: booleano para indicar si se usa elitismo
        elitePercentage: porcentaje de la población que se considera elite
        tournamentSize: tamaño del torneo para la selección
        '''
        self.ciudades = ciudades
        self.N = len(ciudades)
        self.route = list(np.arange(self.N))+[0]

        self.poblationSize = poblationSize
        self.mutationRate = mutationRate
        self.generations = generations
        self.stopcriteria = stopcriteria
        self.elitism = elitism
        self.elitePercentage = elitePercentage
        self.tournamentSize = tournamentSize
        
        self.distanceMatrix = self.dist_matrix() 
        self.distanciaTotal = self.totalDistance(range(self.N))

        self.poblation = np.random.permutation([[0]+list(np.random.permutation(range(1,self.N)))+[0] for _ in range(self.poblationSize)])
        self.fitness = np.array([self.getFitness(i) for i in self.poblation])
        self.bestRoute = self.poblation[np.argmax(self.fitness)]

        self.distances = []
    def dist_matrix(self):
        '''
        Función para calcular la matriz de distancias
        '''
        d = np.zeros((self.N,self.N))
        for i in range(self.N):
            for j in range(self.N):
                d[i][j] = np.linalg.norm(self.ciudades[i]-self.ciudades[j])
        return d
    
    def totalDistance(self, route):
        '''
        Función para calcular la distancia total de una ruta.
        '''
        return np.sum(self.distanceMatrix[route,np.roll(route,-1)])
    
    def getFitness(self, individuo):
        return self.totalDistance(individuo)**-1
    
    def mutation(self, indiviudo):
        '''
        Función para mutar un individuo
        '''
        new_route = indiviudo.copy()

        # Elegimos uno de los dos métodos de mutación
        # de forma aleatoria
        method = np.random.choice(['swap','inverse'])

        # Seleccionamos el trozo a mutar
        i,j = np.random.randint(1,self.N,2)
        while j==i:
            j = np.random.randint(1,self.N)

        # Generamos la nueva ruta con un swap aleatorio:
        if method == 'swap':
            new_route[i],new_route[j] = new_route[j],new_route[i]
        
        # Generamos la nueva ruta con un inverse aleatorio:
        if method == 'inverse':
            if i>j:
                i,j = j,i
            new_route[i:j+1] = new_route[i:j+1][::-1]
        
        return new_route

    def plotRoute(self):
        '''
        Función para mostrar la ruta
        '''

        plt.figure(figsize=(15,15))
        plt.subplot(2,2,1)
        plt.plot(self.ciudades[self.route,0],self.ciudades[self.route,1],'o-')
        plt.title(f'Distancia total = {self.distanciaTotal:.2f}')
        plt.xlabel('x')
        plt.ylabel('y')
        for i in range(self.N):
            plt.text(self.ciudades[i][0]*1.01, self.ciudades[i][1], i, fontsize=10)
        
        plt.subplot(2,2,2)
        plt.plot(self.distances)
        plt.title('Distancia total')
        plt.xlabel('Generación')
        plt.ylabel('Distancia total')
        

        plt.subplot(2,2,3)
        plt.hist(self.fitness, bins=20)
        plt.title('Fitness')

        plt.subplot(2,2,4)
        plt.loglog(self.distances)
        plt.title('Distancia total')
        plt.xlabel('Generación')
        plt.ylabel('Distancia total')
        plt.show()
    
    def getElite(self):
        '''
        Función para obtener la elite de la población
        '''
        n = int(self.poblationSize*self.elitePercentage)
        return self.poblation[np.argsort(self.fitness)[-n:]]

    def tournamentSelection(self):
        '''
        Función para seleccionar un individuo mediante torneo
        '''
        selection = np.random.choice(self.poblationSize, self.tournamentSize, replace=False, p=self.fitness/self.fitness.sum())
        return selection[np.argmax(self.fitness[selection])]
    
    def crossover(self, parent1, parent2):
        '''
        Función para cruzar dos individuos
        '''
        child = parent1.copy()
        inx = [0,0]
        while inx[0] == inx[1]:
            inx = np.random.randint(1,self.N-1,2)
        inx.sort()
        i, j = inx   
        chromosomeP1 = parent1[i:j]
        
        chromosomeP2 = [i for i in parent2 if i not in chromosomeP1]
        
        child = -1*np.ones(self.N+1)
        child[i:j] = chromosomeP1
        # Conseguimos los índices de los -1
        inx = np.where(child==-1)[0]
        # Rellenamos los -1 con los valores de chromosomeP2
        child[inx] = chromosomeP2
        child = child.astype(int) # Lo ponemos como enteros los valores porque antes eran floats

        return child
    
    def nextGeneration(self):
        '''
        Función para generar la siguiente generación
        '''
        newPoblation = []

        # Si se usa elitismo, añadimos la elite a la nueva población
        if self.elitism:
            newPoblation.extend(self.getElite())

        # El resto de la población la generamos mediante cruces
        while len(newPoblation) < self.poblationSize:
            # Seleccionamos dos padres mediante torneo distintos
            parent1 = self.poblation[self.tournamentSelection()]
            parent2 = parent1
            while np.array_equal(parent1,parent2):
                parent2 = self.poblation[self.tournamentSelection()]
            # Cruzamos los padres para obtener un hijo
            child = self.crossover(parent1,parent2)
            # Mutamos el hijo con una probabilidad mutationRate
            if np.random.random() < self.mutationRate:
                child = self.mutation(child)
            newPoblation.append(child)

        # Actualizamos las variables
        self.poblation = np.array(newPoblation)
        self.fitness = np.array([self.getFitness(i) for i in self.poblation])
        self.bestRoute = self.poblation[np.argmax(self.fitness)]
        # Devolvemos los índices de las ciudades de la mejor ruta
        self.route = self.bestRoute
        self.distanciaTotal = self.totalDistance(self.bestRoute)
        

    def run(self):
        '''
        Función para ejecutar el algoritmo genético
        '''
        # vamos a añadir un stopcriteria para que se detenga cuando 
        #la distancia total no mejore

        self.distances.append(self.distanciaTotal)
        c = 0
        for i in range(self.generations):
            self.nextGeneration()
            clear_output(wait=True)
            print(f'Generación {i+1}/{self.generations}')
            print(f'Distancia total = {self.distanciaTotal:.2f}')
            if self.distances[-1] == self.distanciaTotal:
                c+=1
            self.distances.append(self.distanciaTotal)
            if c == self.stopcriteria:
                break
        self.plotRoute()
        plt.show()

    def graficRun(self):
        '''
        Función para ejecutar el algoritmo genético
        mostrando la gráfica de la ruta en cada generación
        '''
        self.distances.append(self.distanciaTotal)
        c = 0
        for i in range(self.generations):
            self.nextGeneration()
            clear_output(wait=True)
            print(f'Generación {i+1}/{self.generations}')
            print(f'Distancia total = {self.distanciaTotal:.2f}')
            
            if self.distances[-1] == self.distanciaTotal:
                c+=1
            else:
                c = 0

            self.distances.append(self.distanciaTotal)

            self.plotRoute()
            plt.show()
            if c == self.stopcriteria:
                break