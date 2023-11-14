var numeroSecreto = parseInt(Math.random() * 1001);
var chute;

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
    if (chute === numeroSecreto) {
        alert('Parabéns! Você acertou o número secreto: ' + numeroSecreto);
        break;
    } else if (chute < numeroSecreto) {
        alert('Você errou. O número é maior. Tente novamente.');
    } else {
        alert('Você errou. O número é menor. Tente novamente.');
    }
}
