def traduccion_grimex(info_aldo):
    opciones = [['BRAZO DEFENSA',0],['BRAZO DEFENSA TRAS',1],['BRAZO DEFENSA DEL',2],
               ['BIGOTERA',3],['CUARTO LAT',4],['DEFENSA',5],['DEFENSA DEL',6],['DEFENSA TRAS',7],
               ['FARO NIEBLA',8],['GUIA DEFENSA',9],['GUIA DEFENSA DEL',10],['GUIA DEFENSA TRAS',11],
               ['MANIJA ELEV',12],['MARCO RADIADOR',13],['MOLDURA DEFENSA',14],['PORTAPLACA',15],
               ['REFUERZO DEFENSA',16],['REFUERZO DEFENSA DEL',17],['REFUERZO DEFENSA TRAS',18]]
    
    lista_piezas_grimex = ['BRACK','BRACK TRAS','BRACK DEL','CORAZA','CUARTO L',['DEFENSA','FASCIA'],
                           ['DEFENSA DEL','FASCIA DEL'],['DEFENSA TRAS','FASCIA TRAS'],'FARO N','GUIA FASCIA',
                           'GUIA FASCIA DEL','GUIA FASCIA TRAS','MANIJA ELEVAR','MARCO RAD','BANDA DEF',
                           'PORTA PLACA','REFUERZO','REFUERZO DEL','REFUERZO TRAS']
    pieza_grimex = ''
    
    for opcion in opciones:
        if opcion[0] == info_aldo[0]:
            pieza_grimex = lista_piezas_grimex[opcion[1]]
            break
    if pieza_grimex == '':
        pieza_grimex = info_aldo[0]
          
    
    
    info_grimex = [pieza_grimex,info_aldo[1],info_aldo[2]] 
    
    return info_grimex