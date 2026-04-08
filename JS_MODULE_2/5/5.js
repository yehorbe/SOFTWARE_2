nums=[]

let num = prompt('Enter the number:');
while (! nums.includes(num)) {
    nums.push(num);
    num = prompt('Enter the number:');
}
nums.sort((a, b) => a-b);
console.log(nums);