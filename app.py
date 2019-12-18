import asyncio
import websockets

async def hello(websocket, path):
    greeting = f"Hello!"
    await websocket.send(greeting)
    print(f"> {greeting}")
start_server = websockets.serve(hello, "10.1.41.116", 8888)
#asyncio.get_event_loop().run_until_complete(start_server)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
#This says what it says! :P
def index():
    return render_template('index.html')

counter = 0
@app.route("/")
def counter():
    global counter
    counter += 1
    return str(counter)

@app.route('/classicOatmeal')
def classicOatmeal():
    #return 'Hahaha... classic oatmeal!'
    user = {'username': 'Miguel'}
    return 'hello'

@app.route('/hello/<name>')
def hello(name):
    print (counter)
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
#the ip for this is 10.1.41.114
