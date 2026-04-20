let num = parseInt(prompt('Enter the number'));
nums = [];
while (num !== 0) {
    nums.push(num);
    num = parseInt(prompt('Enter the number'));
}
nums.sort((a,b)=>b-a);
console.log(nums);