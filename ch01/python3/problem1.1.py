def notOverlap(s):
  s_set = set(s)
  return len(s_set) == len(s)


def printNotOverlap(s):
  if notOverlap(s):
    print('"' + s + '"に重複する文字はありません')
  else:
    print('"' + s + '"には重複する文字があります')

s1 = "Yokai Jaki"
s2 = "永野"

printNotOverlap(s1)
printNotOverlap(s2)