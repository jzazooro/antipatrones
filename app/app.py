from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora', methods=['POST'])
def calcular():
    operacion = request.form['operacion']
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])

    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
    elif operacion == 'division':
        if num2 == 0:
            return 'No se puede dividir entre cero'
        else:
            resultado = num1 / num2
    else:
        return 'Operación no válida'

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
