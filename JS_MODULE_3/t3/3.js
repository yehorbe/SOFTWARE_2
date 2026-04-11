'use strict';
const target = document.getElementById('target');
const names = ['John', 'Paul', 'Jones'];
for (let i=0; i<names.length; i++) {
    const li = document.createElement('li');
    target.appendChild(li);
    li.textContent = names[i];
}