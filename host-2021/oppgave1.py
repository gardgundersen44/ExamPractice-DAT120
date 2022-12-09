# Regner ut arealet til en elipse
import math

lengde_1 = float(input("Oppgi lengde a: "))
lengde_2 = float(input("Oppgi lengde b: "))

def areal_ellipse(a,b):
    areal = math.pi * lengde_1 * lengde_2
    return print(f"Arealet til elippsen er: {areal:1.2f} kvadratenheter")

areal_ellipse(lengde_1, lengde_2)




