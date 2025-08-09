"""
    Altere o programa anterior para mostrar no final a soma dos números.
"""

n1= int (input  ('coloque um numero:'))
n2= int (input  ('coloque outro numero:'))

for i in range (n1+1, n2 ):
    print(i,end=' ')
    soma = soma +i
print (f'a soma dos numros digitados é {soma}')