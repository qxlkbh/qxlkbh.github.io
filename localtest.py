from flask import Flask
from markupsafe import escape

app = Flask(__name__, static_folder='build')


@app.route("/")
def index():
  return app.send_static_file("index.html")


def serve(fname):
  if any(fname.endswith(x) for x in [".ico", ".png", ".webmanifest", ".html"]):
    return app.send_static_file(f"{fname}")
  return app.send_static_file(f"{fname}.html")


@app.route("/<name1>")
@app.route("/<name1>/<name2>")
@app.route("/<name1>/<name2>/<name3>")
def show(**names):
  return serve("/".join(escape(names[i]) for i in sorted(names.keys())))


app.run(port=8080)
