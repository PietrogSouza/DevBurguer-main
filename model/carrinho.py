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


def inserir_item(usuario,cod_produto, quantidade=1):
    conexao, cursor = conectar()

    cursor.execute("""
                    SELECT cod_carrinho FROM carrinhos
                    WHERE usuario = %s
                    AND finalizado = 0
                    LIMIT 1;

                   """,[usuario])
    
    resultado_carrinho = cursor.fetchone()

    if resultado_carrinho:
        codigo_carrinho = resultado_carrinho["cod_carrinho"]
    else:
        cursor.execute("""
                        INSERT INTO carrinhos (usuario)
                        VALUES (%s);

                        """,[usuario])
        codigo_carrinho = cursor.lastrowid

        cursor.execute("""
                        INSERT INTO itens_carrinhos
                                (cod_carrinho, cod_produto, quantidade)
                        VALUES
                                (%s, %s, %s);

                        """,[codigo_carrinho, cod_produto, quantidade])
    conexao.commit()
    cursor.close()

    
    
