const dice = () => Math.floor(Math.random() * 6) + 1;
let nums = '<ul>';
let result = 0;
while (result !== 6) {
    result = dice();
    nums += `<li>${result}</li>`;
}
nums += '</ul>'
document.querySelector('#target').innerHTML = nums