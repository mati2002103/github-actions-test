from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Witaj! To moja pierwsza aplikacja we Flasku działająca od zera.'

if __name__ == '__main__':
    # Uruchamiamy na wszystkich interfejsach (0.0.0.0), co ułatwia pracę z Dockerem później
    app.run(host='0.0.0.0', port=5000, debug=True)