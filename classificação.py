monitor de classe:

	atributos:
		marca: caractere;
		cor: caractere;
		tamanho: real;
		resolução: caractere;
		conectado: lógico;

	métodos:
		exibir imagem;
		conectar;
		desconectar;

	instaciamento do objeto:
		monitor = monitor()
			monitor.marca = Samsung;
			monitor.cor = Preto;
			monitor.tamanho = 45,3cm X 24,5cm;
			monitor.resolucao = Full HD;
			monitor.conectado = Verdadeiro;

-------------------------------------------------- ----------------------------------------------

carro de classe:

	atributos:
		marca: caractere;
		modelo: caractere;
		ano: inteiro;
		automático: lógico;
		combustível: caractere;

	métodos:
		dirigente;
		acelerar;
		freiar;

	instaciamento do objeto:
		carro = carro()
			carro.marca = Chevrolet;
			carro.modelo = S10;
			carro.ano = 2010;
			carro.automático = Falso;
			carro.combustível = Diesel;

-------------------------------------------------- ----------------------------------------------

classe transacaoBancaria:

	atributos:
		banco: caractere;
		agência: inteiro;
		conta: real;
		transação: caractere;
		valor: real;

	métodos:
		pagar;
		transferir;
		receber;
		investir;
		emprestimo;
		saque;

	instaciamento do objeto:
		transacaoBancaria tb = transacaoBancaria()
			tb.banco = Banco do Brasil;
			tb.agencia = 0922;
			tb.conta = 4455888-9;
			tb.transacao = saque;
			tb.valor = 599,99;

-------------------------------------------------- ----------------------------------------------

aula estudar:

	atributos:
		andamento: real;
		local: caractere;
		disciplina: caractere;
		assunto: caractere;
		
	métodos:
		assistir;
		ler;
		escrever;
		exercícios;


	instanciamento do objeto:
		estudar = estudar()
			estudar.tempo = 2,50h;
			estudar.local = Faculdade;
			estudar.disciplina = Física;
			estudar.assunto = Mecânica dos fluidos;