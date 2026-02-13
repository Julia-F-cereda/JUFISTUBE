from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/home", methods=["GET"])
@app.route("/")
def pg_principal():

    #conectando no bd
    conexao = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password= "root",
        database= "jufisTube"
    )
    #criando cursor
    cursor = conexao.cursor(dictionary=True)

    #executando a consulta       
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica") 

    musicas = cursor.fetchall()                                                                                                                       

    #fechando a conexao
    conexao.close()


    return render_template("principal.html", musicas = musicas)


@app.route("/administracao")
def pg_administracao():
    return render_template("administracao.html")


if __name__ == "__main__":
    app.run(debug=True)
