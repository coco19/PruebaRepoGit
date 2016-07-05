#!/usr/bin/python
# encoding: utf-8

for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'es igual a', x, '*', n/x
            break
        else:
            print n, 'es un numero primo'
            
a = ['gato','persona','auto']
for i in a:
    print i, a, len(a)
print '\n'
for x in a:#[:]:
    b = a[2:]
    print b
    if len(x)>5: a.insert(0, x)
    print x, a