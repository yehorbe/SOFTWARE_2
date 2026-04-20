let rolls = parseInt(prompt('Enter the number of rolls'));
let start_point = 0
for (let i=0; i<rolls; i++) {
    num = Math.floor(Math.random()*6)+1;
    start_point+=num
} document.querySelector('#target').innerHTML = `${start_point}`