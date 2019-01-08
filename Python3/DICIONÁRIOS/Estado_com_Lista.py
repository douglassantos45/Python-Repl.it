Brasil = []
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}


Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil[1]['sigla'])

"""
estado = dict()
brasil = list()

for c in range(0,2):
  estado['uf'] = str(input('Unidade Federativa: '))
  estado['sigla'] = str(input('Sigla do Estado: '))
  brasil.append(estado.copy())#Obrigatório

for estado in brasil:
  for valores in estado.values():
    print(valores, end=' ')
  print()

"""
