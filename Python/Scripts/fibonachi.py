#!/usr/bin/python
# encoding: utf-8
#canción las expresiones a la derecha son evaluadas antes que la asignacion, las expresiones a la derecha de la asignacion se evaluan de izquierda a derecha
#cualquier entero distinto de 0 es verdadero, 0 es falso
a,b = 0,1
while b<10:
    print b, # la coma al final evita el salto de línea
    a,b = b,a+b

#cualquier cosa con longitud distinta de cero es verdadera
print "\n"
c = "hola"
while c:
    print c,
    c = c[:len(c)-1]
l = ['hola', 123, [1,2], 'chau']
print "\n"
while l:
    for i in l: # la sentencia for de python itera sobre los elementos de cualquier secuencia
                # modificar las secuencias sobre las que se esta iterando solo es posible para tipos de secuencias mutables como las listas
        print i,
    l = l[:len(l)-1]
print "\n"

#Para ejecutar la siguiente línea es necesario ejecutar el script desde terminal

#a = int(raw_input("Ingresa un numero y te lo mostrare sumandole 4 \n"))
#print "el resultado es", a+4

d=range(5) # la función range() genera una lista conteniendo progresiones aritméticas, se puede expresar un incremento diferente modificando el paso
print d

f=range(0,9,2)
print f
