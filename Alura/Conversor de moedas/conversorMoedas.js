var valorEmDolar = prompt("Digite o valor em dólar:");
valorEmDolar = parseFloat(valorEmDolar);
var cotacaoDoDolar = prompt("Digite a cotação do dólar:");
cotacaoDoDolar = parseFloat(cotacaoDoDolar);
if (isNaN(valorEmDolar) || isNaN(cotacaoDoDolar)) {
    alert("Por favor, insira valores numéricos válidos.");
} else {
    var valorEmReal = valorEmDolar * cotacaoDoDolar;
    valorEmReal = valorEmReal.toFixed(2);
    alert("O valor em reais é: " + valorEmReal);
}