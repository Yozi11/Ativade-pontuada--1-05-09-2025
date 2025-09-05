import os
os.system


A = float(input("digite o valor A: "))

B = float(input("digite o valor B: "))
C = float(input("digite o valor C: "))

s= A+B

if A+B < C:
    print(f"{A} + {B} e menor que {C}")
else:
    print(f"{A} + {B} e maior que {C}")    
