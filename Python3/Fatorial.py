print('Fatorando um número')
num = int(input('\nInforme um número: '))
c = num
f = 1
while c > 0:
  print(f'{c}', end=' ')
  print(' x ' if c > 1 else ' = ', end=' ')
  f *= c
  c -= 1
print(f'{f}', end=' ')

"""
print('Fatorando um número')
num = int(input('\nInforme um número: '))
c = num
f = 1
for i in range(c):
  print(f'{c}', end=' ')
  print(' x ' if c > 1 else ' = ', end=' ')
  f *= c
  c -= 1
print(f'{f}', end=' ')
"""