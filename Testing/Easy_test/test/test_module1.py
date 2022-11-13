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