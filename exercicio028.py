from random import randint
from time import sleep
print('-=' * 30)
print('\033[34mVou pensar em um número entre 0 e 5...tente adivinhar!\033[0m') 
print('-=' * 30)
sleep(2)
computador = randint(0,5) # Faz o computador pensar
choice = int(input('Em que número eu pensei? ')) # escolha do usuário
print('PROCESSANDO...')
sleep(3) #intervalo de contagem
if choice == computador:
    print('\033[32mVOCÊ VENCEU!')
    print(f'Eu pensei no número {computador}')
else:
    print('\033[31mVOCÊ PERDEU!')
    print(f'Eu pensei no número {computador} e não no número {choice}')

