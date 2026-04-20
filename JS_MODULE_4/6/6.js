const form = document.querySelector('form');



form.addEventListener('submit', async(e) => {
    e.preventDefault();
    const value_from_input = document.querySelector('#query').value
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${value_from_input}`)
    const jsonData = await response.json();

    const article = document.createElement('article');

    const joke = document.createElement('p');
    joke.textContent = (jsonData.result[0].value);


    article.appendChild(joke);
    document.body.appendChild(article)
})