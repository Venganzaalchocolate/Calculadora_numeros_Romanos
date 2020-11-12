

def romano_a_entero(romano):
    numeros={'M':1000,'D':500,'C':100,'L':50,'X':10, 'V':5, 'I':1}
    if isinstance(romano, str) and romano.upper() in numeros:
        return numeros[romano.upper()]
    elif isinstance(romano, str):
        return ValueError('{} no es un número romano'.format(romano))
    else:
        raise ValueError(f'parámetro {romano} debe ser un string')