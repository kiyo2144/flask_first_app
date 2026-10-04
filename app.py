from flask import Flask

app = Flask(__name__)


# ルートデコレーション
@app.route("/")
def hello_world():
    return "Hello,World"


# [URL]/goodbyeページを表示すると"Goodbye"が表示される
@app.route("/goodbye")
def goodbye():
    return "Goodbye"


# [URL]/user/<name>ページを表示すると"<name>"が表示される
@app.route("/user/<name>")
def hi(name):
    return f"Hi, {name}!"


# [URL]/helloページを表示すると見出し1で"Hello"が表示される
@app.route("/hello")
def hello():
    html = "<html><body><h1>Hello</h1></body></html>"
    return html


# [URL]/helloページを表示すると見出し1で"<neme>'s Hello"が表示される
@app.route("/profile/<name>")
def profile(name):
    html = f"<html><body><h1>{name}'s Hello</h1></body></html>"
    return html


if __name__ == "__main__":
    # 使用するポートを明示
    app.run(port=8000)  # ポートを指定しない場合はデフォルトで5000になる
