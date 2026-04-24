function mostrar_carrinho() {
    const reesposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")

    if (reesposta.ok) {
        alert("ERRO AO CARREGAR CARRINHO!")
    }
    else {
        const dados = await resposta.json()

        const carrinho = document.getElementById("carrinho")

        carrinho.innerHTML = "";

        for (let dado of dados) {

            total += dado.preco

            let linha = ` <img src= "${dado.foto}" alt="Classic Dev" class="card__image"/>
              </div>
                <div class="card__body">
                    <h3 class="card__title">${dado.produto}</h3>
                    <p class="card__description"> {{produto.descricao}} </p>
                <div class="card__footer">
                    <span class="card__price">R${dado.preco}}</span>
                    <button class="button button--small"><a href="/detalhes_produto/{{ produto.codigo }}">Comprar</a></button>
                </div>
              </div>`

            carrinho.innerHTML += linha
        }
        document.querySelector(".cart-item__price").textContent = "R$" + total
    }
}

mostrar_carrinho()