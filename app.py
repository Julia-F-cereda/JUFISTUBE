from flask import Flask, render_template, request, redirect, session
import mysql.connector
from model.musica import recuperar_musicas
from model.genero import recuperar_generos
from model.musica import salvar_musica
from model.musica import excluir_musica
from model.musica import ativar_musica
from model.cadastro import inserir_usuario
from model.cadastro import conferir_usuario

app = Flask(__name__)

app.secret_key = "chocolate"

@app.route("/home", methods=["GET"])
@app.route("/")

def pg_principal():
    musicas = recuperar_musicas(True)
    generos = recuperar_generos()



    return render_template("principal.html", musicas = musicas, generos = generos)


@app.route("/admin")
def pg_administracao():
    if "usuario_logado" not in session:
        return redirect ("/login")
    musicas = recuperar_musicas()
    generos = recuperar_generos()
    return render_template("administracao.html", musicas = musicas, generos = generos)

@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("input-nome")
    cantor = request.form.get("input-cantor")
    genero = request.form.get("input-genero")
    duracao = request.form.get("input-duracao")
    imagem = request.form.get("input-imagem")
    try:
        if salvar_musica(cantor, duracao, nome_musica, imagem, genero):
            return redirect("/admin")
        else: return "erro"
    except Exception as erro:
        print(erro)

@app.route("/musica/excluir_musica/<id>")
def api_excluir_musica(id):
    if excluir_musica(id):
        return redirect("/admin")
    else:
        return "erro"
    
@app.route("/musica/ativar_musica/<id>/<ativo>")
def api_ativar_musica( id,ativo):
    if ativar_musica(id,ativo):
        return redirect("/admin")
    else:
        return "erro"
    
@app.route("/cadastro")
def pg_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=["POST"])
def rota_cadastro():
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    try:
        if inserir_usuario(nome, senha):
            return redirect("/cadastro")
        else:
            pass
    except Exception as erro:
        print (erro)

@app.route("/login")
def login_usuario():
    if "usuario_logado" in session:
        return redirect ("/admin")
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def rota_login():
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    usuario = conferir_usuario(nome, senha)
    if usuario:
        session["usuario_logado"] = usuario
        return redirect("/admin")
    else:
        return redirect("/login")

@app.route("/logout")
def logout():
    return redirect("/admin")



if __name__ == "__main__":
    app.run(debug=True)
