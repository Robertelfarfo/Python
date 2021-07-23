from pandas import read_excel
from tkinter import ttk
from tkinter import Button
from tkinter import Label
from tkinter import LabelFrame
from tkinter import Entry
from tkinter import Tk
import busqueda as f_buscar
import cadenas
import grimex
from sqlite3 import connect
from os import path

class Product:
    
    global x
    global num_cotizacion
    x = 0
    
    
    def __init__(self,window):
        self.window = window
        self.window.title('Busqueda de prodcutos')
        self.window.geometry('1350x550')
        
        if path.isfile('db_cotizaciones.db'):
            #print('existe')
            d = 1
        else:
            #print('No existe')  
            conn = connect('db_cotizaciones.db')

            #creacion de cursor
            c = conn.cursor()

            #creacion de tabla
            c.execute("""CREATE TABLE cotizacion (
                piezas text,
                precios text
                )""")

            #commit our command
            conn.commit()
    
            #cerrar la conexion
            conn.close()
        
            #print('ya se creo')
            
    
        
        #creando el 
        
        tab_control = ttk.Notebook(window,width = 0 , height = 0)
        
        #creando la primera pestaña
        
        
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1 ,text = 'Hacer presupuesto')
        
        #craando la segunda pestaña 
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2 ,text = 'Buscar presupuesto')
        
        # creacion de Frame en tab1
        
        s = ttk.Style()
        s.configure('.', font=('Times', 12))
        
        #inicio del tab1
        frame = LabelFrame(tab1, text = "Producto a buscar")
        frame.place(x = 30, y = 20)
        
        #Label con el numero de cotizacion
        #num_cotizacion = cotizaciones['Num'][0]
        num_cotizacion = self.numero_cotizaciones_bd()
        cotizacion_visualizacion = Label(tab1, text ='Cotizacion no : A' + str(num_cotizacion))
        cotizacion_visualizacion.place(x = 1200,y = 120)
        
        def buscar_pieza_enter(event):
            buscar_pieza()
            return
        #Creacion  de cuadro de texto de busqueda y label
        Label(frame, text = 'Busqueda: ').grid(row = 1, column = 0)
        cuadro_pieza = Entry(frame, width = 45, borderwidth = 5)
        cuadro_pieza.bind('<Return>', buscar_pieza_enter)
        cuadro_pieza.focus()
        cuadro_pieza.grid(row = 1, column = 1)
        
        #creacion de boton de buscar
        buscar_pieza_boton = Button(frame, text = 'Buscar Ahora', padx = 10, pady = 5, command = lambda: buscar_pieza())
        buscar_pieza_boton.grid(row = 2, column = 1, pady = 10)
        
        #crear segunddo frame
        frame2 = LabelFrame(tab1, text = 'Opciones de producto')
        frame2.place(x = 210 ,y = 430)
        
        #creacion de  un boton de eliminar elementos de un arbol
        eliminar_resultados = Button(frame2, text = 'Borrar resultados', pady = 5,command = lambda: borrar_busqueda())
        eliminar_resultados.grid(row = 0,column = 0, pady = 10, padx = 10)
        
        #boton de añadir a presupuesto
        presupuesto = Button(frame2, text = 'Añadir al presupuerto', pady = 5, command = lambda: agregar())
        presupuesto.grid(row = 0, column = 1,pady = 10, padx = 10)
        
        
        #creacion de un tercer frame 
        frame3 = LabelFrame(tab1, text = 'Opciones de cotizacion')
        frame3.place(x = 950, y = 430)
        
        #boton para guardar a cotizacion
        guardar_cotizacion = Button(frame3, text = 'Guardar cotizacion', pady = 5,command = lambda : salvar_cotizacion())
        guardar_cotizacion.grid(row = 0, column = 0,pady = 10,padx = 10)
        
        #boton para eliminar articulo de la cotizacion
        eliminar_articulo = Button(frame3, text = 'Eliminar articulo', pady = 5, command = lambda : quitar_articulo())
        eliminar_articulo.grid(row = 0, column = 1, pady = 10, padx = 10)
        
         #boton para modificar el precio
        cambiar_precio = Button(frame3, text = 'Cambiar precio', pady =5, command = lambda : cambiar_costo())
        cambiar_precio.grid(row = 0, column = 2, pady = 10, padx = 10)
        
        #boton que carga las listas de excel
        cargar_listas_excel = Button(tab1,text = 'Cargar listas', pady = 5 , command = lambda: cargar_listas())
        cargar_listas_excel.place(x = 500, y = 70)
        indicador_lista = Label(tab1, text = 'Aun no se cargan datos de listas')
        indicador_lista.place(x = 600, y = 70)
        
        #para indicar numero de oincidencias 
        anuncio = Label(tab1, text = 'Coincidencias encontradas: ')
        anuncio.place(x = 50, y = 140)
        num_encontrado = Label(tab1, text = '-')
        num_encontrado.place(x = 210, y = 140)
        
        #creacion de arbol
        resultados = ttk.Treeview(tab1, selectmode = 'browse')
        #ubicacion de la tabla
        resultados.place(x = 30, y = 180)
        #definiendo columnas
        resultados["columns"] = ('1','2','3','4')
        #definiendo titulos
        resultados['show'] = 'headings'
        #asignndo el ancho y la alineacion a cada una de la soclumnas
        resultados.column("1", width = 25, anchor = 'w',stretch = True)
        resultados.column("2", width = 80, anchor = 'w')
        resultados.column("3", width = 500, anchor = 'w')
        resultados.column("4", width = 70, anchor = 'e')
        #ASIGNANDO EL NOMBRE DE LAS COLUMNAS
        resultados.heading("1", text = 'No')
        resultados.heading("2", text = 'Proveedor')
        resultados.heading("3", text = 'Pieza')
        resultados.heading("4", text = 'Precio')
        #fin de creacion de arbol
        
        #inicio de la tabla donde se guardan los productos cotizados
        cotizados = ttk.Treeview(tab1, selectmode = 'browse')
        #ubicacion de la tabla 
        cotizados.place(x = 750 ,y = 180)
        #deficion de las columnas 
        cotizados['columns'] = ('1','2')
        #definicion de titulos
        cotizados['show'] = 'headings'
        #asignacion del ancho y alineacion de las columnas 
        cotizados.column('1', width = 500 ,anchor = 'w' ,stretch = True)
        cotizados.column('2', width = 70 ,anchor = 'e' ,stretch = True)
        #nombre de las columnas
        cotizados.heading('1', text = 'Pieza')
        cotizados.heading('2', text = 'Precio')
        
        #fin de tab1
        
        
        
        
        #inicio de tab2
        
        #frame con busqueda de cotizacion
        tab2_frame1 = LabelFrame(tab2, text = "Busqueda de cotizacion")
        tab2_frame1.place(x = 30, y = 20)
        
        def buscar_cotizacion_enter(event):
            buscar_cotizacion()
            return
        
        Label(tab2_frame1, text = 'Cotizacion No. : A').grid(row = 1, column = 0)
        global cuadro_cotizacion
        cuadro_cotizacion = Entry(tab2_frame1, width = 20, borderwidth = 5)
        cuadro_cotizacion.bind('<Return>',buscar_cotizacion_enter)
        cuadro_cotizacion.grid(row = 1, column = 1)
        
        #creacion de boton de buscar cotizacion
        buscar_cotizacion_boton = Button(tab2_frame1, text = 'Buscar Cotizacion', padx = 10, pady = 5, command = lambda: buscar_cotizacion())
        buscar_cotizacion_boton.grid(row = 2, column = 0, pady = 10,padx = 5)
        
        #boton para borrar parametros
        borrar_parametros = Button(tab2_frame1, text = 'Limpiar', padx = 10, pady = 5, command = lambda : limpiar_casillas(arbol_cotizaciones))
        borrar_parametros.grid(row = 2,column = 1, pady = 10, padx = 5)
        
        #creacion de arbol que muestra los numeros de cotizaciones
        arbol_cotizaciones = ttk.Treeview(tab2, selectmode = 'browse')
        #ubicacion de la tabla
        arbol_cotizaciones.place(x = 30, y = 150)
        #definiendo columnas
        arbol_cotizaciones["columns"] = ('1','2')
        #definiendo titulos
        arbol_cotizaciones['show'] = 'headings'
        #asignndo el ancho y la alineacion a cada una de la soclumnas
        arbol_cotizaciones.column("1", width = 500, anchor = 'w',stretch = True)
        arbol_cotizaciones.column("2", width = 70, anchor = 'e')
        #ASIGNANDO EL NOMBRE DE LAS COLUMNAS
        arbol_cotizaciones.heading("1", text = 'Pieza')
        arbol_cotizaciones.heading("2", text = 'Precios')
        #fin de creacion de arbol
        
        #finde tab2
        
        
        tab_control.pack(expand = 1,fill = 'both') #fin del notebook
        
        def borrar_arbol(arbol):
            len_cuadro = len(arbol.get_children())
            if len_cuadro > 0:
                for x in range(0,len_cuadro):
                    arbol.delete(x)
            return #fin de funcion borrar_arbol()
        
        #funcion cuando se busca alguna pieza
        def buscar_pieza():
            global aldo
            global l_grimex
            borrar_tabla_resultados() # borra la tabla que muestra los resultados
            #resultados_piezas = []
            #se obtiene el dato de la caja de texto
            dato = cuadro_pieza.get()
            
            # en la linea siguinte se obtiene el modelo del carro y
            # que pieza del carro se esta buscando
            pieza_y_carro = f_buscar.pieza_carro_ano(dato) 
            #print('ALDO ',pieza_y_carro)
            
            #en la linea siguiente se obtiene el años del carro
            modelo = f_buscar.ano_conversion(pieza_y_carro[2])
            #print(modelo)
            pieza_grimex = grimex.traduccion_grimex(pieza_y_carro)
            #print('pieza_grimex ',pieza_grimex)
            
            #se hace la busqueda en toda la base de excel
            resultados_piezas_aldo = f_buscar.buscar_2(pieza_y_carro, aldo ,modelo)
            #print('listos resultados aldo')
            resultados_piezas_grimex = f_buscar.buscar_2(pieza_grimex, l_grimex , modelo)
            #print('listos resultados grimex')
            #print(len(resultados_piezas))
            m = len(resultados_piezas_aldo)
            n = len(resultados_piezas_grimex)
            
            for x in range(0,len(resultados_piezas_aldo)):
                #print(x)
                #print(resultados_piezas[x][0], resultados_piezas[x][1])
                resultados.insert("", 'end',iid = x, values =(x + 1,'Aldo', resultados_piezas_aldo[x][0], resultados_piezas_aldo[x][1]))
                #return #return de la insercion de elementos en la tabla
            
            for x in range(m,m+len(resultados_piezas_grimex)):
                resultados.insert("",'end',iid = x, values = (x + 1,'Grimex',resultados_piezas_grimex[m-x][0],resultados_piezas_grimex[m-x][1]))
            num_encontrado.configure(text = str(n+m))
            
            return #return de la deficnicion de funcion buscar_pieza()
        
        def borrar_tabla_resultados():
            len_resultados = len(resultados.get_children())
            #print(resultados.get_children())
            if len_resultados > 0:
                for x in range(0,len(resultados.get_children())):
                    resultados.delete(x)
            num_encontrado.configure(text = '-')
            return #return de la fincion borrar_resultados()
       
        def borrar_busqueda():
            cuadro_pieza.delete(0,'end')
            borrar_tabla_resultados()
            return
        
        def agregar():
            global x
            seleccion = resultados.selection()
            seleccion = seleccion[0]
            dato_seleccionado = resultados.item(seleccion)
            #print(dato_seleccionado['values'][1],dato_seleccionado['values'][2],x)
            cotizados.insert('','end',iid = x,values = (dato_seleccionado['values'][2], dato_seleccionado['values'][3]))
            x = x + 1
            return #return de la funcion agregar()
        
        def texto_cotizacion(num_cotizacion):
            texto = 'Cotizacion no: ' + str(num_cotizacion)
            return texto
        
        def salvar_cotizacion():
            global x
            cotizacion = cotizados.get_children()
            #print(cotizacion)
            cadena_pieza = ''
            cadena_precios = ''
            #print(cotizacion)
            for x in range(0,len(cotizacion)):
                dato = cotizados.item(x)
                #print(dato['values'][0])
                #print(dato['values'][1])
                cadena_pieza = cadena_pieza + dato['values'][0] + '!'
                cadena_precios = cadena_precios + str(dato['values'][1]) + '!'
                
            #print(cadena_pieza)
            #print(cadena_precios)
            
            
            #crar una base de datos o conectarse a ella
            conn = connect('db_cotizaciones.db')

            #crear un cursor
            c = conn.cursor()
            c.execute("INSERT INTO cotizacion VALUES (:piezas, :precios)",
              {
                  'piezas' : cadena_pieza,
                  'precios' : cadena_precios,
                  })
    
            #commit changes
            conn.commit()

            #cerrar conexion
            conn.close()
            
            #limpiar los arboles
            borrar_arbol(resultados)
            borrar_arbol(cotizados)
            
        
            cuadro_pieza.delete(0,'end') #limpia el cuadro de texto
                                        #donde se introduce la busqueda
            
            
            #modificando el numero de cotizacion 
            num_cotizacion = self.numero_cotizaciones_bd()
            cotizacion_visualizacion.configure(text = 'Cotizacion no A: ' + str(num_cotizacion))
            num_encontrado.configure(text = '-')
            x = 0
            
        
            
            return #esta funcion toma los articulos guardados en la seccion de piezas cotizadas y 
                  #los guarda en una base de datos
    
        def quitar_articulo():
            global x
            x = x - 1
            seleccion = cotizados.selection()
            seleccion = seleccion[0]
            #print(seleccion)
            cotizados.delete(seleccion)
            return #esta funcion elimina un articulo de la cotizacion
        
        def buscar_cotizacion():
            borrar_arbol(arbol_cotizaciones)
            #crar una base de datos o conectarse a ella
            conn = connect('db_cotizaciones.db')

            #crear un cursor
            c = conn.cursor()
            record_id = cuadro_cotizacion.get()
    
            #query de database
            c.execute('SELECT * FROM cotizacion WHERE oid = ' + record_id)
            records = c.fetchall()
            #commit changes
            conn.commit()

            #cerrar conexion
            conn.close()
            #print(records)
            
            piezas = cadenas.separacion(records[0][0])
            precios = cadenas.separacion(records[0][1])
            
            #print(piezas)
            #print(precios)
            for x in range(0,len(piezas)):
                arbol_cotizaciones.insert("", 'end',iid = x, values =(piezas[x], precios[x]))

            
            return 
        
        def cambiar_costo():
            
            seleccion_modificar = cotizados.selection() #pieza a cambiar el precio
            seleccion_modificar = seleccion_modificar[0] #indice dentro de la tabla de cotizados
            pieza_modificar = cotizados.item(seleccion_modificar)
            #print(pieza_modificar)
            
            global cambio_precio
            cambio_precio = Tk()
            cambio_precio.title('Modificar precio')
            cambio_precio.geometry('500x150')
            
            cadena = 'Articulo: ' + pieza_modificar['values'][0]
            label_pieza = Label(cambio_precio, text = cadena)
            label_pieza.place(x = 10, y = 10)
            
          
            #creacion de un tercer frame 
            frame_cambio_precio = LabelFrame(cambio_precio, text = 'Cambiar precio')
            frame_cambio_precio.place(x = 10, y = 35)
            
            #creacion de labels
            label_nuevo_precio = Label(frame_cambio_precio, text = 'Nuevo precio')
            label_nuevo_precio.grid(row = 0, column = 0)
            
            #text boxes
            global textbox_precio
            textbox_precio= Entry(frame_cambio_precio, width = 20, borderwidth = 5)
            textbox_precio.focus_set()
            textbox_precio.grid(row = 0, column = 1)
            
            #boton de cambiar modificar precio
            boton_modificar_precio = Button(frame_cambio_precio, text = 'Cambiar',padx = 7, pady = 5, command = lambda: modificar(seleccion_modificar,pieza_modificar))
            boton_modificar_precio.grid(row = 1,column = 1 , pady = 5, padx = 10)
            
            
            
            return
        
        def modificar(indice,actual):
            
            nuevo_precio = textbox_precio.get()
            cotizados.item(indice,values = (actual['values'][0],nuevo_precio))
            cambio_precio.destroy()
            
            return
        
        def limpiar_casillas(arbol):
            cuadro_cotizacion.delete(0,'end')
            borrar_arbol(arbol)
            
            return
        def cargar_listas():
            global aldo
            global l_grimex
            
            if path.isfile('LISTA ALDO.xlsx'):
                aldo = read_excel("LISTA ALDO.xlsx")
                aldo = aldo.fillna("nada") #rellena celdas que no tendan datos
                aldo = aldo.iloc[:,[1,2,3]]
                aldo.columns = ['pieza','sin_iva','con_iva']
            
            if path.isfile('GRIMEX_3.xlsx'):
                l_grimex = read_excel("GRIMEX_3.xlsx")
                l_grimex = l_grimex.fillna("nada") #rellena celdas que no tendan datos
                l_grimex = l_grimex.iloc[:,[1,2,3]]
                l_grimex.columns = ['pieza','sin_iva','con_iva']
            #print(aldo)
            #print(l_grimex)
            for x in range(0,len(l_grimex['pieza'])):
                if type(l_grimex['pieza'][x]) == int:
                    l_grimex['pieza'][x] = str(l_grimex['pieza'][x])
            
            indicador_lista.configure(text = 'Ya se cargaron listas')
            return
        

    
    def numero_cotizaciones_bd(self):
        #crar una base de datos o conectarse a ella
        conn = connect('db_cotizaciones.db')

        #crear un cursor
        c = conn.cursor()
    
        #query de database
        c.execute('SELECT *, oid FROM cotizacion')
        records = c.fetchall()
        #commit changes
        conn.commit()

        #cerrar conexion
        conn.close()
            
        num = len(records)
        
        num = num + 1
            
        #print(records)
        return num
    

        return #return de la definicion de la clase
    
    
    
        
    





if __name__ == '__main__':
    window = Tk()
    #manejo de dataframe
    
 
    #creacion de la aplicacion
    application = Product(window)
    window.mainloop()