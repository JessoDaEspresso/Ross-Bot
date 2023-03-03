from flask import Flask
from threading import Thread

app = Flask('')

# home route
@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='localhost', port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
    
keep_alive()