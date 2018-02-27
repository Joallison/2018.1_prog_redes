valorsacado = int(input('Olá digite o valor a ser sacado: R$'))
total = valorsacado
ced = 100
totalcedulas = 0
while True:
  if total >= ced:
    total -= ced
    totalcedulas += 1
  else:
    if totalcedulas > 0:
      print "Total de %s cédulas de R$ %s" % (totalcedulas, ced)
    if ced == 100:
      ced = 50
    elif ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 5
    elif ced == 5:
      ced = 2
    totalcedulas = 0
    if total == 0:
      break
print('Obrigado!')
