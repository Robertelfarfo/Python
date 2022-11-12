import math

def modulus(a = dict):
    z = math.sqrt(a['re']**2 + a['im']**2)
    return z

def argument(a = dict):
    sigma = math.atan(a['im']/a['re'])
    return sigma