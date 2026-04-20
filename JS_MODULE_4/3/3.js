const form = document.querySelector('form');
const res = document.getElementById('results');


form.addEventListener('submit', async(e) => {
    e.preventDefault();
    res.innerHTML='';
    try {
        const query = document.querySelector('#query').value;
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
        const jsonData = await response.json();

        jsonData.forEach(jsonData => {
            const article = document.createElement('article');

            const head = document.createElement('h2');
            head.textContent = jsonData.show.name;

            const link = document.createElement('a');
            link.href = jsonData.show.url;
            link.target = '_blank';
            link.textContent = 'Detail';

            const picture = document.createElement('img')
            picture.src = jsonData.show.image?.medium;
            picture.alt = jsonData.show.name;

            const summary = document.createElement('div')
            summary.innerHTML = jsonData.show.summary;

            article.appendChild(head);
            article.appendChild(link);
            article.appendChild(picture);
            article.appendChild(summary);

            res.appendChild(article);
        });
    } catch (error) {
        console.log(error.message);
    }
})