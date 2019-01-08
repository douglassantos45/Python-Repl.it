list = []

for contador in range(0,5):
  n = int(input('\ndigite um número: '.title()))

  if contador == 0 or n > list[-1]:#list[-1] significa valor maior que o ultimo
    list.append(n)
    print('\nAdicionado ao final da lista')

  else:
    posicao = 0
    
    while posicao < len(list):
      if n <= list[posicao]:
        list.insert(posicao, n)
        print('\nFoi adicionado na {posicao}')
        break
      posicao += 1

print('\nPosição {}'.format(list))