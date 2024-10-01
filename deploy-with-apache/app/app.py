from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_nginx():
    return "<h1 style='text-align: center;'>Hello, this is an Nginx server acting as a Reverse Proxy!</h1>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
