from flask import Flask
from threading import Thread

app = Flask('app')

@app.route('/')
def main():
    return "https://discord.gg/m4ev9hQ94f"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()