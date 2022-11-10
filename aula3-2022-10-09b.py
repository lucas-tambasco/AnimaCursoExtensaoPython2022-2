def caucular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

preco = 299
print(caucular_imposto(preco))

valores = [1.99, 24.50, 78.27, 1515.5]

for valor in valores:
  print(f"O imposto de {valor} é {caucular_imposto(valor)}") 

def caucular_imposto_aliquota(valor, aliquota = 7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {caucular_imposto_aliquota(valor)}") 

for valor in valores:
  print(f"O imposto de {valor} é {caucular_imposto_aliquota(valor, 10)}") 
