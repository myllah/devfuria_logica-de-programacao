# -*- coding: utf-8 -*-

#Escreva um algoritmo que armazene o valor 999 na variável a e o valor 555 na variável b.
#A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo
#com que o valor que está em a passe para b e vice-versa.

# Variáveis #
a = 999
b = 555

#  Sua lógica

temp = a
a = b
b = temp

# Testes #
assert a == 555
assert b == 999
