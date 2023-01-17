classe  Banco  {
    constructor ( conta ,  saldo ,  tipo Conta ,  agência )  {
      isso . conta  =  conta ;
      isso . saldo  =  saldo ;
      isso . tipoConta  =  tipoConta ;
      isso . agência  =  agência ;
    }

    buscar Saldo ( )  {
      devolva  isso . saldo ;
    }

    depósito ( valor )  {
      isso . saldo  +=  valor ;
      return  `Depósito realizado com sucesso. Novo saldo: ${ this . saldo } ` ;
    }

    saque ( valor )  {
      if  ( valor  >  this . saldo )  {
        return  "Saldo insuficiente para realizar saque." ;
      }  senão  {
        isso . saldo  -=  valor ;
        return  `Saque realizado com sucesso. Novo saldo: ${ this . saldo } ` ;
      }
    }

    numeroConta ( )  {
      devolva  isso . conta ;
    }
  }

  const  minhaConta  =  new  Banco ( 123456 ,  1000 ,  'corrente' ,  1234 ) ;
  console . log ( minhaConta.buscarSaldo ( ) ) ; _ _ // 1000 
  console . log ( minhaConta.depósito ( 500 ) ) ; _ _ // Depósito realizado com sucesso. Novo saldo: 1500 
  console . log ( minhaConta . saque ( 2000 ) ) ;  // Saldo insuficiente para realizar saque.
  console . log ( minhaConta . numeroConta ( ) ) ;  // 123456
