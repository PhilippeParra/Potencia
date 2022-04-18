"""Programa para calcular la potencia
X ^ Y"""

print("........................................................")
print("....................POTENCIA: X ^ Y.....................")
print("........................................................")

#input
X = input("Digite el valor de X: ")
X = int(X)
Y = input("Digite el valor de Y: ")
Y = int(Y)

#processing
Z = X ** Y

#output
print(str(X) + " elevado a la " + str(Y) + " es igual a " + str(Z))