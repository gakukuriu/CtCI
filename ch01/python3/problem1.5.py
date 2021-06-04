def conversionCheckInsertOrDelete(s1, s2):
  if len(s1) == len(s2):
    return False
  else:
    minS = min(s1, s2, key=lambda s: len(s))
    maxS = max(s1, s2, key=lambda s: len(s))
    for c in minS:
      maxS = maxS.replace(c, '', 1)
    return len(maxS) == 1

def conversionCheckSub(s1, s2):
  if len(s1) != len(s2):
    return False
  else:
    test = s2
    for c in s1:
      test = test.replace(c, '', 1)
    return len(test) == 1


print('pale, ple - >', conversionCheckInsertOrDelete('pale', 'ple') or conversionCheckSub('pale', 'ple'))
print('pales, pale - >', conversionCheckInsertOrDelete('pales', 'pale') or conversionCheckSub('pales', 'pale'))
print('pale, bale - >', conversionCheckInsertOrDelete('pale', 'bale') or conversionCheckSub('pale', 'bale'))
print('pale, bake - >', conversionCheckInsertOrDelete('pale', 'bake') or conversionCheckSub('pale', 'bake'))
