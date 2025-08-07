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
        
    #salario=(input('coleque seu salario'))
    #sexo=(input('coloque seu sexo"f" ou "m" '))
    #estadocivil=(input('coleque seu salario'))