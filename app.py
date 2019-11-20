from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
#This says what it says! :P
def index():
    return render_template('index.html')

@app.route('/classicOatmeal')
def classicOatmeal():
    return 'Hahaha... classic oatmeal!'

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
#the ip for this is 10.1.41.114 
