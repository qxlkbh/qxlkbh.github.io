import urllib.request
import re
import os.path
try:
  import ext.wood as wood
except:
  import wood
import time
import sys
import json

pat = re.compile('src="(/.*?)"')

ARCHIVES = ["https://qxlkbh.github.io/archive-1/"]

thing = []

try:
  f = json.load(open("cack.json", "r"))
  if time.time() - f["time"] < 86000 and "-rc" not in sys.argv:
    for i in ARCHIVES:
      thing += [f[i]]
  else:
    0 // 0
except:
  f = {"time": time.time()}
  for i in ARCHIVES:
    thing += [urllib.request.urlopen(
      i).read().decode("utf8").strip().split("\n")]
    f[i] = thing[-1]
  json.dump(f, open("cack.json", "w"))

wood.log("finished reading archives", l=2)


def resolve(x, fname):
  assert x[0] == "/"
  x = x[1:]
  if os.path.isfile(x) or os.path.isfile("bees/" + x):
    wood.log(f"{fname}: {x} found locally")
    return x
  for i, j in zip(ARCHIVES, thing):
    if x in j:
      wood.log(f"{fname}: {x} found in {i}")
      return i + x
  wood.log(f"{fname}: {x} does not exist", 1)
  return x


def subst(src, fname="?"):
  x = re.search(pat, src)
  while x is not None:
    var = x.group(1)
    l, r = x.span()
    src = src[:l] + f'src[SUBBED]="{resolve(var, fname)}"' + src[r:]
    x = re.search(pat, src)
  return src.replace("[SUBBED]", "")
