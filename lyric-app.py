from flask import Flask, render_template, jsonify
import lyrics
import api
app = Flask(__name__)

app.register_blueprint(api.api, url_prefix="/api")

@app.route("/")
def hello():
    return render_template("base.html",)

if __name__=="__main__":
    app.run(debug=True)