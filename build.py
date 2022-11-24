import os
import shutil
import distutils.dir_util
import re

import ext


class Holder():
  pass


glo = Holder()
ext.init(glo)


def substitute(template: str, setup: Holder, fullpath: str):
  dynamic = Holder()
  ext.ppgsetup(template, setup, fullpath, dynamic)
  context = {"glo": glo, "dynamic": dynamic, "setup": setup}
  src = open(f"templates/{template}").read()
  x = re.search("\{\{ (.*?) \}\}", src)
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
        print("[warn] execution error %s on %s" % (str(e), fullpath))
    else:
      d = ""
      try:
        d = eval(var)
      except Exception as e:
        print("[warn] evaluation error %s on %s" % (str(e), fullpath))
      src = src[:l] + d + src[r:]
    x = re.search("\{\{ (.*?) \}\}", src)
  return src


shutil.rmtree("build", ignore_errors=True)
os.mkdir("build")

# bees
distutils.dir_util.copy_tree("bees", "build")
distutils.dir_util.copy_tree("comics", "build/comics")
shutil.copy("qxlkbh.png", "build")

# readd
li = []
for temp in os.listdir("source"):
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
