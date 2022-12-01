from flask import send_file
from flask import Flask
from markupsafe import escape


import build
print("build done")


app = Flask(__name__, static_folder='build')


@app.errorhandler(404)
def page_not_found(e):
  return app.send_static_file("404.html"), 404


@app.route("/")
def index():
  return app.send_static_file("index.html")


def serve(fname):
  fname = fname.replace("&#39;", "'")
  try:
    return app.send_static_file(f"{fname}.html")
  except:
    return app.send_static_file(f"{fname}")


@app.route("/<name1>")
@app.route("/<name1>/<name2>")
@app.route("/<name1>/<name2>/<name3>")
def show(**names):
  return serve("/".join(escape(names[i]) for i in sorted(names.keys())))


app.run(port=8080)
