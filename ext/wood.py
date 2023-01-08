import sys

loglevel = 1
for i in sys.argv:
  if i.startswith("-ll="):
    loglevel = int(i[4:])


def log(s, l=3):
  if l <= loglevel:
    print("[%s] %s" % (["FAIL", "warn", "info", "dbug"][l], s))

log(f"loglevel = {loglevel}")