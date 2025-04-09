from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Начална страница работи! 🚀"

@app.route('/program/olx')
def olx():
    return render_template('olx.html')

if __name__ == '__main__':
    app.run()
