ano = int(input(" digite um ano: ".title()))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
     print ('\n O ano informado é Bissexto: ',ano)
else:
    print ('\n O ano informado não é Bissexto: ',ano)
