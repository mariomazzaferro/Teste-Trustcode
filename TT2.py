#2
lista1=[]
lista2=[]
lista3=[]
import random
import math
for i in range(500):
    lista1.append(random.randint(0,5000000))
for i in range(50000):
    lista2.append(random.randint(0,5000000))
for i in range(50000):
    for j in range(500):
        if(lista2[i]==lista1[j]):
            lista3.append(lista2[i])
print(lista3)
    
    
