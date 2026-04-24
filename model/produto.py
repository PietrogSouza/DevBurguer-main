from database.conexao import conectar

def capturando_produtos():

    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM produtos;")

    produto = cursor.fetchall()

    conexao.close()

    return produto

def capturando_destaques():

    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, produto, foto FROM produtos WHERE destaque = 1;")

    resultado = cursor.fetchall()

    conexao.close()

    return resultado

def capturando_produto(codigo: int):

    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade from produtos WHERE codigo = %s",[codigo])

    produto = cursor.fetchone()

    conexao.close()

    return produto
