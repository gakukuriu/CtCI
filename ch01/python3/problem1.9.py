def isRotation(s1, s2):
  s = s1 + s1
  return s2 in s

s1 = 'waterbottle'
s2 = 'erbottlewat'

print(isRotation(s1, s2))