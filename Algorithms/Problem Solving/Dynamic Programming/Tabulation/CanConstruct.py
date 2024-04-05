def CanConstruct(target, words):
  if target == "":
    return True
  
  letterTable = [False] * (len(target) + 1)
  letterTable[0] = True

  for letters in range(len(letterTable)):
    if letterTable[letters]:
      for word in words:
        if target[letters:letters + len(word)] == word:
          if letters + len(word) < len(letterTable):
            letterTable[letters + len(word)] = True

  return letterTable[len(target)]


print(CanConstruct("abcdef", ["abc", "def", "abcd"]))