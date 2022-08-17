def forceload(fname, alt=""):
  try:
    return open(fname).read()
  except:
    return alt
