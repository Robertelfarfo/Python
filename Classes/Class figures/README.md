# About the heritage

As I mentioned this code is very simple, first I declared a class named "figure" in the file figures.py:

This class just have a constructor and two methods but there are not defined because the daughter classes will define this methods. As each figure has a different formula, each method would be different but all will have the same method names.

```python

class figure(object):
    def __init__(self,n_s):
        #n_s is the number of figure number sides
        self.n_s = n_s
    def area(self):
        pass
    def perimeter(self):
        pass

```

For example, tle class square:

```python

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

```

For know that the code works we can test it with a simple manual test:

