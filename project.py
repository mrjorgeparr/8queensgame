import matplotlib.pyplot as plt


import math


K = {15000}
C = {1700}
values = []
for k in K:
    for c in C:
        print(f"valor (k,c) = {k,c}")
        csq = pow(c,2)
        val1 = (-c + math.sqrt(pow(c,2) - 4*46*k))/(92)
        val2 = (-c - math.sqrt(pow(c, 2) - 4*46 * k)) / (92)
        line = f"Para (k,c) = {k,c} obtenemos los siguientes valores de las exponenciales {val1, val2}"
        values.append((val1, val2))

print(values)