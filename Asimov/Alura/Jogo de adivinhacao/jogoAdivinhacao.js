var numeroSecreto = 581;
var chute = prompt('Digite um número entre 1 e 1000');

while (chute != numeroSecreto) {
    if (chute < numeroSecreto) {
        alert('Você errou. O número é maior. Tente novamente.');
    } else if (chute > numeroSecreto) {
        alert('Você errou. O número é menor. Tente novamente.');
    }
    chute = prompt('Digite um número entre 1 e 1000');
}

alert('Parabéns! Você acertou o número secreto: ' + numeroSecreto);