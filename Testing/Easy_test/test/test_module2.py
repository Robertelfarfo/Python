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