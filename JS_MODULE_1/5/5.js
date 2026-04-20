let year = parseInt(prompt('Enter the year'))
if ((year % 4 === 0 && year % 100) || (year % 400 === 0)) {
            alert('Your year is a leap year')
}
