import itertools

def palindromeCheck(s):
  s1 = s.replace(' ', '').lower()
  for p in itertools.permutations(s1, len(s1)):
    s2 = ''.join(p)
    if s2[::-1] == s2:
      return True
  return False

s = "Tact Coa"
print(palindromeCheck(s))

