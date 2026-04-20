const form = document.querySelector('form');


form.addEventListener('submit', async(e) => {
    e.preventDefault();
    try {
        const query = document.querySelector('#query').value;
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
        const jsonData = await response.json();
        console.log(jsonData[0].show.name, jsonData[0].show.genres, jsonData[0].show.language, jsonData[0].show.network.country.name)
    } catch (error) {
        console.log(error.message)
    }
})