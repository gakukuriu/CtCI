def permutationCheck(s1, s2):
  if len(s1) != len(s2):
    return False
  else:
    test = s2
    for c in s1:
      test = test.replace(c, '', 1)
    return test == ""

def printPermutationCheck(s1, s2):
  if permutationCheck(s1, s2):
    print(s1 + "は" + s2 + "の並び換えです。")
  else:
    print(s1 + "は" + s2 + "の並び換えではありません。")


s1 = "コウメ太夫"
s2 = "赤井貴"
s3 = "ロレックス"
s4 = "クスロレッ"

printPermutationCheck(s1, s2)
printPermutationCheck(s3, s4)

