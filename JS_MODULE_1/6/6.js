const answer = confirm('Should I calculate the square root?')
if (answer) {
    let number = parseInt(prompt('Enter the number'))
    if (number>0) {
        let result = (number)**0.5
        alert(`Square root of ${number} is ${result}`)
        } else {document.querySelector('#target').innerHTML='The square root of a negative number is not defined'}
} else {alert('The square root is not calculated.')}