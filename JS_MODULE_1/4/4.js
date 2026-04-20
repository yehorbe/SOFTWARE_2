let name=prompt('Enter the name');
let classes = Math.floor(Math.random() * 4) + 1;
if (classes === 1) {
    alert(`${name} you are Gryffindor`);
} else if (classes === 2) {
    alert(`${name} you are Slytherin`);
} else if (classes === 3) {
    alert(`${name} you are Hufflepuff`);
} else if (classes === 4) {
    alert(`${name} you are Ravenclaw`);
}
