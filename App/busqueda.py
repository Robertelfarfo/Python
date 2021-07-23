from re import findall
import redondeo as redondeo

def pieza_carro_ano(busqueda):
    #saca el string con el modelo del carro y la pieza que se desea buscar
    pieza_modelo_ano = busqueda.upper()
    busqueda_upper = pieza_modelo_ano
    pieza_modelo_ano = findall("\w+",pieza_modelo_ano)

    #print(pieza_modelo_ano)   
    pieza_aux = False
    #pieza = ' '
    #ANALISIS DEL TIPO DE PIEZA
    if 'ALERON' in pieza_modelo_ano:
        pieza = 'ALERON'
    else:
        if 'ANTI' in pieza_modelo_ano or ('ANTIMPACTO' in pieza_modelo_ano):
            if pieza_modelo_ano[1] == 'DEL' or pieza_modelo_ano[2] == 'TRAS':
                pieza = ['ANTIMPACTO',pieza_modelo_ano[1]]
                pieza = " ".join(pieza)
                pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                pieza_aux = ' '.join(pieza_aux)
            else:
                pieza = 'ANTIMPACTO'
                pieza_aux = pieza_modelo_ano[0]
        else:
            if 'BIGOTERA' in pieza_modelo_ano:
                pieza = 'BIGOTERA'
            else:
                if 'BISAGRA' in pieza_modelo_ano:
                    pieza = 'BISAGRA'
                else:
                    if 'BISEL' in pieza_modelo_ano:
                        pieza = 'BISEL'
                    else:
                        if 'BRAZO' in pieza_modelo_ano:
                            if 'DEF' in pieza_modelo_ano:
                                if ('TRAS' in pieza_modelo_ano) or ('DEL' in pieza_modelo_ano):
                                    pieza = ['BRAZO DEFENSA',pieza_modelo_ano[2]]
                                    pieza = " ".join(pieza)
                                    pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1],pieza_modelo_ano[2]]
                                    pieza_aux = ' '.join(pieza_aux)
                                else:
                                    pieza = 'BRAZO DEFENSA'
        
                                    pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                    pieza_aux = ' '.join(pieza_aux)
                            else:
                                pieza = 'BRAZO'
                        else:
                            if (('CALAVERA' in pieza_modelo_ano) or ('CAL' in pieza_modelo_ano)):
                                pieza = 'CALAVERA'
                                pieza_aux = pieza_modelo_ano[0]
                                # opciones = ['CAL','CALAVERA']
                                # for opcion in opciones: 
                                #     if opcion in pieza_modelo_ano and (opcion == pieza_modelo_ano[0]):
                                #         pieza = 'CALAVERA'
                                #         pieza_aux = pieza_modelo_ano[0]
                                #         pieza_aux = ' '.join(pieza_aux)
                                #         print('Pieza aux: ',pieza_aux)
                                #         print('Resto: ',pieza_modelo_ano)
                                
                            else:
                                if 'CHAPA' in pieza_modelo_ano:
                                    pieza = 'CHAPA'
                                else:
                                    if 'COFRE' in pieza_modelo_ano and ('COFRE' == pieza_modelo_ano[0]):
                                        pieza = 'COFRE'
                                    else:
                                        if 'CONDENSADOR' in pieza_modelo_ano:
                                            pieza = 'CONDENSADOR'
                                        else:
                                            if 'COSTADO' in pieza_modelo_ano:
                                                pieza = 'COSTADO'
                                            else:
                                                if 'CUARTO' in pieza_modelo_ano:
                                                    if pieza_modelo_ano[1] == 'LAT' or pieza_modelo_ano[1] == 'PUNTA' or pieza_modelo_ano[1] == 'TRAS' or pieza_modelo_ano[1] == 'FRONTAL':
                                                        pieza = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                        pieza = ' '.join(pieza)
                                                        pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                        pieza_aux = ' '.join(pieza_aux)
                                                    else:
                                                        pieza = 'CUARTO'
                                                else:
                                                    if ('DEF' in pieza_modelo_ano or 'DEFENSA' in pieza_modelo_ano) and ('DEF' == pieza_modelo_ano[0] or 'DEFENSA' == pieza_modelo_ano[0]):
                                                        if (pieza_modelo_ano[1] == 'TRAS') or (pieza_modelo_ano[1] == 'DEL'):
                                                            pieza = ['DEFENSA',pieza_modelo_ano[1]]
                                                            pieza = ' '.join(pieza)
                                                            pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                            pieza_aux = ' '.join(pieza_aux)
                                                        else:
                                                            pieza = 'DEFENSA'
                                                            pieza_aux = pieza_modelo_ano[0]
                                                    
                                                    else:
                                                        if 'DEPOSITO' in pieza_modelo_ano:
                                                            pieza = 'DEPOSITO'
                                                        else:
                                                            if ('ESPEJO' in pieza_modelo_ano) or ('ESP' in pieza_modelo_ano):
                                                                pieza = 'ESPEJO'
                                                                pieza_aux = pieza_modelo_ano[0]
                                                                #print(pieza_aux)
                                                            else:
                                                                if 'FARO' in pieza_modelo_ano and ('FARO' == pieza_modelo_ano[0]):
                                                                    if pieza_modelo_ano[1] == 'NIEBLA':
                                                                        pieza = 'FARO NIEBLA'
                                                                    else:
                                                                        pieza = 'FARO'
                                                                else:
                                                                    if 'GUIA' in pieza_modelo_ano:
                                                                        if ('DEL' in pieza_modelo_ano) or ('TRAS' in pieza_modelo_ano):
                                                                            pieza = [pieza_modelo_ano[0],'DEFENSA',pieza_modelo_ano[1]]
                                                                            pieza = ' '.join(pieza)
                                                                            pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                            pieza_aux = ' '.join(pieza_aux)
                                                                        else:
                                                                            pieza = 'GUIA DEFENSA'
                                                                            pieza_aux = pieza_modelo_ano[0]
                                                                    else:
                                                                        if 'MANIJA' in pieza_modelo_ano:
                                                                            if pieza_modelo_ano[1] == 'INT' or pieza_modelo_ano[1] == 'EXT' or pieza_modelo_ano[1] == 'TAPA':
                                                                                pieza = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                pieza = ' '.join(pieza)
                                                                                pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                pieza_aux = ' '.join(pieza_aux)
                                                                            else:
                                                                                if pieza_modelo_ano[1] == 'ELEVADOR' or pieza_modelo_ano == 'ELE':
                                                                                    pieza = 'MANIJA ELEV'
                                                                                    pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                    pieza_aux = ' '.join(pieza_aux)
                                                                                else:
                                                                                    pieza = pieza_modelo_ano[0]
                                                                        else:
                                                                            if 'MARCO' in pieza_modelo_ano:
                                                                                if pieza_modelo_ano[1] == 'RAD' or pieza_modelo_ano[1] == 'RADIADOR':
                                                                                    pieza = 'MARCO RADIADOR'
                                                                                    pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                    pieza_aux = ' '.join(pieza_aux)
                        
                                                                                else:
                                                                                    pieza = 'MARCO'
                                                                            else:
                                                                                if ('MOLD' in pieza_modelo_ano) or ('MOLDURA' in pieza_modelo_ano):
                                                                                    if 'DEF' in pieza_modelo_ano:
                                                                                        pieza = 'MOLDURA DEFENSA'
                                                                                        pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                        pieza_aux = ' '.join(pieza_aux)
                                                                                    else:
                                                                                        if 'SALP' in pieza_modelo_ano or 'ARCO' in pieza_modelo_ano:
                                                                                            pieza = 'MOLDURA ARCO'
                                                                                            pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                            pieza_aux = ' '.join(pieza_aux)
                                                                                        else:
                                                                                            if 'COFRE' in pieza_modelo_ano:
                                                                                                pieza = 'MOLDURA COFRE'
                                                                                                pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                                pieza_aux = ' '.join(pieza_aux)
                                                                                            else:
                                                                                                if 'FARO' in pieza_modelo_ano:
                                                                                                    pieza = 'MOLDURA FARO'
                                                                                                    pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                                    pieza_aux = ' '.join(pieza_aux)
                                                                                                else:
                                                                                                    if 'CALAVERA' in pieza_modelo_ano or 'CAL' in pieza_modelo_ano:
                                                                                                        pieza = 'MOLDURA CALAVERA'
                                                                                                        pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                                        pieza_aux = ' '.join(pieza_aux)
                                                                                                    else:
                                                                                                        if 'PUERTA' in pieza_modelo_ano:
                                                                                                            pieza = 'MOLDURA PUERTA'
                                                                                                            pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                                            pieza_aux = ' '.join(pieza_aux)
                                                                                                        else:
                                                                                                            pieza = 'MOLDURA'
                                                                                                            pieza_aux = pieza_modelo_ano[0]
                                                                                    #if 'SALP' in pieza_modelo_ano:
                                                                                    #    pieza = 'MOLDURA ARCO'
                                                                                    #    pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                    #    pieza_aux = ' '.join(pieza_aux)
                                                                                    #else:
                                                                                    #    if 'TRAS' in pieza_modelo_ano:
                                                                                    #        pieza = 'MOLDURA ARCO TRAS'
                                                                                    #        pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                    #        pieza_aux = ' '.join(pieza_aux)
                                                                                    #    else:
                                                                                    #        pieza = 'MOLDURA'
                                                                                else:
                                                                                    if ('PARRILLA' in pieza_modelo_ano) or ('ILLA' in pieza_modelo_ano):
                                                                                        pieza = 'PARRILLA'
                                                                                        pieza_aux = pieza_modelo_ano[0]
                                                                                    else:
                                                                                        if ('PORTAPLACA' in pieza_modelo_ano):
                                                                                            pieza = 'PORTAPLACA'
                                                                                        else:
                                                                                            if ('CHICOTE' in pieza_modelo_ano):
                                                                                                pieza = 'CHICOTE'
                                                                                            else:
                                                                                                if('PUERTA' in pieza_modelo_ano) and ('PUERTA' == pieza_modelo_ano[0]):
                                                                                                    pieza = 'PUERTA'
                                                                                                else:
                                                                                                    if('CAJUELA' in pieza_modelo_ano):
                                                                                                        pieza = 'TAPA CAJUELA'
                                                                                                    else:
                                                                                                        if 'TOLVA' in pieza_modelo_ano:
                                                                                                        
                                                                                                            if 'RAD' in pieza_modelo_ano or 'RADIADOR' in pieza_modelo_ano:
                                                                                                                pieza = ['TOLVA','RADIADOR']
                                                                                                                #pieza = ' '.join(pieza)
                                                                                                                pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                                                pieza_aux = ' '.join(pieza_aux)
                                                                                                            else:
                                                                                                                if 'MOTOR' in pieza_modelo_ano:
                                                                                                                    pieza = 'TOLVA INF MOTOR'
                                                                                                                    pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                                                    pieza_aux = ' '.join(pieza_aux)
                                                                                                                else:
                                                                                                                    if 'DEF' in pieza_modelo_ano or 'DEFENSA' in pieza_modelo_ano:
                                                                                                                        pieza = 'TOLVA DEFENSA'
                                                                                                                        pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                                                        pieza_aux = ' '.join(pieza_aux)
                                                                                                                    else:
                                                                                                                        if 'SALP' in pieza_modelo_ano:
                                                                                                                            pieza = ['TOLVA ','SALP']
                                                                                                                            pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                                                            pieza_aux = ' '.join(pieza_aux)
                                                                                                                        else:
                                                                                                                            pieza = 'TOLVA'
                                                                                                        else:
                                                                                                            if ('REF' in pieza_modelo_ano) or ('REFUERZO' in pieza_modelo_ano) or ('ALMA' in pieza_modelo_ano):
                                                                                                                if 'DEL' in pieza_modelo_ano or ('TRAS' in pieza_modelo_ano):
                                                                                                                    pieza = ['REFUERZO','DEFENSA',pieza_modelo_ano[1]]
                                                                                                                    pieza = ' '.join(pieza)
                                                                                                                    pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                                                    pieza_aux = ' '.join(pieza_aux)
                                                                                                                else:
                                                                                                                    pieza = 'REFUERZO DEFENSA'
                                                                                                                    pieza_aux = pieza_modelo_ano[0]
                                                                                                            else:
                                                                                                                if ('SALP' in pieza_modelo_ano) or ('SALPICADERA' in pieza_modelo_ano):
                                                                                                                    opcion = [['SALP' in pieza_modelo_ano, 'SALP'] , ['SALPICADERA' in pieza_modelo_ano,'SALPICADERA']]
                                                                                                                    #print(opcion)
                                                                                                                    for x in opcion:
                                                                                                                        if x[0]:
                                                                                                                            pieza_aux = x[1]
                                                                                                                            #print(pieza_aux)
                                                                                                                    
                                                                                                                    if pieza_modelo_ano.index(pieza_aux) == 0:
                                                                                                                        #print(pieza_modelo_ano.index(pieza_aux))
                                                                                                                        pieza = 'SALPICADERA'
                                                                                                                        pieza_aux = pieza_modelo_ano[0]
                                                                                                                    else:
                                                                                                                        if pieza_modelo_ano.index(pieza_aux) == 1:
                                                                                                                            #print(pieza_modelo_ano.index(pieza_aux))
                                                                                                                            pieza = 'TOLVA SALPICADERA'
                                                                                                                            pieza_aux = [pieza_modelo_ano[0],pieza_modelo_ano[1]]
                                                                                                                            pieza_aux = ' '.join(pieza_aux)
                                                                                                                else:
                                                                                                                    if ('SPOILER' in  pieza_modelo_ano):
                                                                                                                        pieza = 'SPOILER'
                                                                                                                    else:
                                                                                                                        #aqui poner lo de radiador
                                                                                                                        if ('RAD' in pieza_modelo_ano) or 'RADIADOR' in pieza_modelo_ano:
                                                                                                                            #print('es un radiador')
                                                                                                                            pieza = 'RADIADOR'
                                                                                                                            pieza_aux = pieza_modelo_ano[0]
                                                                                                                           
                                                                                                                            
                                                                                        
                
            
    #la variable pieza_modelo_ano es una lista, donde el string ingresado por el usuario 
    #esta separado por palabras
    
    if pieza_modelo_ano[len(pieza_modelo_ano) - 1].isdigit(): #si la pieza buscada tiene un año
        ano = pieza_modelo_ano[len(pieza_modelo_ano) - 1]     #en especifico
        index_ano = pieza_modelo_ano.index(ano)
        index_ano_en_busqueda = busqueda_upper.find(ano)
        
        if 'MAZDA' in pieza_modelo_ano or 'SERIE' in pieza_modelo_ano or 'PEUGEOT' in pieza_modelo_ano:
            #proceso para obtener indices de modelo y de año
            opcion = [['MAZDA','MAZDA' in pieza_modelo_ano],['SERIE','SERIE' in pieza_modelo_ano],['PEUGEOT','PEUGEOT' in pieza_modelo_ano]]
            
            for x in opcion:
                if x[1]:
                    modelo = x[0]
                    index_modelo = pieza_modelo_ano.index(modelo)
            
            if index_ano == index_modelo + 1:
                modelo = [pieza_modelo_ano[index_modelo],pieza_modelo_ano[index_ano]]
                modelo = ' '.join(modelo)
                ano = False
            else:
                modelo = [pieza_modelo_ano[index_modelo],pieza_modelo_ano[index_modelo + 1]]
                modelo = ' '.join(modelo)
                ano = pieza_modelo_ano[len(pieza_modelo_ano) - 1]
            
        else:
            #print('No es un mazda ni nada de eso')    
            if pieza_aux:
                #print('Tiene pieza aux: ',pieza_aux)
                modelo = busqueda_upper[(len(pieza_aux) + 1) : index_ano_en_busqueda - 1]
            
            else:
                modelo = busqueda_upper[(len(pieza) + 1) : index_ano_en_busqueda - 1]
            
    else:
        ano = False
        if pieza_aux:
            modelo = busqueda_upper[(len(pieza_aux) + 1) : len(busqueda_upper)]
            
        else:
            modelo = busqueda_upper[(len(pieza) + 1) : len(busqueda_upper)]
    
    
    
    carro = [pieza,modelo,ano]
    #print(carro)
    
    return carro

