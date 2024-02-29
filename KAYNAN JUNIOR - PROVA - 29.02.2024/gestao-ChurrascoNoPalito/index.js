// O Churrasco no Palito quer você para fazer o controle dos pedidos dos clientes. Onde é possivel anotar o nome e pedido do cliente e dizer o valor da conta.

const pedido = {
  pedido: 'pedido do cliente',
  totalPessoasPedido: 'total de pessoas para o pedido',
  valorPedido: 'valor do pedido do cliente',
};

const cliente = {
  nome: 'nome do cliente',
  mesa: 'mesa do cliente',
  pagar: function(valorPago) {
    if (this.valorPedido > valorPago ) {
        this.valorPedido -= valorPago;
        console.log(`O cliente pagou R$${ valorPago }, ainda faltam R$${ this.valorPedido }`)
        return this.valorPedido;
    } else if(this.valorPedido < valorPago) {
        console.log(`O cliente pagou R$${ valorPago }, de R$${ this.valorPedido } o troco dele é R$${ valorPago -= this.valorPedido }`);
        this.valorPedido -= this.valorPedido;
        return this.valorPedido
    } else if (this.valorPedido === valorPago) {
        console.log(`O cliente pagou a conta completa.`);
        this.valorPedido -= valorPago
        return this.valorPedido
    } else {
      console.log('Não foi possível identificar o pagamento');
    };
  }
};


Object.setPrototypeOf(cliente, pedido);
cliente.nome = 'João';
cliente.mesa = 10;
cliente.pedido = 'Arroz com camarão';
cliente.totalPessoasPedido = 1;
cliente.valorPedido = 40;
console.log(cliente);
console.log();
cliente.pagar(40);
console.log();
console.log(cliente.valorPedido);