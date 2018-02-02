from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/Hello_World")
def hello_world():

    return "Hello World!"


@app.route("/Hello")
def hello():

    return "Only Hello!"


if __name__ == "__main__":
      app.run()
