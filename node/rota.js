var  expresso  =  requer ( 'expresso' ) ;
var  rota  =  expresso . Roteador ( ) ;
 
rota . get ( '/users' ,  function ( req ,  res )  {
    res . send ( `Listar usuários` ) ;
} ) ;
 
rota . post ( '/user' ,  function ( req ,  res )  {
    res . send ( `Criar um usuário` ) ;
} ) ;
 
módulo . exporta  =  rota ;