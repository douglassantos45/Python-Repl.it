aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if 5 <= aluno['media'] < 7:
  aluno['situação'] = 'Recuperação'
elif aluno['media'] >= 7:
  aluno['situação'] = 'Aprovado'
else:
  aluno['situação'] = 'Reprovado'
  
print(f'Nome é igual a {aluno["nome"]}\nMédia é igual a {aluno["media"]}\nSituação é igual a {aluno["situação"]}')  


