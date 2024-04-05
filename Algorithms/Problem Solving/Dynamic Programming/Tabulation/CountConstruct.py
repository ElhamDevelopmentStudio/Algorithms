def CanConstruct(target, words):
  if target == "":
    return 1
  
  letterTable = [0] * (len(target) + 1)
  letterTable[0] = 1

  for letters in range(len(letterTable)):
    for word in words:
      if target[letters: letters + len(word)] == word:
        letterTable[letters + len(word)] += letterTable[letters]

  return letterTable[len(target)]


print(CanConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))