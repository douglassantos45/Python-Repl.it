cateto_Oposto = float(input('Comprimento: '))
cateto_Adjacente = float(input('Comprimento: '))

hipotenusa = (cateto_Oposto ** 2 + cateto_Adjacente **2) ** (1/2)

print('A hipotenusa vai medir {}'.format(hipotenusa))


"""
import math

cateto_Oposto = float(input('Comprimento: '))
cateto_Adjacente = float(input('Comprimento: '))

hipotenusa = math.hypot(cateto_Oposto, cateto_Adjacente)

print('A hipotenusa vai medir {}'.format(hipotenusa))