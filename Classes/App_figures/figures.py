class figure(object):
    def __init__(self,n_s):
        #n_s is the number of figure number sides
        self.n_s = n_s
    def area(self):
        pass
    def perimeter(self):
        pass
        
        
class square(figure):
    
    def __init__(self,size=0):
        figure.__init__(self,4)
        self.size = size
        self.a = 0
        self.peri = 0
        
    def area(self):
        self.a = self.size * self.size
        return 
    def perimeter(self):
        self.peri = self.n_s * self.size
        return 


class circle(figure):
    def __init__(self, radius = 0):
        figure.__init__(self,1)
        self.radius = radius
        self.peri = 0.0
        self.a = 0;
        
    def perimeter(self):
        self.peri = 3.1416*2*self.radius
        return 
    def area(self):
        self.a = self.radius*self.radius*3.1416
        return

class right_triangle(figure):
    
    def __init__(self,base = 0,height=0):
        figure.__init__(self,3)
        self.base = base
        self.height = height
        self.a = 0
        self.peri = 0
        
    def area(self):
        self.a = (self.base * self.height) / 2
        return
    
    def perimeter(self):
        self.peri = self.base + self.height + pow(pow(self.base,2)+pow(self.height,2),0.5)
        return
