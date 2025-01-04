from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)


calculation_sequence = ""
numbers_entered = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression')
    try:
        expression = expression.replace("^", "**")
        
        result = eval(expression)
        global calculation_sequence, numbers_entered
        calculation_sequence = f"{expression} = {result}"
        numbers_entered.append(expression)
        
        return jsonify({
            'result': result,
            'calculation_sequence': calculation_sequence,
            'numbers_entered': numbers_entered
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        })

@app.route('/clear', methods=['POST'])
def clear():
    global calculation_sequence, numbers_entered
    calculation_sequence = ""
    numbers_entered = []
    return jsonify({
        'result': '',
        'calculation_sequence': '',
        'numbers_entered': []
    })

if __name__ == '__main__':
    app.run(debug=True)
