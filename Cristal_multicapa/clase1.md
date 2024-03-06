# Diseño de nuevos materiales

## Optica de multicapa

[Fecha:: 2024/03/04]

Tenemos varios medios con distinto indice de refracción.

Al pasar la luz parte se refleja y parte se transmite. 

Los materiales multicapa son interesantes, son un array de cristales (una serie de capas de distintos indices de refracción).

En cada interfase, parte se refleja y parte se transmite. Finalmente en conjunto parte se refleja y parte se transmite. Jugando con la frecuencia de la onda y los indices de refracción (y los angulos de incidencia). Podemos crear filtros. Así podemos hacer materiales que reflejen y transmitan lo que queramos. (Alberto detallará el viernes aplicaciones)

Hoy vamos a simular una multicapa de estas para ver que hace. Queremos que filtre luz. 

Hacer:



## Método matricial 

(libro: tema 5, )

Se va a usar la ley de snell y la fórmula de Fresnell.

Igual que los problemas de electro 2 de trasmisión en varios medios.

En la interfase tenemos: a izquierda indicente y reflejado, en la siguiente el que se transmite y el reflejado del transmitido en la siguiente interfase.

Tenemos el campo electrico (E exp(i(wt-ki*r))) y H = 1/wmu rotacional de E (igual que en electro 2).

2 situaciones de campo electrico y magnético:

- Onda s: TE (transversal eléctrico) (el electrico va pa fuera si el rayo va para la derecha).

condicion: las fases tienen que ser consecuentes en la interfase (sale ley de snell)

Escribimos el campo eléctrico como suma de las 2 ondas en el medio (la incidente y la reflejada) para cada medio. (escribimos a la izquierda y derecha de la interfase) queremos sacar las condiciones de continuidad:

Aplicamos la continuidad al campo eléctrico y al campo magnético. 

Como vamos a trabajar con medios ópticos mu va a ser similar en todos los materiales.

Al final, la ecuación de la continuidad que nos queda para el campo eléctrico, se puede escribir de forma matricial.

Usando D1 y D2 que son la primera fila 1 y la segunda fila cos ntheta1-n1costheta1 y lo mismo con 2 para el otro medio.


Así podemos sacar las de un medio mediante en función del otro con las matrices: E1 = D1**-1D2 E2

Queremos sacar Rs y Ts (la cantidad emitida y la cantidad propagada). (rs es el  módulo reflejado entre el módulo entrante.) 


Rs = rs**2

Ts = ts**2


Formulas que nos interesan:

$$
(E1, E1') = D1^{-1}D2(E2, E2')
$$


$$

$$

