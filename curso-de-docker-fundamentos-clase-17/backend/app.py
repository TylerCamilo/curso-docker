from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Amin",
        "lastname": "Espinoza",
        "socialMedia":
        {
            "facebookUser": "aminespinoza10",
            "instagramUser": "aminespinoza10",
            "xUser": "aminespinoza",
            "linkedin": "amin-espinoza",
            "githubUser": "aminespinoza10"
        },
        "blog": "https://aminespinoza.com",
        "author": "Miranda Espinoza"
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)