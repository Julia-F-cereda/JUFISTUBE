import mysql.connector

conexao_banco = "LOCAL"

def conectar():
        if conexao_banco == "LOCAL":
        
            conexao = mysql.connector.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password= "root",
                    database= "jufisTube"
                )
        else:
              conexao = mysql.connector.connect(
                    host="server-juliafiscarellicereda-julia-fiscarelli-cereda.a.aivencloud.com",
                    port=23810,
                    user="23810",
                    password= "AVNS_C-gZuerDKRNTQmnP_zp",
                    database= "defaultdb"
                )
              
            #criando cursor
        cursor = conexao.cursor(dictionary=True)

        return conexao, cursor
        