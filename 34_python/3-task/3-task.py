from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Saugojimo vieta
user_data = {}

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        user_data["name"] = name
        user_data["email"] = email
        return redirect(url_for("result"))
    return render_template("form.html")

@app.route("/result")
def result():
    return render_template("result.html", data=user_data)

if __name__ == "__main__":
    app.run(debug=True)