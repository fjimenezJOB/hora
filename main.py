from flask import Flask, render_template, redirect, url_for, request
import csv
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


def escribir(methods=['POST']):

    data = json.loads(request.cookies.get('data'))

    fecha = data.get('fecha')
    dinero = data.get('dinero')
    horas = data.get('horas')
    lugar = data.get('lugar')

    with open('registro.csv', 'a') as f:
        f.write(f'{fecha},{dinero},{horas},{lugar}\n')
        f.close()


@app.route('/registro')
def registro(fecha='00/00/00', dinero=0, horas=0, lugar=""):
    return render_template('registro.html')


@app.route('/enviar', methods=['POST'])
def enviar():
    response = redirect(url_for('home'))
    response.set_cookie('data', json.dumps(dict(request.form.items())))
    escribir()
    return response


@app.errorhandler(404)
def error(error):
    return '<h1> Pagina no encontrada...(404)<h1>'


if __name__ == "__main__":
    app.run('0.0.0.0', '5000', debug=True)
