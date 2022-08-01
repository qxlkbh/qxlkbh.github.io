import os
import shutil
import distutils.dir_util
import re


class Holder():
  pass


glo = Holder()

# setupdynamic
_lc = 1
while str(_lc + 1) in os.listdir("source/comic"):
  _lc += 1
glo.lastComic = str(_lc)

firstComic = 1
lastComic = int(glo.lastComic)


def path_to_comic(comic: int):
  return "/" + str(comic) + ".html"


def resolve(var: str, context: dict, fullpath: str):
  ___ = Holder()
  for i in context:
    var = var.replace(i, "___." + i)
    vars(___)[i] = context[i]
  try:
    return eval(var)
  except Exception as e:
    print("Warning: error %s on %s" % (str(e), fullpath))
    return ""


def substitute(template: str, setup: Holder, fullpath: str):
  dynamic = Holder()
  if template == "comic":
    dynamic.navbar = ""
    pg = setup.pg
    try:
      pg = int(pg)
      if pg == lastComic:
        dynamic.navbar = '<a href="%s">&lt;</a> <a href="%s">&lt;&lt;</a>' % \
          (path_to_comic(pg - 1), path_to_comic(firstComic))
      elif pg == firstComic:
        dynamic.navbar = '<a href="%s">&gt;&gt;</a> <a href="%s">&gt;</a>' % \
          (path_to_comic(lastComic), path_to_comic(pg + 1))
        # dynamic.navbar = '<a href="%s">&gt;&gt;</a> <a href="%s">&gt;</a>' % \
        #   ("/index.html", path_to_comic(pg + 1))
      else:
        dynamic.navbar = '<a href="%s">&gt;&gt;</a> <a href="%s">&gt;</a> <a href="%s">&lt;</a> <a href="%s">&lt;&lt;</a>' %\
          (path_to_comic(lastComic), path_to_comic(pg + 1),
           path_to_comic(pg - 1), path_to_comic(firstComic))
        # dynamic.navbar = '<a href="%s">&gt;&gt;</a> <a href="%s">&gt;</a> <a href="%s">&lt;</a> <a href="%s">&lt;&lt;</a>' %\
        #   ("/index.html", path_to_comic(pg + 1),
        #    path_to_comic(pg - 1), path_to_comic(firstComic))
    except ValueError:
      pass
  context = {"glo": glo, "dynamic": dynamic, "setup": setup}
  src = open(f"templates/{template}").read()
  s = re.finditer("\{\{ (.*?) \}\}", src)
  for i in s:
    src = src.replace(i.group(0), resolve(i.group(1), context, fullpath))
  return src


shutil.rmtree("build", ignore_errors=True)
os.mkdir("build")

# bees
distutils.dir_util.copy_tree("bees", "build")
distutils.dir_util.copy_tree("comics", "build/comics")
shutil.copy("qxlkbh.png", "build")

# substitue
for temp in os.listdir("source"):
  for sub in os.listdir(f"source/{temp}"):
    setup = Holder()
    curvar = ""
    for i in open(f"source/{temp}/{sub}"):
      if i.strip().endswith("==="):
        curvar = i.strip()[:-3]
        vars(setup)[curvar] = ""
      else:
        vars(setup)[curvar] += i
    comp = substitute(temp, setup, f"source/{temp}/{sub}")
    open(f"build/{sub}.html", "w").write(comp)

# print(glob.glob("source/*"))
# print(os.listdir("source"))
