from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask("__name__")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1212'
app.config['MYSQL_DB'] = 'desafiodw'

mysql = MySQL(app)

@app.route("/") # criando rotas com decorator
def index(): # função para retornar uma mensagem 
    return render_template("index.html")

@app.route("/contato", methods=['GET','POST']) 
def contato(): 

    if request.method =='POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        cur = mysql.connection.cursor()
        cur.execute(' INSERT INTO contato VALUES(%s,%s,%s)',(email,assunto,descricao))
        mysql.connection.commit()
        cur.close()
        return 'Oba'

    return render_template("contato.html")


@app.route("/quem_somos") 
def quem_somos(): 
    return render_template("quem_somos.html")

@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contato")

    if users > 0:
        userDetails = cur.fetchall()

    return render_template("users.html", userDetails=userDetails)