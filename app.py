from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find')
def find_spot():
    #index1.html을 접근하기 위해서는 /find로 접근해야한다
    return render_template('index1.html')

@app.route('/create')
def create_spot():
    return render_template('index2.html')

@app.route('/wonder')
def wonder_spot():
    return render_template('index3.html')

if __name__ == '__main__':
    app.run('localhost',port=5000,debug=True)
    #0.0.0.0