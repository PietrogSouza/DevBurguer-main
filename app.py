from flask import Flask, render_template, request, redirect, session
from model.produto import capturando_produtos, capturando_destaques, capturando_produto 
from model.usuarios import Usuarios

app = Flask(__name__)

app.secret_key = "banana_loca"

@app.route("/")
def pagina_principal():

    produtos = capturando_produtos()
    destaques = capturando_destaques()

    return render_template("index.html", produtos = produtos, destaques = destaques)

@app.route("/pagina2/<codigo>")
def pagina_pagina2(codigo):

    rcp = capturando_produto(codigo)

    return render_template("pagina2.html", rcp = rcp)

@app.route("/cadastrar", methods=["GET"])
def cadastrar():
    
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get ("nome")

    novo_usuario = Usuarios(usuario, senha, nome)
    novo_usuario.cadastrar()

    return render_template("/login.html")

@app.route("/login/usuario", methods=["POST"])
def pagina_login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    resultado = usuario.logar(usuario, senha)
    return render_template("login.html")

    if not resultado:
        session["usuario_logado"] = resultado
        return redirect()
    
@app.route('/carrinho')
def ver_carrinho():
    # Pega a lista de produtos da sessão, ou uma lista vazia se não houver nada
    itens = session.get('carrinho', [])
    
    # Calcula o total (convertendo para float se necessário)
    total = sum(float(str(item['preco']).replace(',', '.')) for item in itens)
    
    return render_template('carrinho.html', carrinho=itens, total=f"{total:.2f}".replace('.', ','))



if __name__=="__main__":
    app.run(debug=True)