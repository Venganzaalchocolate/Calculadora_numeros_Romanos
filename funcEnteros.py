entrada=123

def ListaNumeros(entrada):
    if not isinstance(entrada, int):
        raise SyntaxError(f"{entrada} no es un número natural")
    
    lnum=str(entrada)
    ListaNumero=[]
    for n in lnum:
        ListaNumero.append(int(n))
    return ListaNumero
    
def unidades(listaNumeros):
    unidad=listaNumeros[-1]
    return listaUnidades[unidad]
    
def decenas(listaNumeros):
    unidad=listaNumeros[-2]
    return listaDecenas[unidad]

def centenas(listaNumeros):
    unidad=listaNumeros[-3]
    return listaCentenas[unidad]

def millares(listaNumeros):
    unidad=listaNumeros[-4]
    return listaMillares[unidad]

def convertir(ListaNumero):
    contador=0
    for x in ListaNumero[::-1]:
        procesar_simbolo(x, lista_ordenes[contador])
        contador += 1
 
        
    
lista_ordenes=[listaUnidades,listaDecenas,listaCentenas,listaMillares]      
listaMillares={1:'M', 2:'MM', 3:'MMM'}
listaCentenas={1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'}
listaDecenas={1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
listaUnidades={1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}

print(unidades(ListaNumeros(entrada)))