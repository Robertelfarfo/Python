import re

def separacion(cadena):
    num_piezas = cadena.count('!')
    #print(num_piezas)
    elementos = []
   
    
    for x in range(0,num_piezas):
        #print(cadena)
        index_separador = cadena.find('!')
        elementos.append(cadena[0:index_separador])
        cadena = cadena[index_separador + 1 : len(cadena)]
        #print(cadena)
        
        
    #print(elementos)
    return elementos