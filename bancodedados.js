const  mysql  =  requer ( 'mysql2' ) ;

 conexão  const =  mysql . criarConexão ( {
  host : 'localhost' ,
  usuário : 'nome de usuário' ,
  senha : 'senha' ,
  banco de dados : 'banco de dados'
} ) ;

conexão . conectar ( ( err )  =>  {
  if  ( err )  {
    console . log ( `Erro ao conectar ao banco de dados: ${ err . message } ` ) ;
  }  senão  {
    console . log ( "Conexão com o banco de dados estabelecido com sucesso!" ) ;
  }
} ) ;