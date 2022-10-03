Rodas= int(input("Digite a quantidade de rodas: "))
peso= float(input("Qual o peso do veiculo: "))
pessoas= int(input("Quantas pessoas comporta o veiculo: "))

if (Rodas <=3):
    print("categoria A ")
elif(Rodas == 4 and pessoas <= 8 and peso <= 3500):
    print("categoria B ")
elif(Rodas >=4 and peso >=3501 and peso<=6000 ):
    print("Categoria C ")
elif(Rodas >=4 and pessoas > 8):
    print("Categoraia D ")
elif(Rodas >=4 and peso >= 6000 ): 
    print("Categoria E ")
else: 
    print("sem categoria ")
