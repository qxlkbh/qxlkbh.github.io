import os
import shutil
import re

import ext
import ext.resource
import ext.wood as wood
from ext import use

import sys
if "-h" in sys.argv:
  print("why are you reading this")
  print("-ll=<log level>")
  print("-rc  refresh cack")
  sys.exit(0)


class Holder():
  pass


glo = Holder()
ext.init(glo)


def substitute(template: str, setup: Holder, fullpath: str):
  dynamic = Holder()
  ext.ppgsetup(template, setup, fullpath, dynamic)
  context = {"glo": glo, "dynamic": dynamic, "setup": setup}
  src = open(f"templates/{template}").read()
  pat = re.compile("\{\{ (.*?) \}\}")
  x = re.search(pat, src)
  while x is not None:
    var = x.group(1)
    l, r = x.span()
    ___ = Holder()
    for i in context:
      var = var.replace(i, "___." + i)
      vars(___)[i] = context[i]
    if var.startswith("##EXEC "):
      src = src[:l] + src[r:]
      try:
        # very good practice.
        ldct = dict(locals())
        exec(var[7:], globals(), ldct)
        src = ldct["src"]
      except Exception as e:
        wood.log("execution error %s on %s" % (str(e), fullpath), 1)
    else:
      d = ""
      try:
        d = eval(var)
      except Exception as e:
        wood.log("evaluation error %s on %s" % (str(e), fullpath), 1)
      src = src[:l] + d + src[r:]
    x = re.search(pat, src)
  return ext.resource.subst(src, fname=fullpath)


shutil.rmtree("build", ignore_errors=True)

# bees
shutil.copytree("bees", "build")
shutil.copytree("comics", "build/comics")
shutil.copy("qxlkbh.png", "build")

# readd
li = []
for temp in os.listdir("source"):
  if temp[0] == '_':
    wood.log("you aren't supposed to be using template %s" % temp, 1)
  for sub in os.listdir(f"source/{temp}"):
    setup = Holder()
    curvar = ""
    for i in open(f"source/{temp}/{sub}", encoding="utf8"):
      if i.strip().endswith("==="):
        curvar = i.strip()[:-3]
        vars(setup)[curvar] = ""
      else:
        vars(setup)[curvar] += i
    li += [(f"build/{sub}.html", temp, setup, f"source/{temp}/{sub}")]
    ext.addpage(temp, sub, setup)

ext.glosetup(glo)

# substitue
for targ, temp, setup, fullpath in li:
  open(targ, "w", encoding="utf8").write(substitute(temp, setup, fullpath))

# print(glob.glob("source/*"))
# print(os.listdir("source"))
