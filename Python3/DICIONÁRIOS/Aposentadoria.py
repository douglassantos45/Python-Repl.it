from datetime import datetime
funcionario = dict()
funcionario['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
funcionario['idade'] = datetime.now().year - nasc
funcionario['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if funcionario['ctps'] == 0:
  for k, v in funcionario.items():
    print(f'{k} = {v}')
else:
  funcionario['contratação'] = int(input('Ano de Contratação: '))
  funcionario['salario'] = float(input('Salário: R$'))
  funcionario['aposentadoria'] = funcionario['idade'] + ((funcionario['contratação'] + 35) - datetime.now().year)
  
  print()

  for k, v in funcionario.items():
    print(f'{k} = {v}')