# 유클리드 호제법


def Euclidean(a, b):

  r = b % a

  if r == 0:
    return a
  else:
    return Euclidean(r, a)