fetch("../list.json")
  .then((res) => res.json())
  .then((data) => {
    data.profiles.forEach((element) => {
      cardsset.insertAdjacentHTML(
        "beforeend",
        `  <div class="card">
        <div class="imgBx">
            <img src=${element.avatarUrl} alt="images">
        </div>
        <div class="details">
            <h2>${element.name}</h2>
            <a id="socials" href="https://github.com/${element.github}">
              <i class="fa-brands fa-github"></i>
          </a>
          <a id="socials" href="https://twitter.com/${element.twitter}">
              <i class="fa-brands fa-twitter"></i>
          </a> 
        </div>
      </div>`
      );
    });
  });

