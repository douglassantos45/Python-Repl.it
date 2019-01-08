list = []
par = []
ímpar = []

while True:
  list.append(int(input('\nInforme um número: ')))
  resp = str(input('\nDeseja Continuar? [S/N]'))
  if resp in 'Nn':
    break

for índece, valor in enumerate(list):
  if valor % 2 == 0:
    par.append(valor)
  elif valor % 2 == 1:
    ímpar.append(valor)
print(f'{list}')
print(f'Números pares {par}')
print(f'Números ímpares {ímpar}')
