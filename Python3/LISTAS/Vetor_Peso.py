galera = list()
dados = list()

for i in range(0,3):
  dados.append(str(input('Informe seu nome: ')))
  dados.append(int(input('Informe seu peso: ')))
  galera.append(dados[:])
  dados.clear()

for p in galera:
  if p[1] > 10:
    print('doidor')
    
print(galera)