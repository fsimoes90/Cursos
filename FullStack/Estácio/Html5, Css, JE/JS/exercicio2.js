// Função para verificar se um número é inteiro positivo
function isPositiveInteger(num) {
    return Number.isInteger(num) && num > 0;
  }
  
  // Função para solicitar um número inteiro positivo ao usuário
  function getInput(promptText) {
    let input;
    do {
      input = parseInt(prompt(promptText));
    } while (!isPositiveInteger(input));
    return input;
  }
  
  // Solicitar ao usuário que insira dois números inteiros positivos
  const num1 = getInput("Digite o primeiro número inteiro positivo: ");
  const num2 = getInput("Digite o segundo número inteiro positivo: ");
  
  // Dividir os dois números
  const resultado = num1 / num2;
  
  // Imprimir o resultado da divisão
  console.log(`O resultado da divisão de ${num1} por ${num2} é: ${resultado}`);
  