from time import time
import time
from flask import Flask, request, render_template
from gpa import getgpa


usergpa  = getgpa()

app=Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    try:
        id = request.form['idd']
        password = request.form['pas']
        (Overrallgpa ,last60gpa, l) =  usergpa.apply(id, password)
        return render_template('index.html', gpa = Overrallgpa, last60 = last60gpa, all = l)
    except Exception as e: 
        result = "輸入資料有誤"
        #result = e
        return render_template('index.html', gpa = result)
    #result = "OK"

@app.route('/index2')
def my_form2():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)