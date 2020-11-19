from funcRomanos import *

romano=('XIX')







print(romano.find('IXI')) #REGLA RESTA JODIDA:Un símbolo que aparece restando solo se puede repetir cuando su repetición esté colocada a más de un símbolo de distancia a su derecha.


numeros={'M':1000,'D':500,'C':100,'L':50,'X':10, 'V':5, 'I':1}
lista_romanos=[]
list_repeticion=[]
for letra in romano:
    if isinstance(letra, str) and letra.upper() in numeros:
        list_repeticion.append(letra.upper())       
        if list_repeticion.count('M')>4:
            print('Demasiadas M')
        elif list_repeticion.count('D')>1:
            print('Demasiadas M')
        elif list_repeticion.count('C')>4:
            print('Demasiadas C')
        elif list_repeticion.count('L')>1:
            print('Demasiadas M')
        elif list_repeticion.count('X')>4:
            print('Demasiadas X')
        elif list_repeticion.count('V')>1:
            print('Demasiadas M')
        elif list_repeticion.count('I')>4:
            print('Demasiadas I')
        else:
            lista_romanos.append(numeros[letra])
    elif isinstance(letra, str):
        print('Error')
    else:
        print('Error')
    



print(numero)
lista_mayor_menor=[]
for x in numero:
    if len(lista_mayor_menor)<=1:
        lista_mayor_menor.append(x)
        if len(lista_mayor_menor)==2:
            if lista_mayor_menor[0]>lista_mayor_menor[1]:
                lista_mayor_menor.pop(0)
            elif lista_mayor_menor[0]==lista_mayor_menor[1]:
                lista_mayor_menor.pop(0)
            elif lista_mayor_menor[0]<lista_mayor_menor[1]:
                print('fallo')

suma=0
for i in numero:
    suma+=i
           
        
print(suma)


