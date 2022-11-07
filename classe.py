classe  pessoa ():
    def  __init__ ( self , nome , peso ):
        próprio . _nome  =  nome
        próprio . _peso  =  peso

    def  exibir ( self ):
        print ( " \n Meu nome é" , self . _nome , "e eu ganhei" , self . _peso , "kg no último ano!!" )
        print ( "---------------------------------------------------------- ------------------------------------" )

    def  set_peso ( self , novo_peso ):
        próprio . _peso  -=  novo_peso

    def  get_nome ( self ):
        retornar  a si mesmo . _nome

    def  get_peso ( self ):
        retornar  a si mesmo . _peso

print ( "--------- Balança Python ---------" )
p1  =  pessoa ( input ( ' \n Qual o seu nome completo?: ' ), float ( input ( ' \n Qual o seu peso atual?: ' )))
p1 . get_nome ()
p1 . get_peso ()
p1 . set_peso ( float ( input ( ' \n Quantos kg você tinha ano passado?: ' )))
p1 . get_nome ()
p1 . get_peso ()
p1 . exibir ()

p2  =  pessoa ( input ( ' \n Qual o seu nome completo?: ' ), float ( input ( ' \n Qual o seu peso atual?: ' )))
p2 . get_nome ()
p2 . get_peso ()
p2 . set_peso ( float ( input ( ' \n Quantos kg você tinha ano passado?: ' )))
p2 . get_nome ()
p2 . get_peso ()
p2 . exibir ()