
def calculadora (numero1, numero2, operacao):
    if (operacao == 1):
        resultado = (print(numero1 + numero2))
    elif(operacao == 2):
       resultado = (print (numero1 - numero2))
    elif(operacao == 3):
       resultado = (print (numero1 * numero2))
    elif(operacao == 4):
       resultado = (print (numero1 / numero2))
   
operacao =1

while operacao:
   print("soma-1\n" ,"subtração-2\n" , "multiplicação-3\n" , "divisão-4\n" , "sair-0\n" )

   operacao = int(input('\nOperador: '))
   if (operacao==0):
      print("calc finalizada")
      exit()
   elif (operacao>=1 or operacao<=4):
      numero1= float(input("Digite um numero: "))
      numero2= float(input("Digite um numero: "))
      calculadora (numero1, numero2, operacao)
   else:
      print("invalido")


