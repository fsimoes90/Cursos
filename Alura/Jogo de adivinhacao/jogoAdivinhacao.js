var numeroSecreto = parseInt(Math.random() * 1001);
var chute;
var tentativas = 0;

while (true) {
    chute = prompt('Digite um número entre 1 e 1000\nDigite "Esc" a qualquer momento para sair');
    
    if (chute.toLowerCase() === 'esc') {
        alert('Você saiu do jogo.');
        break;
    }

    if (isNaN(chute) || chute < 1 || chute > 1000) {
        alert('Por favor, digite um número válido entre 1 e 1000.');
        continue;
    }

    chute = parseInt(chute);
    tentativas++;

    if (chute === numeroSecreto) {
        alert('Parabéns! Você acertou o número secreto: ' + numeroSecreto + '\nNúmero de tentativas: ' + tentativas);
        break;
    } else {
        alert('Você errou.\nO número secreto é ' + (chute < numeroSecreto ? 'maior' : 'menor') + ' ' + chute + '. Tente novamente.\nNúmero de tentativas: ' + tentativas);
    }
}
