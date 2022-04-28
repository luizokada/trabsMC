import math

def taylorCosseno(n, anguloEmGraus):
    _sum = 0
    anguloEmGraus = math.radians(anguloEmGraus)
    for n in range(n):
        fact = math.factorial(2 * n)
        dividendo = (-1) ** n
        cos = (dividendo / fact) * (anguloEmGraus ** (2 * n))
        _sum += cos

    return round(_sum, 11)


def seno(x, n=7):
    x = math.radians(x) 
    return round(sum(serieTaylor(x, 20)),11)

def taylorInterection(x, n):
    return ((-1)**n / math.factorial(2*n+1)) * (x**(2*n+1))

def serieTaylor(x, n):
    list=[]
    for i in range(n):
        list.append(taylorInterection(x, i))
    return list
        
    
angle = input("angulo: ")
print(taylorCosseno(20,int(angle)))
print(seno(int(angle),20))