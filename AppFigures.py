import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import figures as f


class Figures:
    
    def __init__(self,window):
        
        triangle = f.right_triangle()
        square = f.square()
        circle = f.circle()
        
        global image_number 
        self.window = window
        self.window.title('Figures')
        self.window.geometry('700x250')
        
        #Frame number 1, this frame will contain a radio button
        frame = LabelFrame(window, text = "Chose a Figure")
        frame.place(x=200,y =10)
        
        #end of frame declaration
        
        #creating radiobutton inside the frame
        Modes = [
                ('Circle','Circle'),
                ('Square','Square'),
                ('Triangle','Triangle'),
                ]
        
        figu = StringVar()
        figu.set("Square")
        
        for text, mode in Modes:
            Radiobutton(frame, text = text, variable = figu, value = mode, command = lambda: click(figu.get())).pack(anchor = W)
        #ending with the radio button



        ### Create a photoimage object of the image in the path
        
        ## First we read the images and we stores in variables
        image1 = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.abspath(__file__))+"/Images/circle.jpg"))
        image2 = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.abspath(__file__))+"/Images/square.jpg"))
        image3 = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.abspath(__file__))+"/Images/triangle.jpg"))
        
        image_list = [image1, image2, image3] #this is alist that contains the images
        image_number = 1

        label1 = tkinter.Label(image=image_list[image_number])
        label1.image = image_list[image_number]

        # Position image
        label1.place(x=10, y=10)
        
        ### the Photoimage end configuration
        
        ### to create the Entrys that wil recibe the side measurements
        
        size_label = Label(window,text = 'Size :')
        size_label.place(x= 190, y = 120)
        
        size_entry = Entry(window)
        size_entry.place(x= 240, y = 120)
        
        height_label = Label(window,text = '- :')
        height_label.place(x= 390, y = 120)
        
        height_entry = Entry(window)
        height_entry.place(x= 440, y = 120)
        
        ### To create the labels that will show the calculus of area and perimeter
        
        Label(window,text = 'Perimeter = ').place(x = 190, y = 170)
        perimeter_label = Label(window,text = ' 0 ')
        perimeter_label.place(x= 270, y = 170)
        
        
        Label(window,text = 'Area = ').place(x = 320, y = 170)
        area_label = Label(window,text = ' 0 ')
        area_label.place(x= 380, y = 170)
        
        ### end of labels creation
        
        ### To create the button that will calculate the perimeter and area
        
        calculate_button = Button(window, text = 'Calculate',command = lambda : calculate(figu.get()))
        calculate_button.place(x = 440, y = 165)
        
        ### end of the button calculator
        
        
        ### the function click will update the radio button and the image
        def click(value):
            global image_number
            
            if value == 'Circle':
                image_number = 0
                size_label.configure(text='Radius :')
                height_label.configure(text = "- :")
            elif value == 'Square':
                image_number = 1
                size_label.configure(text='Size :')
                height_label.configure(text = "- :")
            elif value == "Triangle":
                image_number = 2
                size_label.configure(text='Base :')
                height_label.configure(text = "Height :")
            
            label1.configure(image=image_list[image_number])
            label1.image = image_list[image_number]
            
            return
        
        def calculate(figure):
            if figure == 'Circle':
                if type(int(size_entry.get())) == int and int(size_entry.get()) > 0:
                    
                    circle.radius = int(size_entry.get())
                    circle.perimeter()
                    circle.area()
                    perimeter_label.configure(text = str(circle.peri))
                    area_label.configure(text = str(circle.a))
                
            elif figure == 'Square':
                
                if type(int(size_entry.get())) == int and int(size_entry.get()) > 0:
                    square.size = int(size_entry.get())
                    square.perimeter()
                    square.area()
                    perimeter_label.configure(text = str(square.peri))
                    area_label.configure(text = str(square.a))
                    
            elif figure == 'Triangle':
                
                if type(int(size_entry.get())) == int and int(size_entry.get()) > 0:
                    triangle.base = int(size_entry.get())
                    triangle.height = int(height_entry.get())
                    triangle.perimeter()
                    triangle.area()
                    perimeter_label.configure(text = str(triangle.peri))
                    area_label.configure(text = str(triangle.a))
                
            
                
                
            #elif value == 'Square':
                
            #elif value == "Triangle":
                
            return
        
        
        

if __name__ == '__main__':
    window = Tk()
    #manejo de dataframe
    
    #creacion de la aplicacion
    application = Figures(window)
    window.mainloop()