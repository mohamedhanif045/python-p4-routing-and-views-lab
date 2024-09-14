from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Prints to console
    return parameter  # Displays in browser

@app.route('/count/<int:parameter>')
def count(parameter):
    # Return numbers separated by newline characters
    return '\n'.join(str(i) for i in range(parameter))

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return 'Division by zero is undefined', 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400
    return str(result)

if __name__ == '__main__':
    app.run(port=5555)
