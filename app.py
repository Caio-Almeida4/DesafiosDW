from flask import Flask, render_template, url_for
app = Flask("__name__", static_folder="./static")

# @app.route("/") # criando rotas com decorator
# def hello_world(): # função para retornar uma mensagem 
#     return"<p>Hello, Flask!</p>"

@app.route("/") # criando rotas com decorator
def index(): # função para retornar uma mensagem 
    return render_template("index.html")

@app.route("/contato") # criando rotas com decorator
def contato(): # função para retornar uma mensagem 
    return render_template("contato.html")

@app.route("/quem_somos") # criando rotas com decorator
def quem_somos(): # função para retornar uma mensagem 
    return render_template("quem_somos.html")
