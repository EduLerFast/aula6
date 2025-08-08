"""Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

while True:
    nome=(input('digite o nome:'))
#funçao q retorna o tamanho do campo 'valor informado'
    while len(nome)<3:
        nome= input('digite o nome:')
    print(f'digitou um nome maior que 3 =>{nome}')
    break

Idade= int (input('digite sua idade:'))    
while Idade<0 or Idade> 150:
         Idade= int (input('digite sua idade:'))
print(f'digitou sua idade entre 0 e 150 =>{Idade}')

salario= float (input('digite seu salario:'))    
while salario<=0 :
         salario= float (input('digite seu salario:'))
print(f'digitou seu salario maior que 0 =>{Idade}')

while True:
    sexo = input('digite seu sexo:')
    if sexo == 'm':
     print(f'digitou o sexo =>masculino')
    elif sexo==('f'):
     print (f'digitou o sexo =>feminino')
     break

while True:
    estadocivil = input('digite seu estado civil:')
    if estadocivil == 's':
     print(f'digitou o estado civil =>solteiro')
    elif estadocivil==('c'):
     print (f'digitou o estado civil =>casado')
    elif estadocivil==('v'):
     print (f'digitou o estado civil =>viuvio')
    elif estadocivil==('d'):
     print (f'digitou o estado civil =>divorciado')

     break

