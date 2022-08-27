# Programa No. 1: area y perimetro circulo


print("---------------------")
print("---AREA-PERIMETRO----")
print("---------------------")

# inpunt
r = input("Digete el valor del radio:")
r = int(r)

# processing
import math
a = math.pi*r*r
p = 2*math.pi*r

#output
print("-------RESULTADOS-------")
print("Area: " + str(a))
print("perimetro: " + str(p))