def modelo(ano):
    modelo = int(ano)
    #if modelo < 1 and modelo > 

    return modelo

def ano_conversion(ano):
    conversion = int(ano)
    
    if ano == False:
        ano = False
    else:
        if conversion >= 0 and conversion < 24:
            ano = 2000 + conversion
        else:
            ano = 1900 + conversion
        
    return ano

def analisis_celda(pieza_carro,celda):
    #posicion en la informacion de la celda sobre el carro analizado
    index_carro_celda = celda.find(pieza_carro[1])
    #recortamos la infromacion a analizar
    recorte = celda[index_carro_celda + len(pieza_carro[1]):len(celda)]
    #print(recorte)
    #nuevo indice
    index_carro_celda = recorte.find(pieza_carro[1])
    modelos_celda = []
    #separamos las palabras de la informacion en la celda
    recorte_separada = findall('\w+',recorte)
    #print(recorte_separada)
    #print(len(recorte_separada))
    
    for x in range(0,len(recorte_separada)):
        if recorte_separada[x].isdigit() == True:
            index_modelo = recorte.find(recorte_separada[x])
            if index_modelo > index_carro_celda:
                modelos_celda.append(recorte_separada[x])
                if (x < (len(recorte_separada) - 1)):
                    if (recorte_separada[x + 1].isdigit() == True):    
                        modelos_celda.append(recorte_separada[x + 1])
                        break
    return modelos_celda


