from flask import Flask
import matplotlib

app = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello from server!"


@app.route("/chart")
def main():
    return "Hello from chart"


if __name__ == "__main__":
    app.run()

