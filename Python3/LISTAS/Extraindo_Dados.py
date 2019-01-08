valores = []

while True:
  valores.append(int(input('\nInforme um número: ')))
  resp = str(input('\nDeseja continuar? [s] ou [n]'))
  if resp in 'Nn':
    break

print(f'\nVocê digitou {len(valores)} números')
valores.sort(reverse=True)
print(f'Os números na ordem decrescente')

for i in valores:
  print(i)

if 5 in valores:
  print('\nO valor 5 está na lista')