def buscar(pieza_carro,datos_busqueda,modelo = False):

    encontrado = []
    #print(pieza_carro[0],pieza_carro[1])
    
    if modelo:
        for x in range(0,len(datos_busqueda['pieza'])): 
            #si los datos de busqueda coinciden con la infromacion en la celda
            modelo_celda =[]
            if (datos_busqueda['pieza'][x].find(pieza_carro[0]) > -1) and (datos_busqueda['pieza'][x].find(pieza_carro[1]) > -1) and (datos_busqueda['pieza'][x].find(pieza_carro[0]) == 0):
                #print(datos_busqueda['pieza'][x])
                modelo_celda = analisis_celda(pieza_carro, datos_busqueda['pieza'][x])
                #print(modelo_celda)                            
                #ahora analizamos si el modelo buscado esta dentro del rango de la informacion
                
                if len(modelo_celda) == 2:
                    modelo_celda[0] = ano_conversion(modelo_celda[0])
                    modelo_celda[1] = ano_conversion(modelo_celda[1])
                    #modelo_celda[0] = int(modelo_celda[0])
                    #modelo_celda[1] = int(modelo_celda[1])
                    #print(modelo_celda)
                    #print(datos_busqueda['pieza'][x])
                    if (modelo >= modelo_celda[0]) and (modelo <= modelo_celda[1]):
                        encontrado.append([datos_busqueda['pieza'][x], redondeo.calculo_precio_final(datos_busqueda['sin_iva'][x])])
                        #print(datos_busqueda['pieza'][x])
                else:
                    if len(modelo_celda) == 1:
                        #modelo_celda[0] = ano_conversion(modelo_celda[0])
                        modelo_celda[0] = int(modelo_celda[0])
                        if modelo == modelo_celda[0]:
                            encontrado.append([datos_busqueda['pieza'][x],redondeo.calculo_precio_final(datos_busqueda['sin_iva'][x])])
   
    else:
        #print('no hay modelo')
        #print(pieza_carro)
        for x in range(0,len(datos_busqueda['pieza'])):
            modelo_celda = []
            if (datos_busqueda['pieza'][x].find(pieza_carro[0]) > -1) and (datos_busqueda['pieza'][x].find(pieza_carro[1]) > -1) and (datos_busqueda['pieza'][x].find(pieza_carro[0]) == 0):
                encontrado.append([datos_busqueda['pieza'][x],redondeo.calculo_precio_final(datos_busqueda['sin_iva'][x])])
                
            
            #fin del for x in range(0,len(datos_busqueda['pieza]))
            
            
            
            
        #return #return del if-else
    
    return encontrado #return de la definicion 

