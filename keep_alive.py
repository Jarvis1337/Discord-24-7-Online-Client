from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return '<meta http-equiv="refresh" content="0; URL=https://yours-jarvis.github.io/Yours-Jarvis"/>'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

## <!-- 🚀 Please follow on GitHub to stay tuned with us for more Exciting future Updates like this. | © 2022 — Made By Your's Jarvis #2431 with ♥ -->