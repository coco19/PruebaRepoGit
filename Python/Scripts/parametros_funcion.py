#!/usr/bin/python
# encoding: utf-8
a=8
def funcion(p=a):
    """
    funcion para demostrar que los argumentos por omisión de una función son evaluados 
    en la definición de la función
    """
    print p

a=9
funcion()