def buscar_2(pieza_carro,datos_busqueda,modelo = False):
    encontrado = []
    if type(pieza_carro[0]) == list:
        #print('pieza en tipo lista')
        if modelo:
            #print('pieza a buscar tiene modelo especifico')
            m = len(pieza_carro[0])
            
            for x in range(0,len(datos_busqueda['pieza'])):
                n = 0
                for palabra in pieza_carro[0]:
                    
                    if palabra in datos_busqueda['pieza'][x]:
                        n = n + 1
                
                if ('DEFENSA' in pieza_carro[0][0]) and ('FASCIA' in pieza_carro[0][1]):
                    #print('entra ya que esta ',pieza_carro[0][0],' o ',pieza_carro[0][1])
                    for opcion in pieza_carro[0]:
                        #print('Entra ',opcion)
                        if opcion in datos_busqueda['pieza'][x]:
                            n = m
                
                if n == m:
                    if datos_busqueda['pieza'][x].find(pieza_carro[1]) > -1:
                        #print('coincidencia con: ' + pieza_carro[1])
                        modelos_celda = analisis_celda(pieza_carro, datos_busqueda['pieza'][x])
                        respuesta = analisis_modelo(modelo,modelos_celda)
                        if respuesta:
                            encontrado.append([datos_busqueda['pieza'][x],redondeo.calculo_precio_final(datos_busqueda['sin_iva'][x])])
                    
                
        else:
            #print('pieza a buscar no tiene modelo especifico')
            m = len(pieza_carro[0])
            
            for x in range(0,len(datos_busqueda['pieza'])):
                n = 0
                for palabra in pieza_carro[0]:
                    if palabra in datos_busqueda['pieza'][x]:
                        n = n + 1
                
                if ('DEFENSA' in pieza_carro[0][0]) and ('FASCIA' in pieza_carro[0][1]):
                    #print('entra ya que esta ',pieza_carro[0][0],' o ',pieza_carro[0][1])
                    for opcion in pieza_carro[0]:
                        #print('Entra ',opcion)
                        if opcion in datos_busqueda['pieza'][x]:
                            n = m
                
                if n == m:
                    if datos_busqueda['pieza'][x].find(pieza_carro[1]) > -1:
                        encontrado.append([datos_busqueda['pieza'][x],redondeo.calculo_precio_final(datos_busqueda['sin_iva'][x])])
            
    
    else:
        #print('pieza en tipo palabra')
        
        if modelo:
    
            for x in range(0,len(datos_busqueda['pieza'])):
                if (datos_busqueda['pieza'][x].find(pieza_carro[0]) > -1) and (datos_busqueda['pieza'][x].find(pieza_carro[1]) > -1) and (datos_busqueda['pieza'][x].find(pieza_carro[0]) == 0):
                    modelos_celda = analisis_celda(pieza_carro, datos_busqueda['pieza'][x])
                    respuesta = analisis_modelo(modelo,modelos_celda)
                    if respuesta:
                        encontrado.append([datos_busqueda['pieza'][x],redondeo.calculo_precio_final(datos_busqueda['sin_iva'][x])])
                
            
        else:
            #print('si modelo especifico')
            for x in range(0,len(datos_busqueda['pieza'])):
                 if (datos_busqueda['pieza'][x].find(pieza_carro[0]) > -1) and (datos_busqueda['pieza'][x].find(pieza_carro[1]) > -1) and (datos_busqueda['pieza'][x].find(pieza_carro[0]) == 0):
                     encontrado.append([datos_busqueda['pieza'][x],redondeo.calculo_precio_final(datos_busqueda['sin_iva'][x])])
            
    
    return encontrado

def analisis_modelo(modelo_carro,modelos_celda):
    resp = False
    if len(modelos_celda) == 2:
         year_1 = ano_conversion(modelos_celda[0])
         year_2 = ano_conversion(modelos_celda[1])
         if (modelo_carro >= year_1) and (modelo_carro <= year_2):
             resp = True
    else:
        if len(modelos_celda) == 1:
            year_1 = ano_conversion(modelos_celda[0])
            if modelo_carro == year_1:
                resp = True
    return resp
    
    