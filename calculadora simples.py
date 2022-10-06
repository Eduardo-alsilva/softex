
def  calculadora ( numero1 , numero2 , operacao ):
    if ( operação  ==  1 ):
        resultado  =  float ( print ( numero1  +  numero2 ))
    elif ( operacao  ==  2 ):
       resultado  =  float ( print ( numero1  -  numero2 ))
    elif ( operacao  ==  3 ):
       resultado  =  float ( print ( numero1  *  numero2 ))
    elif ( operacao  ==  4 ):
       resultado  =  float ( print ( numero1  /  numero2 ))
    elif ( operação  > 4 ):
     print ( "Operação invalida" )

print ( "soma-1 \n " , "subtração-2 \n " , "multiplicação-3 \n " , "divisão-4 \n " )
operacao =  int ( input ( "digite a operação: " ))
numero1 =  float ( input ( "Digite um numero: " ))
numero2 =  float ( input ( "Digite um numero: " ))
calculadora ( numero1 , numero2 , operacao )