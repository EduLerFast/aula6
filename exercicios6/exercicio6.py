"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro
"""


for i in range(20):
    
    print(i+1)

lado=[]
for i in range(21) :
 
 lado.append(i)
 
 if lado==[20]:
  break
lado.pop(0) 
print(lado) 