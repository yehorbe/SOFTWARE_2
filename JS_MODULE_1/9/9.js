let num = parseInt(prompt('Enter the number'));

if (num <= 1) {
    alert(num + ' is not a prime number!');
} else {
    for (let i = 2; i <= (num)**0.5; i++) {
        if (num % i === 0) {
            alert(num + ' is not a prime number!');
            break;
        }
    } alert(num + ' is a prime number!');
}
