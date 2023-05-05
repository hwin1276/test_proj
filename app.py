from flask import Flask, render_template, request
from views import fz, fb, cb

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/fizzbuzz/", methods=['GET', 'POST'])
def fizzbuzz():
    result = ' '
    if request.method == 'POST':
        input = int(request.form.get('input'))
        first = int(request.form.get('first'))
        second = int(request.form.get('second'))
        phrase1 = str(request.form.get('phrase1'))
        phrase2 = str(request.form.get('phrase2'))
        for i in range(0, input+1):
            result = result + " " + fz(i, first, second, phrase1, phrase2)

    return render_template("fizzbuzz.html", result=result)

@app.route("/fibonacci/", methods=['GET', 'POST'])
def fibonacci():
    result = ' '
    finput = 0
    if request.method == 'POST':
        x = int(request.form.get('x'))
        y = int(request.form.get('y'))
        z = int(request.form.get('z'))
        result = result + str(fb(x, y, z)) + ", "
        # display x in result
        finput = x

    return render_template("fibonacci.html", result=result, finput=finput)

@app.route("/combined/", methods=['GET', 'POST'])
def combined():
    result = ''
    finput = 0
    if request.method == 'POST':
        # default values indicated after 'or'
        d1 = int(request.form.get('first')) or 3
        d2 = int(request.form.get('second')) or 5
        p1 = str(request.form.get('phrase1')) or "Fizz"
        p2 = str(request.form.get('phrase2')) or "Buzz"
        x = int(request.form.get('x'))
        y = int(request.form.get('y')) or 1
        z = int(request.form.get('z')) or 2
        result= cb(x, y, z, d1, d2, p1, p2)
        # display x in result
        finput = x
    return render_template("combined.html", result=result, finput=finput)