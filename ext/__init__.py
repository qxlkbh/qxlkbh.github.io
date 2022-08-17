import os

import ext.navgen
import ext.forceload

firstComic = None
lastComic = None
beespages = []


def init(glo):
  global firstComic, lastComic
  _lc = 1
  while str(_lc + 1) in os.listdir("source/comic"):
    _lc += 1
  glo.lastComic = str(_lc)
  firstComic = 1
  lastComic = int(glo.lastComic)


def path_to_comic(comic: int):
  return "/" + str(comic)


def addpage(temp, sub, setup):
  if temp == "beespage":
    global beespages
    beespages += [(int(setup.priority), sub, setup.title)]


def glosetup(glo):
  global beespages
  glo.beespageindex = "<ul>"
  for _, id, tit in sorted(beespages):
    glo.beespageindex += f'<li><a href="/{id}">{id}: {tit}</a></li>'
  glo.beespageindex += "</ul>"


def ppgsetup(template: str, setup, fullpath: str, dynamic):
  if template == "comic":
    dynamic.navbar = ""
    pg = setup.pg
    links = []
    nav = []
    if hasattr(setup, "nav"):
      nav = setup.nav.split("\n")
    if "default" in nav:
      try:
        pg = int(pg)
        if pg != lastComic:
          links += [("&gt;&gt;", path_to_comic(lastComic))]
          links += [("&gt;", path_to_comic(pg + 1))]
        if pg != firstComic:
          links += [("&lt;", path_to_comic(pg - 1))]
          links += [("&lt;&lt;", path_to_comic(firstComic))]
      except ValueError as e:
        print("[warn] default nav failed for %s: %s" % (fullpath, str(e)))
        pass
    try:
      for x in nav:
        if " --> " in x:
          a, b = x.split(" --> ")
          links += [(a, b)]
    except ValueError:
      print("[warn] custom nav failed for %s: %s" % (fullpath, str(e)))
      pass
    dynamic.navbar = ext.navgen.gennav(links)
