#1
# Nas orientações diz 'Você recebe uma lista de número de 0 a 300
# ordenados por ordem crescente', interpreto que a lista recebida
# tem 300 números em ordem crescente do 0 ao 299, apesar do algoritmo
# desenvolvido não ter muita utilidade prática.
lista=[]
for i in range(300):    
    lista.append(i)
x=int(input('Informe o número:'))
while(x>299 or x<0):
    print('O número deve ser um inteiro positivo < 300')
    x=int(input('Informe o novo número:'))
y=lista[x]
print(y)


