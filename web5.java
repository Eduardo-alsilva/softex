const soap = require('soap');

// URL do WSDL do serviço dos Correios
const url = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl';

// Método que será chamado no serviço dos Correios
const method = 'consultaCEP';

// Parâmetros do método
const args = { cep: '70002900' };

// Realiza a chamada ao serviço SOAP dos Correios
soap.createClient(url, (err, client) => {
  if (err) {
    console.error(err);
  } else {
    client[method](args, (err, result) => {
      if (err) {
        console.error(err);
      } else {
        console.log(result);
      }
    });
  }
});
