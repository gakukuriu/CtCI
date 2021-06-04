def compressSentence(s):
  compS = []
  temp = []
  
  for c in s:
    if len(temp) == 0:
      temp.append(c)
    else:
      if temp[-1] == c:
        temp.append(c)
      else:
        compS.append(temp[-1] + str(len(temp)))
        temp = [c]
  compS.append(temp[-1] + str(len(temp)))
  
  s2 = ''.join(compS)
  if len(s) > len(s2):
    return s2
  else:
    return s

s = "aabcccccaaa"
print(compressSentence(s))

