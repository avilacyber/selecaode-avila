"""
25/02/2024

=> App flask com dados apenas em memória <=

python -m venv .venv

source .venv/bin/activate         [Linux]
source .venv/Scripts/activate     [Windows]

pip install -r requirements.txt
or
pip install flask 

"""

from flask import Flask, render_template, request, redirect, url_for
from seunome import config

app = Flask(__name__)

dados = [[config['username']]]
lista = []

@app.get("/")
def home():
    return render_template("base.html", lista_front=lista, lista_dados=dados)


@app.post("/add")
def add():
    user = []    
    Seleção  = request.form.get("Seleção")
    Continente  = request.form.get("Continente")
    Titulos = request.form.get("Quantidade de Titulos")
    if Seleção != '' and Continente != '' and Titulos != '':        
        user.append(Seleção.strip())
        user.append(Continente.strip())
        user.append(Titulos.strip())
        lista.append(user)        
        print(f'Add: {lista}')                     
    else:
        print('** País nao cadastrato, todos os dados devem ser fornecidos **')    
    return redirect(url_for("home"))


@app.post("/sort")
def sort():
    if lista != []:
        print(f'** Ordenando a lista **')
        lista.sort()    
    return redirect(url_for("home"))


@app.post("/reverse")
def reverse():
    global lista   
    if lista != []:                
        print(f'** Invertendo a lista **')        
        lista = sorted(lista, reverse=True, key=lambda x: x[0])
    return redirect(url_for("home"))


@app.post("/clear")
def clear():
    global lista
    print(f'==> Apagando toda a lista <==')
    lista = []   
    return redirect(url_for("home"))


@app.get("/delete/<lista_nome>")
def delete(lista_nome):
    Seleção = lista_nome
    print(f'==> Removendo: {Seleção}')
    for i in range(len(lista)):
        if Seleção in lista[i]:            
            del lista[i]
            break   
    return redirect(url_for("home"))
       

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
