#Cual es el numero minimo de elemtnos de la serie 1 + 1/2 + 1/4 + 1/8 + ...para alcanzar un error absoluto dentro de 10^-1?

error = 10**-1
suma = 0
n = 0
while abs(2 - suma) > error:
    suma += 1/(2**n)
    n += 1


