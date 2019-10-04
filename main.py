# IMPORTS DE LAS LIBRERIAS DE FLASK
from flask import Flask, render_template, redirect, url_for, request
# imports de otras librerias
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# Metodo para escribir en archivo.csv, la informacion llega a traves de una cookie que se genera en el navegador despues de darle a enviar.


def escribir(fecha='00/00/0000', dinero=0, horas=0, lugar=' '):

    with open('registro.csv', 'a') as f:
        # escribe la informacion en el archivo csv.
        f.write(f'{fecha},{dinero},{horas},{lugar}\n')
        f.close()

# metodo para leer el archivo registro.csv (inacabada)
@app.route('/registro')
def registro():

    resultados = []
    with open("registro.csv") as archivo:
        reader = csv.reader(archivo)
        for row in reader:
            resultados.append(row)

    return render_template('registro.html', **resultados)

# Metodo que genera la cookie y llama al metodo de escribir() para que se escriba en el archivo.
@app.route('/enviar', methods=['POST'])
def enviar():
    fecha = request.form.get('fecha')
    lugar = request.form.get('lugar')
    dinero = request.form.get('dinero')
    horas = request.form.get('horas')
    response = redirect(url_for('home'))
    escribir(fecha, dinero, horas, lugar)
    return response


@app.errorhandler(404)
def error(error):
    return '<h1> Pagina no encontrada...(404)<h1>'


if __name__ == "__main__":
    app.run('0.0.0.0', '8080', debug=True)
