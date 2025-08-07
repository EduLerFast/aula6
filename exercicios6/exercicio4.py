"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com 
uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas
as taxas de crescimento."""
ano=0
paisa=(80000)
paisb=(200000)
while paisa < paisb:
    paisa=paisa*1.03
    paisb=paisb*1.015
    ano+=1
    #print('\n')
#if paisa >= paisb:
    print(f'pais A:{paisa:.0f}')
    print(f'pais B:{paisb:.0f}')
    print(f'irá demorar {ano} anos')
    