import math
import sys
from unicodedata import decimal
from unittest import skip


class IEEE():
    def __init__(self,signal,mantissa,exp) -> None:
        self.signal=signal
        self.mantissa=mantissa
        self.exp=exp
        pass
    def getSignal(self):
        return self.signal
    def getMantissa(self):
        return self.mantissa
    def getEXP(self):
        return self.exp
    
def srqrt(value):
    valueIEEE=deicalParaIEEE(value)
    valueIEEE.mantissa=srqrtCalc(valueIEEE)
    value=IEEEParaDecimal(valueIEEE)
    print(value)
    pass

def deicalParaIEEE(value):
    exp=int(math.log(value)/math.log(2))
    if value<0:
        value=value*(-1)
        bitSinal=1
    else:
        bitSinal=0
    mantissa=(value/(2**exp))-1
    return IEEE(bitSinal,mantissa,exp)
    
def IEEEParaDecimal(value:IEEE):
    sinal=(-1)**value.getSignal()
    decimal=(value.getMantissa()*sinal*(2**value.getEXP()))
    return decimal

def srqrtCalc(valueIEEE):
    if valueIEEE.exp%2==0:
        even=True
    else:
        even=False
        valueIEEE.exp=valueIEEE.exp-1
    valueIEEE.exp=valueIEEE.exp*0.5
    xk=0
    xk1=valueIEEE.mantissa*0.5+1
    valueIEEE.mantissa=valueIEEE.mantissa+1
        
    while(abs(xk1-xk)>math.exp(-20)):
        xk=xk1
        xk1=xk-(((xk**2)-valueIEEE.mantissa)/2*xk)
    
    if not even:
        return(math.sqrt(2)*xk1)
    else:
        return xk1

def test():    
    srqrt(2)
    srqrt(3)
    srqrt(4)
    srqrt(5)
    srqrt(6)
    srqrt(7)
    
if sys.argv[0]=="test":
    test()
else:
    x=input("Digite o valor que deseja calcular")
    srqrt(x)
    
    