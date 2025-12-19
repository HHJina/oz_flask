from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello!!!!"

@app.route("/user/<username>")
def greet(username):
    # return f"안녕하세요 {name}님, {age}살이시네요?"
    return render_template("user.html", username = username)

@app.route("/hello")
def hello():
    return render_template('hello.html', name = "황현진")

@app.route("/fruits")
def fruits():
    fruits = ['멜론', '바나나', '포도', '멜론', '망고']
    return render_template('fruits.html', fruits = fruits)

if __name__ == "__main__":
    app.run(debug=True)