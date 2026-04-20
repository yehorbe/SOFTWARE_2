let start_year = parseInt(prompt('Enter the start year'));
let end_year = parseInt(prompt('Enter the end year'));

let leap_years = '<ul>';

for (let i = start_year; i<=end_year; i++) {
    if ((i % 4 === 0 && i % 100 !== 0) || (i % 400 === 0)) {
            leap_years += `<li>${i}</li>`;
    }
}
leap_years += '</ul>'
document.querySelector('#target').innerHTML = leap_years;