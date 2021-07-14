
class figure(object):
    def __init__(self,n_s):
        #n_s is the number of figure number sides
        self.n_s = n_s
    def area(self):
        pass
    def perimeter(self):
        pass
        
        
class square(figure):
    
    def __init__(self,size):
        figure.__init__(self,4)
        self.size = size
        self.area = self.area(size)
        self.perimeter = self.perimeter(self.n_s,size)
        
    def area(self,size):
        a = size * size
        return a
    def perimeter(self,n_s,size):
        return n_s*size


class circle(figure):
    def __init__(self, radius):
        figure.__init__(self,1)
        self.radius = radius
        self.perimeter = self.perimeter(radius)
        
    def perimeter(self,radius):
        return 3.1416*2*radius

class right_triangle(figure):
    
    def __init__(self,base,height):
        figure.__init__(self,3)
        self.base = base
        self.height = height
        self.area = self.area(base,height)
        
    def area(self,base,height):
        return (base*height) / 2

        
    
        
    

# square1 = square(5)
# circle1 = circle(2)


# print(square1.area)
        

