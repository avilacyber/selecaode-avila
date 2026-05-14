from flask import Flask, render_template, request, redirect, url_for
from seunome import config

app = Flask(__name__)

dados = [[config['username']]]
lista = []


@app.get("/")
def home():
    return render_template(
        "base.html",
        lista_front=lista,
        lista_dados=dados
    )


@app.post("/add")
def add():

    user = []

    selecao = request.form.get("Selecao")
    continente = request.form.get("Continente")
    titulos = request.form.get("Titulos")

    if selecao != '' and continente != '' and titulos != '':

        user.append(selecao.strip())
        user.append(continente.strip())
        user.append(titulos.strip())

        lista.append(user)

        print(f'Add: {lista}')

    else:
        print('Todos os dados devem ser preenchidos')

    return redirect(url_for("home"))


@app.post("/sort")
def sort():

    if lista != []:
        lista.sort()

    return redirect(url_for("home"))


@app.post("/reverse")
def reverse():

    global lista

    if lista != []:
        lista = sorted(lista, reverse=True, key=lambda x: x[0])

    return redirect(url_for("home"))


@app.post("/clear")
def clear():

    global lista

    lista = []

    return redirect(url_for("home"))


@app.get("/delete/<nome>")
def delete(nome):

    for i in range(len(lista)):

        if nome in lista[i]:
            del lista[i]
            break

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
