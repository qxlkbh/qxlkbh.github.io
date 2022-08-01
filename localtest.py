from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
  return open("build/index.html").read()


@app.route("/<name>")
def show(name):
  bb = escape(name)
  if bb.endswith(".html"):
    bb = bb[:-4]
  try:
    return open(f"build/{bb}.html").read()
  except FileNotFoundError:
    try:
      return open(f"build/{bb}").read()
    except UnicodeDecodeError:
      return open(f"build/{bb}", "rb").read()


@app.route("/<name>/<name2>")
def show2(name, name2):
  bb = escape(name) + "/" + escape(name2)
  if bb.endswith(".html"):
    bb = bb[:-4]
  try:
    return open(f"build/{bb}.html").read()
  except FileNotFoundError:
    try:
      return open(f"build/{bb}").read()
    except UnicodeDecodeError:
      return open(f"build/{bb}", "rb").read()


app.run(port=8080)
