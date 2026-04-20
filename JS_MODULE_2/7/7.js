let sideNum=parseInt(prompt('Enter the number of the sides'))
const dice = (x) => Math.floor(Math.random() * x) + 1;
let nums = '<ul>';
let result = 0;
while (result !== sideNum) {
    result = dice(sideNum);
    nums += `<li>${result}</li>`;
}
nums += '</ul>'
document.querySelector('#target').innerHTML = nums