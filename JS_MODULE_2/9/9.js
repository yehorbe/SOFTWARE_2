let array = [1, 2, 3, 4, 5, 6];
let evenNums = [];
function even(x) {
    for (const num of x) {
        if (num%2===0) {
            evenNums.push(num)
        }
    }
}
even(array)
console.log(array)
console.log(evenNums)