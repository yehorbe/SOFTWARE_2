const numbers = [];
const count = 5;

for (let i = 0; i < count; i++) {
    const input = prompt('Enter the number:');
    const num = Number(input);
    numbers.push(num);
}

numbers.sort((a, b) => b - a);

console.log(numbers);
