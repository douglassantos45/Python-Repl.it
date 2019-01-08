def soma(*valores):
  s = 0 #quantidade a ser mostrada
  for num in valores:
    s += num
  print(f'Somando os valores {valores} temos {s}')

soma(4,5)