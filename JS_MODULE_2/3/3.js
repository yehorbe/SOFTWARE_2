let first_list = [];
for (let i =0; i<6; i++) {
    let name = prompt('Enter the dogs name');
    first_list.push(name);
}
first_list.sort().reverse();

let second_list = '<ul>';
for (let i=0; i<6; i++) {
    second_list += `<li>${first_list[i]}</li>`;
}
second_list += '</ul>';

document.querySelector('#target').innerHTML = second_list;