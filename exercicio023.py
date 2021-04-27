n = int(input('digite um número: '))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'analisando o número {n}...')
print(f'unidade: {u} \n dezena {d} \n centena: {c} \n milhar: {m}')
