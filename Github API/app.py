from flask import Flask,render_template,request
import requests


app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        user = request.form.get("githubname")
        url = "https://api.github.com/users/"+user
        response = requests.get(url)
        profile = response.json()
        if "message" not in profile:
            url = url + "/repos"
            response = requests.get(url)
            repos = response.json()
            return render_template("index.html",profile = profile,repos = repos)
        else:
            error = "User Not Found"
            return render_template("index.html",error = error)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)