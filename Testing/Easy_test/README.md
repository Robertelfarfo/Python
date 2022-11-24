### Test on simple packages

Is true that some codes are simplest than others. In this first project I'll show how I prefer test a code that is simple or is in charge of simple tasks.

The package "proj" make simple operations for complex numbers, this package have two modules. 

The package "test" is in charge of the testing, this package also contains two modules. 

The location of the files is show in the image below:

![Files Location](Images/files_1.JPG)


The module complex.py contains two functions "adition()" and "prod_esc()" while "module.py" contains the functions "modulus()" and argument(). In the folder proj both modules are available for more details.

Inside the module test I create two files, "test_module1.py" contains the class that test the function "adition()" and another class that test "prod_esc()":

```python
import proj

class TestAdition:

    def test_1(self):
        a = {'re' : 2,
             'im': 1}

        b = {'re': 7,
             'im': -2}
        assert proj.adition(a,b) == {'re': 9 , 'im': -1}

    def test_2(self):
        a = {'re' : -2,
             'im': 5}

        b = {'re': -5,
             'im': -2}

        assert proj.adition(a,b) == {'re': -7 , 'im': 3}

class TestProduct:
    
    def test_1(self):
        a = {'re': 7,
             'im': -2}
        b = 2
        assert proj.prod_esc(a,b) == {'re': 14, 'im': -4}

```

something similar with the file "test_module.py":

```python
import proj
import math

class TestModulus:

    def test_1(self):
        a = {'re': 4,
             'im': 3}
        assert proj.modulus(a) == 5

    def test_2(self):
        a = {'re': 4,
             'im': -4}
        assert proj.modulus(a) == math.sqrt(32)

class TestArgument:

    def test_1(self):
        a = {'re': 2,
             'im': -3}

        assert proj.argument(a) == math.atan(-3/2) 
```


For biginig the tests the easiest way is to locate us in the folder where both folder are located, I refer to the "proj" and "test" folders. Once I am on that location the comamand for discover all thetest is "nosetests -v" just tahat the image below. 

![Running Tests](Images/running.JPG)
