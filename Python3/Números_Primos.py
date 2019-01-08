num = int(input('>>> '))
for i in range(1,num+1):
  if num % i == 0:
    print('\033[34m', end=' ') #\033[34m faixa de cores
  else:
    print('\033[m', end=' ')
  print(i, end=' ')