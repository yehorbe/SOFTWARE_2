candidates = []

let num = prompt('Enter the number of the candidates')
for (let i=0;i<num;i++) {
    let name = prompt('Enter the name of the candidate')
    candidates.push({
        name:name,
        votes:0
    })
}

let voters = prompt('Enter the number of the voters')
for (let i=0; i<voters; i++) {
    let vote_name = prompt('Enter the candidate You want vote for')
    let candidate = candidates.find(c => c.name === vote_name);
    if (candidate) {
        candidate.votes += 1;
    }
}
candidates.sort((a, b) => {
   return b - a;
})
console.log(`Winner is: ${candidates[0].name} with ${candidates[0].votes}`)

candidates.sort((a, b) => a-b);
console.log(candidates);