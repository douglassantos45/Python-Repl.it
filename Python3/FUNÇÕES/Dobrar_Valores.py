def dobra(list):
  pos = 0
  while pos < len(list):
    list[pos] *= 2
    pos += 1
    
valores = [5, 3, 7, 1, 5]
dobra(valores)
print(valores)