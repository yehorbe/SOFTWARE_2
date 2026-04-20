let array = ['Johnny', 'DeeDee', 'Joey', 'Marky']
const concat = (x) => (document.querySelector('#target').innerHTML = x)
let result = '';
for (const name of array) {
    result += name + '';
}
concat(result)