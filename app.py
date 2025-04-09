from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Здрасти, сайтът ти работи! 🚀"

if __name__ == '__main__':
    app.run()
