'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
const targetElement = document.querySelector('#target');

for (const student of students) {
  targetElement.innerHTML += `<option value="${student.id}">${student.name}</option>`;
}