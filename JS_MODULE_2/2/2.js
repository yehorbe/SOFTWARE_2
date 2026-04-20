let num = parseInt(prompt('Enter the number of the participants'));
let participants = [];

for (let i = 0; i < num; i++) {
    let name = prompt('Enter the name');
    participants.push(name);
}

participants.sort();

let p_list = '<ol>';
for (let i = 0; i < participants.length; i++) {
    p_list += `<li>${participants[i]}</li>`;
}
p_list += '</ol>';

document.querySelector('#target').innerHTML = p_list;