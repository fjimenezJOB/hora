# IMPORTS DE LAS LIBRERIAS DE FLASK
from flask import Flask, render_template, redirect, url_for, request
# imports de otras librerias
import csv
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# Metodo para escribir en archivo.csv, la informacion llega a traves de una cookie que se genera en el navegador despues de darle a enviar.
def escribir(fecha='00/00/0000', dinero=0, horas=0, lugar=' '):

    info = json.loads(request.cookies.get('data'))#coje la informacion del json de la cookie.

    fecha = info.get('fecha')
    dinero = info.get('dinero')
    horas = info.get('horas')
    lugar = info.get('lugar')

    with open('registro.csv', 'a') as f:
        f.write(f'{fecha},{dinero},{horas},{lugar}\n')#escribe la informacion en el archivo csv.
        f.close()

# metodo para leer el archivo registro.csv (inacabada)
@app.route('/registro')
def registro():
    registros = {}
    i = 0
    with open('registro.csv', 'r') as f:
        for row in f:
            registros[f'linea{i}'] = row
            i+=1
        

    return render_template('registro.html',**registros)

# Metodo que genera la cookie y llama al metodo de escribir() para que se escriba en el archivo.
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
