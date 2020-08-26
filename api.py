from flask import Flask
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def hello():
    return "Hello World, it's wonderful to see you!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
