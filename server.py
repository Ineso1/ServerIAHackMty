from flask import Flask
import MainPage from "./src/MainPage.js"
app = Flask(__name__)

@app.route("/")
def index():
    return '<MainPage/>'

if __name__ == "__main__":
    app.run(debug=True)