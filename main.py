from flask import Flask, render_template

app = Flask(__name__)

#zadana ruta, kada odemo na route link, on ce pozvati ovu index funkciju (index se koristi jer je to bazično kao)
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()