print("cadastro ")
rep = False
while rep == False:
    try:
        usuario=str(input("Digite seu nome completo?: "))
        ano=int(input("seu ano de  nascimento?: "))
        nascimento=int(2022 - ano)
        (ano >=1922) and (ano<= 2021 )
        print(usuario, "tem " , nascimento , "anos! " )
        rep = True
    except:
        
        print("erro!" )
        print("digite dados validos ")
    
 





   