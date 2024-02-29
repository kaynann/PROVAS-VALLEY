export class Veiculo {
  constructor(marcaVeiculo, tipoVeiculo, modeloVeiculo, valorServico, placa, cor, prazo) {
    this.marcaVeiculo = marcaVeiculo;
    this.tipoVeiculo = tipoVeiculo;
    this.modeloVeiculo = modeloVeiculo;
    this.valorServico = valorServico;
    this.placa = placa;
    this.cor = cor;
    this.prazo = prazo;
  };

  get getMarcaVeiculo() {
    return this.marcaVeiculo;
  };

  get getTipoVeiculo() {
    return this.tipoVeiculo
  };

  get getModeloVeiculo() {
    return this.modeloVeiculo;
  };

  get getPlaca() {
    return this.placa;
  };

  get getValorServico() {
    return this.valorServico;
  };

  get getCor() {
    return this.cor;
  };

  get getPrazo() {
    return this.prazo;
  };

  get getModelo() {
    return this.tipoVeiculo;
  };

// SET's
  set setMarcaVeiculo(novaMarca) {
    this.marcaVeiculo == novaMarca;
    return this.marcaVeiculo;
  };

  set setTipoVeiculo(novoTipo) {
    this.tipoVeiculo = novoTipo;
    return this.tipoVeiculo;
  };

  set setModeloVeiculo(novoModelo) {
    this.modeloVeiculo = novoModelo;
    return this.modeloVeiculo;
  };

  set setPlaca(novaPlaca) {
    this.placa = novaPlaca;
    return this.placa;
  };

  set setValorServico(novoValor) {
    this.cor = novoValor;
    return this.novoValor;
  };

  set setCor(novaCor) {
    this.cor = novaCor;
    return this.cor;
  };

  set setPrazo(novoPrazo) {
    this.prazo = novoPrazo;
    return this.prazo;
  };

  set setModelo(novoTipo) {
    this.tipoVeiculo = novoTipo;
  };

// MÉTODOS
  dentroDoPrazo() {
    this.prazo = true;
  };

  foraDoPrazo() {
    this.prazo = false;
  };

  validaPrazo() {
    if (this.prazo === true) {
        console.log('O veículo foi entregue no prazo');
    } else {
        console.log('O veículo foi entregue fora do prazo');
    };
  };
};