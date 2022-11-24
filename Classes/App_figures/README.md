## User interface developed with Tkinter for calculate the area and perimeter from circle, square and triangle
 
One of the first more "elaborated" thing I learned to do in Python was how to create a User Interface. For do that I learned how to use Tkinter. I think that the more complicated is understand how to create the class that will run the UI. 

```python

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

```

Inside that class named Figures I wrote the position of each element inside the UI. And just at the end the import thin "__init__", the part that will run the App each time we type "python3 AppFigures.py"

```python
if __name__ == '__main__':
    window = Tk()
    #manejo de dataframe
    
    #creacion de la aplicacion
    application = Figures(window)
    window.mainloop()
 
 ```
 
 Now, to show the results!!!
 
 
![Triangle!](IM2.png.JPG)

Another example:


 ![Circle!](IM3.png.JPG)
 
 If you want to run the app on your computer download the fie Appfigures.py and the file figures.py. The first file contains the user interface and the second one, figures.py , contains the classes "circle","square" and "triangle". Also download the folder Images, it contains the images that uses the interface. Put in the same foldes as the other two ".py" files, I mean if you save the ".py" files on a folder caled "App"
