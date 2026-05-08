async function mostrar_carrinho() {
    const resposta = await fetch("/api/get/carrinho")

    if (!resposta.ok) {
        alert("ERRO AO CARREGAR CARRINHO!")
    }
    else {
        const dados = await resposta.json()

        const carrinho = document.querySelector(".cart-sidebar__content")



        for (let dado of dados) {

            total += dado.preco

            let linha = `
            <div>
            <img src= "${dado.foto}" alt="Classic Dev" class="card__image"/>
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

async function inserirItemCarrinho(usuario, cod_produto, quantidade=1) {
    const resposta = await fetch("/api/post/item_carrinho",
                                    {
                                        method:"POST",
                                        headers:{
                                                    "Content-Type": "application/json"
                                                },
                                        body: JSON.stringify(

                                                                {
                                                                "cod_produto" :cod_produto,
                                                                "quantidade" : quantidade
                                                                }
                                                            )
                                    }

                                 )

    if (resposta.ok)
    {
        alert("Erro ao inserir Item")
    }

    mostrar_carrinho()

}