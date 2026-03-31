let number_of_dices = parseInt(prompt('Enter the number of dices: '));
let number_from_dices = parseInt(prompt('Enter the number from dices: '));
let counter = 0;
let roll = 0;

while (roll < 10000) {
    let totalSum = 0;
    for (let i = 0; i < number_of_dices; i++) {
        let diceNumber = Math.floor(Math.random() * 6) + 1;
        totalSum += diceNumber;
    }
    roll += 1;
    if (totalSum === number_from_dices) {
        counter += 1;
    }
}
let chance = counter / 10000;
document.querySelector('#result').innerHTML = 'Possibility is ' + chance + '!';
