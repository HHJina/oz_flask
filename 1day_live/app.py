from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet")
def greet():
    # TODO: URL에서 name 값 받아오기
    name = request.args.get("name", type=str)
    age = request.args.get('age', type=int)

    # TODO: greet.html 반환
    return render_template("greet.html", name = name, age = age)


if __name__ == "__main__":
    app.run(debug=True)
