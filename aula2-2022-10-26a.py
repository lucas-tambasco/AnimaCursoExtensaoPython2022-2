# comando de entrada
nome = input("Digite seu nome: ")

# comando de saida
print(nome)

idade = int(input("Digite a sua idade: "))
print(f"Sua idade é {idade}")

# mostrar o dobro da idade
dobro = idade * 2
print(dobro)

if idade >= 18:
  print("você é maior de idade, pode dirigir ou beber")
else:
  print("você é menor, volta a estudar")

genero = input("Informe o gênero M=Masculino, F=Feminino: ")

if (idade >= 18 and genero == "M"):
  print("E você também precisa/presisou prestar o serviço militar obrigatório")