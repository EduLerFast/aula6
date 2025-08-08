"""
Faça um programa que leia 5 números e informe o maior número.
"""


Numero1= float (input  ('coloque um numero:'))
Numero2= float (input  ('coloque outro numero:'))
Numero3= float (input  ('coloque outro numero:'))
Numero4= float (input  ('coloque outro numero:'))
Numero5= float (input  ('coloque outro numero:'))

if Numero1 > Numero2 and Numero1 > Numero3 and Numero1 > Numero4 and Numero1 > Numero5:
    print(Numero1, 'é o maior numero')
elif Numero2 > Numero1 and Numero2 >  Numero3 and Numero2 >  Numero4 and Numero2 >  Numero5:
    print(Numero2, 'é o maior numero')
elif Numero3 > Numero2 and Numero3 >  Numero1 and Numero3 >Numero4 and Numero3 > Numero5:
    print(Numero3, 'é o maior numero')
elif Numero4 > Numero3 and Numero4  > Numero2 and Numero4 > Numero1 and  Numero4 >Numero5:
    print(Numero4, 'é o maior numero')
elif Numero5 > Numero4 and  Numero5 > Numero3 and Numero5 > Numero2 and Numero5 >Numero1:
    print(Numero5, 'é o maior numero')







