"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações"""
while True:
 nome= input('digie o nome:')
 senha= input('digie a senha:')
 if senha==nome:
  print('vc digitou a senha igual o nome')
 else:
  print('voce acertou')
  break