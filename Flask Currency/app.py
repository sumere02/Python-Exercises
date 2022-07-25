from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])
def index():
    if request.method == "POST":
        response = requests.get("http://data.fixer.io/api/latest?access_key=b824f9280e65cb54543613435fc8770e")
        data = response.json()
        first_currency = request.form.get('firstCurrency')
        second_currency = request.form.get("secondCurrency")
        amount = float(request.form.get("amount"))
        first_value = float(data["rates"][first_currency])
        second_value = float(data["rates"][second_currency])
        value = second_value/first_value
        result = amount*value
        info = {
            "result":result,
            "amount":amount,
            "firstCurrency":first_currency,
            "secondCurrency":second_currency
        }
        return render_template("index.html",info = info)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)