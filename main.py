from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def submit_form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        with open("form.txt", "a", encoding="utf-8") as f:
            f.write(f"Ad: {name}\n")
            f.write(f"E-posta: {email}\n")
            f.write(f"Mesaj: {message}\n")
            f.write("-" * 30 + "\n")

        return render_template(
            "form_result.html",
            name=name,
            email=email,
            message=message
        )

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
