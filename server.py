from iaCode import iaFunc
from flask import Flask
app = Flask(__name__)
res = iaFunc()

@app.route("/")
def index():
    return {
        "obj": res,
    }

if __name__ == "__main__":
    app.run(debug=True)