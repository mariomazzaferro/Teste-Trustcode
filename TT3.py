#3
primos=[]
x=int(input('Informe o número:'))
if(x>2):
    primos.append(2)
y=(x//3)+1
for i in range(3,x):
    c=0
    if(i%2!=0):
        for j in range(3,y,2):
            if(i!=j and i%j==0):
                c=c+1
                break
        if(c==0):
            primos.append(i)
print(primos)
  
    
