from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def list_todos():
    todos = #load your todos from your files
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
