from database.conexao import conectar

def recuperar_carrinho(usuario:str)->list:
    conexao, cursor = conectar()

    cursor.execute("""
                     SELECT carrinhos.cod_carrinho, 
                        carrinhos.usuario, 
                        carrinhos.data, 
                        carrinhos.finalizado, 
                        produtos.produto, 
                        itens_carrinhos.quantidade, 
                        produtos.preco, 
                        produtos.foto 
                    FROM carrinhos
                    INNER JOIN itens_carrinhos ON carrinhos.cod_carrinho = itens_carrinhos.cod_carrinho
                    INNER JOIN produtos ON produtos.codigo = itens_carrinhos.cod_produto
                    WHERE carrinhos.usuario = %s;
                   """,[usuario])

    produto = cursor.fetchall()

    conexao.close()

    return produto
