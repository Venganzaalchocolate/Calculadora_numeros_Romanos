def romano_a_entero(romano):
    return suma(comprobarMayorMenor(resta(repeticiones(romano))))

def repeticiones(romano):
    numeros={'M':1000,'D':500,'C':100,'L':50,'X':10, 'V':5, 'I':1}
    lista_romanos=[]
    list_repeticion=[]
    for letra in romano:
        if isinstance(letra, str) and letra.upper() in numeros:
            list_repeticion.append(letra.upper())       
            if list_repeticion.count('M')>4:
                return ValueError('Demasiadas M')
            elif list_repeticion.count('D')>1:
                return ValueError('Demasiadas D')
            elif list_repeticion.count('C')>4:
                return ValueError('Demasiadas C')
            elif list_repeticion.count('L')>1:
                return ValueError('Demasiadas L')
            elif list_repeticion.count('X')>4:
                return ValueError('Demasiadas X')
            elif list_repeticion.count('V')>1:
                return ValueError('Demasiadas V')
            elif list_repeticion.count('I')>4:
                return ValueError('Demasiadas I')
            else:
                lista_romanos.append(numeros[letra.upper()])
        elif isinstance(letra, str):
            return ValueError('Error')
        else:
            return ValueError('Error')
    if comprobandoCuatroSeguidas(romano)==True and comprobandoString(romano)==True:
        return lista_romanos
    else:
        ValueError('Fallo')

def comprobandoString(romano):
    rom=romano.upper()
    ivi=rom.find('IVI')
    ixi=rom.find('IXI')
    ixv=rom.find('IXV')
    xlx=rom.find('XLX')
    xcx=rom.find('XCX')
    cdc=rom.find('CDC')
    cmc=rom.find('CMC')
    cmd=rom.find('CMD')
    if ivi!=-1 or ixi!=-1 or ixv!=-1 or xlx!=-1 or xcx!=-1 or cdc!=-1 or cmc!=-1 or cmd!=-1:
        return ValueError('Esta resta no es correcta')
    else:
        return True

def comprobandoCuatroSeguidas(romano):
    rom=romano.upper()
    m=rom.find('MMMM')
    c=rom.find('CCCC')
    x=rom.find('XXXX')
    i=rom.find('IIII')
    if m!=-1 or c!=-1 or x!=-1 or i!=-1:
        return ValueError('Máximo se puede repetir 3 veces seguidas')
    else:
        return True
    
def resta(lista_romanos):
    lista=[]
    numero=[]
    restaI=0
    restaX=0
    restaC=0
    for i in lista_romanos:
        if len(lista)<=1:
            lista.append(i)
            if len(lista)==2:
                if lista[0]<lista[1]:
                    if lista[0]==1: # Me miras el valor que va a restar a I y me compruebas si se ha hecho una resta antes
                        if lista[1]==5 or lista[1]==10 and restaI==0:
                            resta=lista[1]-lista[0]
                            numero.append(resta)
                            lista.pop(0)
                            lista.pop(0)
                            restaI=1
                        else:
                            return ValueError('El símbolo I solo puede restar a V y a X y solo una vez')
                    elif lista[0]==10: # Me miras el valor que va a restar a X y me compruebas si se ha hecho una resta antes
                        if lista[1]==50 or lista[1]==100 and restaX==0:
                            resta=lista[1]-lista[0]
                            numero.append(resta)
                            lista.pop(0)
                            lista.pop(0)
                            restaX=1
                        else:
                            return ValueError('X solo puede restar a L y a C y solo una vez')
                    elif lista[0]==100: # Me miras el valor que va a restar a C y me compruebas si se ha hecho una resta antes
                        if lista[1]==500 or lista[1]==1000 and restaC==0:
                            resta=lista[1]-lista[0]
                            numero.append(resta)
                            lista.pop(0)
                            lista.pop(0)
                            restaC=1
                        else:
                            return ValueError('El símbolo C solo puede restar a D y a M y solo una vez')
                            
                    else:
                        return ValueError('Los símbolos 5 y sus múltiplos (V, L, D) siempre suman y no pueden estar a la izquierda de uno de mayor valor.')
                elif lista[0]>=lista[1]:
                    numero.append(lista[0])
                    lista.pop(0)
    if len(lista)!=0: # si se ha quedado un número colgado pues me lo añades. 
        numero.append(lista[0])
    return numero

def comprobarMayorMenor(numero):
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
                    return ValueError('Los valores tienen que ir de mayor a menor.')
    return numero

def suma(numero): # me sumas todos los elementos de la lista
    suma=0
    for i in numero:
        suma+=i
    return suma


