tupla = ('Lápis',1.54,'Borracha',1,'Caderno',23.54,
'Livro',45.23,'Mochila', 56.45,'Lápis-de-Cor', 3.64)

print('-='*20 + '\n' + f'{"Lista de perços".upper():^40}' + '\n' + '-='*20 + '\n')

for x in range(len(tupla)):
  if x % 2 == 0:
    print(f'{tupla[x]:.<30}', end = '')
    
  else:
    print(f'R${tupla[x]:>7.2f}')