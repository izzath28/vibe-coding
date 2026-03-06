from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        m1 = float(request.form["m1"])
        m2 = float(request.form["m2"])
        m3 = float(request.form["m3"])

        avg = (m1 + m2 + m3) / 3

        if avg >= 40:
            status = "Pass 🎉"
        else:
            status = "Fail ❌"

        result = {
            "name": name,
            "avg": round(avg, 2),
            "status": status
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)