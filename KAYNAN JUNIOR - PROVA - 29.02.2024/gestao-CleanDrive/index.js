import { Cliente } from "./Cliente.js";

let cliente01 = new Cliente('João', 'Centro - Praça Coronel Antônio Belo - N°189', 'Honda', 'Moto', 'FAN 160', 30,'GFE-5780', 'Branca','2h');

console.table(cliente01)
cliente01.dentroDoPrazo()
cliente01.validaPrazo()
cliente01.pagar(40)
console.log(cliente01.valorServico)