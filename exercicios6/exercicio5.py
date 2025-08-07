
"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com 
uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas
as taxas de crescimento."""

"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""
poppaisa= float (input('escolha o tamanho da populaçao do pais A:'))
taxapaisa= float (input('escolha a taxa de crescimento iniciais da populaçao do pais A:'))

poppaisB= float (input('escolha o tamanho da populaçao do pais B:'))
taxapaisB= float (input('escolha a taxa de crescimento iniciais da populaçao do pais B:'))

ano=0

while poppaisa <= poppaisB:
    poppaisa=poppaisa*taxapaisa
    poppaisB=poppaisB*taxapaisB
    ano+=1
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print(f'pais A:{poppaisa:.0f}')
    print(f'pais B:{poppaisB:.0f}')
    print(f'irá demorar {ano} anos')
    