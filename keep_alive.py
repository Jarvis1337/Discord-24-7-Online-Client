from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "🚀 Please follow on GitHub to stay tuned with us for more Exciting future Updates like this. | © 2021 — Made By Your's Jarvis #2431 with ♥"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
