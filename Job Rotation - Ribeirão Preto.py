#Questão 01:
'''indice = 13;
soma =0;
k=0

while(k<indice):
        k=k+1;
        soma =soma+k;

print(soma);'''

#Questão 02:
'''n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1


if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)'''


#Questão 03:
#a) 1, 3, 5, 7, 9

#b) 2, 4, 8, 16, 32, 64, 128

#c) 0, 1, 4, 9, 16, 25, 36, 49

#d) 4, 16, 36, 64, 144

#e) 1, 1, 2, 3, 5, 8, 13

#f) 2,10, 12, 16, 17, 18, 19, 200

#Questão 04:
'''
I) Eq. Horária do Carro:
x= 110*t

II) Eq. Horária do caminhão
x= 100-v2*t

-tempo do caminhão sem os pedágios:
t'=(100km)/(80km/h) = 1,25h
-tempo do caminhão com os pedágios:
t''=(1,25h)+(0,17h) = 1,42h

-velocidade média do  caminhão:
v2= 100km/1,42h  = 70,6 km/h

-Igualando os tempos nas equações I e II:
(x/v1)=(x-100km)/-v2
-v1*x = v1*(x-100km)
x=(v1*100km)/(v1+v2)
x=(110km/h*100km)/(110km/h+70,6km/h)
x=60,9 km
'''

#Questão 05:
'''def inverter(txt):
  return txt[::-1]

print(inverter("Me Contrata!"))'''