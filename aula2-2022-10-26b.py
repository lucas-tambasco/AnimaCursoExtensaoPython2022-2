nome = input("Informe seu nome: ")
nota = int(input("Digite sua nota: "))
if (nota == 10):
  print(f"{nome}, você é o cara mais incrivel que eu conheço!!")
elif (nota >= 6 and nota < 10):
  print("{}, bom trabalho!".format(nome))
else:
  print("Burroooooo!!!!!!!!!")