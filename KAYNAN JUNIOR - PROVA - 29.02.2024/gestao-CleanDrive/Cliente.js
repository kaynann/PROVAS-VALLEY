import { Veiculo } from "./Veiculos.js";

export class Cliente extends Veiculo {
  constructor(nome, endereco, marcaVeiculo, tipoVeiculo, modeloVeiculo, valorServico, placa, cor, prazo) {
    super(marcaVeiculo, tipoVeiculo, modeloVeiculo, valorServico, placa, cor, prazo);
    this.nomeCliente = nome;
    this.endereco = endereco;
  };

// GET´s
  get getNome() {
    return this.nomeCliente;
  };

  get getEndereco() {
    return this.endereco;
  };

  get getPrazo() {
    return this.prazo;
  };

// SET's
  set setNome(novoNome) {
    this.nomeCliente = novoNome;
    return this.nomeCliente;
  };

  set setEndereco(novoEndereco) {
    this.endereco = novoEndereco;
    return this.endereco;
  };

// MÉTODOS
  pagar(valorPago) {
    if (this.valorServico > valorPago ) {
        this.valorServico -= valorPago;
        console.log(`O cliente pagou R$${ valorPago }, ainda faltam R$${ this.valorServico }`)
        return this.valorServico;
    } else if(this.valorServico < valorPago) {
        console.log(`O cliente pagou R$${ valorPago }, de R$${ this.valorServico } o troco dele é R$${ valorPago -= this.valorServico }`);
        this.valorServico -= this.valorServico;
        return this.valorServico
    } else if (this.valorServico === valorPago) {
        console.log(`O cliente pagou a conta completa.`);
        this.valorServico -= valorPago
        return this.valorServico
    } else {
      console.log('Não foi possível identificar o pagamento');
    };
 }
};