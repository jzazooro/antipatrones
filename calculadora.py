from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora', methods=['POST'])
def calcular(operacion, num1, num2): 
    if operacion == 'suma':
        return num1 + num2
    if operacion == 'resta':
        return num1 - num2
    if operacion == 'multiplicacion':
        return num1 * num2
    if operacion == 'division':
        if num2 == 0:
            return 'No se puede dividir entre cero'
        if num2 != 0:
            return num1 / num2
    else:
        return 'Operación no válida'