import os
import shutil
import distutils.dir_util

glo = {}

# setupdynamic
_lc = 1
while str(_lc + 1) in os.listdir("source/comic"):
  _lc += 1
glo["lastComic"] = str(_lc)

firstComic = 1
lastComic = int(glo["lastComic"])


def path_to_comic(comic: int):
  return "/" + str(comic) + ".html"


def substitute(template: str, setup: dict, fullpath: str):
  dynamic = {"navbar": ""}
  if template == "comic":
    pg = setup["pg"]
    try:
      pg = int(pg)
      if pg == lastComic:
        dynamic["navbar"] = '<a href="%s">&lt;</a> <a href="%s">&lt;&lt;</a>' % \
          (path_to_comic(pg - 1), path_to_comic(firstComic))
      elif pg == firstComic:
        dynamic["navbar"] = '<a href="%s">&gt;&gt;</a> <a href="%s">&gt;</a>' % \
          (path_to_comic(lastComic), path_to_comic(pg + 1))
      else:
        dynamic["navbar"] = '<a href="?pg=%s">&gt;&gt;</a> <a href="%s">&gt;</a> <a href="%s">&lt;</a> <a href="%s">&lt;&lt;</a>' %\
          (path_to_comic(lastComic), path_to_comic(pg + 1),
           path_to_comic(pg - 1), path_to_comic(firstComic))
    except ValueError:
      pass
  src = open(f"templates/{template}").read()
  for x in setup:
    src = src.replace("{{ setup.%s }}" % x, setup[x])
  for x in glo:
    src = src.replace("{{ glo.%s }}" % x, glo[x])
  for x in dynamic:
    src = src.replace("{{ dynamic.%s }}" % x, dynamic[x])
  if "{{" in src:
    print("Warning: %s has unreplaced variables", fullpath)
  return src


shutil.rmtree("build")
os.mkdir("build")

# bees
distutils.dir_util.copy_tree("bees", "build")
distutils.dir_util.copy_tree("comics", "build/comics")
shutil.copy("qxlkbh.png", "build")

# substitue
for temp in os.listdir("source"):
  for sub in os.listdir(f"source/{temp}"):
    setup = {"": ""}
    curvar = ""
    for i in open(f"source/{temp}/{sub}"):
      if i.strip().endswith("==="):
        curvar = i.strip()[:-3]
        setup[curvar] = ""
      else:
        setup[curvar] += i
    comp = substitute(temp, setup, f"source/{temp}/{sub}")
    open(f"build/{sub}.html", "w").write(comp)

# print(glob.glob("source/*"))
# print(os.listdir("source"))
