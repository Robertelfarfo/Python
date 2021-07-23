from math import ceil

def calculo_precio_final(precio):
    precio_final = (precio * 0.785) + 30 
    precio_final = ceil(precio_final)
    modulo = precio_final % 10
    extra = 10 - modulo
    
    precio_final = precio_final + extra 
    
    return precio_final