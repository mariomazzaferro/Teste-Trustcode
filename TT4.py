#4
abc='abcdefghijklmnopqrstuvwxyz'
ABC='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d={}
c=1
for i in abc:
    d[i]=c
    c=c+1
for i in ABC:
    d[i]=c
    c=c+1
palavra=str(input('Informe a palavra:'))
soma=0
for i in palavra:
    x=d[i]
    soma=soma+x
p=0
y=(soma//3)+1
if(soma!=2):
    if(soma%2==0 or soma==1):
        p=1
    else:
        for i in range(3,y,2):
            if(soma%i==0):
                p=p+1
                break
if(p==0):
    print('A palavra é prima')
else:
    print('A palavra não é prima')

        
    
        
    
    
    
    
