piratas = list()
cont = 0
opc = ['S','N']
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    poder = float(input('Nível de poder: '))
    grupo = str(input('Grupo [PIRATA/MARINHEIRO/REVOLUCIONÁRIO]: ')).strip().capitalize()
    piratas.append([nome,poder,grupo])
    r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    while r not in opc:
        print('\033[1;31mOpção inválida.Tente novamente\033[m')
        r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 50)
print(f"{'NOME':<10}{'PODER':<10}{'GRUPO:':<10}")
for pirata in piratas:
    print(f'{pirata[0]:<10}{pirata[1]:<10}{pirata[2]:<10}')
print( '-=' * 50)
while True:
    r = str(input('Quer ver uma luta entre dois personagens[S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
    for pos, pirata in enumerate(piratas):
        print(f'''[ {pos} ] - {pirata[0]}''')
    luta1 = int(input('Escolha um dos personagens para lutar: '))
    luta2 = int(input(f'Escolha um personagem para lutar contra {piratas[luta1][0]}: '))
    print('\033[32m-=' * 20,f'{piratas[luta1][0]} VS {piratas[luta2][0]}!', '-=\033[m' * 20)
    if piratas[luta1][1] > piratas[luta2][1]:
        print(f'{piratas[luta1][0]} venceu!')
    elif piratas[luta1][1] < piratas[luta2][1]:
        print(f'{piratas[luta2][0]} venceu!')
    else:
        print(f'EMPATE')


       
    

        
