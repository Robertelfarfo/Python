def adition(a = dict,b = dict):
    c = {'re': None,
         'im': None}

    c['re'] = a['re'] + b['re']
    c['im'] = a['im'] + b['im']
    return c

def prod_esc(a = dict, b= int):
    c = {'re': None,
         'im': None}
    c['re'] = a['re'] * b
    c['im'] = a['im'] * b
    return c